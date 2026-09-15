/* IA além do chat — motor do deck. Sem dependências; funciona offline. */
(() => {
  'use strict';
  const doc = document.documentElement;
  if (!doc.lang) doc.lang = 'pt-BR';
  const params = new URLSearchParams(location.search);
  const estatico = params.has('static');
  if (estatico) doc.classList.add('static');
  const semMovimento = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const $ = id => document.getElementById(id);
  const viewport = $('viewport'), deck = $('deck'), hud = $('hud');
  const notas = $('notas'), aviso = $('aviso'), breu = $('breu');
  const slides = Array.from(deck.querySelectorAll(':scope > .slide'));
  const W = 1920, H = 1080;
  let atual = 0, passo = 0, ultimo = -1, overview = false, editando = false;
  let apresentador = null, inicio = Date.now(), digitos = '', avisoTimer = 0;

  const limita = i => Math.max(0, Math.min(slides.length - 1, i));
  const maxPasso = s => {
    let m = 0;
    s.querySelectorAll('[data-step]').forEach(e => { m = Math.max(m, +e.dataset.step || 0); });
    return m;
  };

  /* ---------- ganchos de slide (animações com dados) ---------- */
  const ganchos = {
    // Campo de pontos em escala: cada ponto é uma submissão.
    pontos(slide, animar) {
      const c = slide.querySelector('canvas[data-total]');
      if (!c) return;
      const total = +c.dataset.total, destaque = +c.dataset.destaque, linhas = +c.dataset.linhas;
      const cw = +c.dataset.w, ch = +c.dataset.h;
      const k = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
      c.width = cw * k; c.height = ch * k;
      c.style.width = cw + 'px'; c.style.height = ch + 'px';
      const ctx = c.getContext('2d');
      ctx.setTransform(k, 0, 0, k, 0, 0);
      const colunas = Math.ceil(total / linhas), p = cw / colunas, r = p * 0.37;
      const css = getComputedStyle(doc);
      const corIA = css.getPropertyValue('--maquina').trim() || '#FF6B21';
      const corResto = '#AEB6C2';
      const pinta = (de, ate, cor, limite) => {
        ctx.fillStyle = cor;
        ctx.beginPath();
        for (let col = de; col < ate; col++) {
          for (let lin = 0; lin < linhas; lin++) {
            const i = col * linhas + lin;
            if (i >= limite) break;
            const x = col * p + p / 2, y = lin * p + p / 2;
            ctx.moveTo(x + r, y);
            ctx.arc(x, y, r, 0, Math.PI * 2);
          }
        }
        ctx.fill();
      };
      const colsIA = Math.ceil(destaque / linhas);
      ctx.clearRect(0, 0, cw, ch);
      pinta(0, colunas, corResto, total);
      if (!animar || estatico || semMovimento) { pinta(0, colsIA, corIA, destaque); return; }
      const t0 = performance.now(), dur = 2600;
      let feito = 0;
      const quadro = t => {
        const f = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - f, 3);
        const alvo = Math.min(colsIA, Math.ceil(e * colsIA));
        if (alvo > feito) { pinta(feito, alvo, corIA, destaque); feito = alvo; }
        if (f < 1 && slide.classList.contains('is-active')) requestAnimationFrame(quadro);
        else pinta(0, colsIA, corIA, destaque);
      };
      requestAnimationFrame(quadro);
    }
  };

  /* Ondas determinísticas (ordem e ruído) para o slide do amplificador. */
  function desenhaOndas() {
    const semente = s => () => {
      s |= 0; s = s + 0x6D2B79F5 | 0;
      let t = Math.imul(s ^ s >>> 15, 1 | s);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
    document.querySelectorAll('path[data-onda]').forEach(el => {
      const [tipo, x0, y0, w, amp, ciclos, seed] = el.dataset.onda.split(',');
      const n = 96, pts = [];
      const rnd = semente(+seed || 7);
      let v = 0;
      for (let i = 0; i <= n; i++) {
        const t = i / n;
        let y;
        if (tipo === 'ordem') y = Math.sin(t * Math.PI * 2 * +ciclos);
        else { v = 0.35 * v + 0.65 * (rnd() * 2 - 1); y = v * 1.25; }
        pts.push(`${(+x0 + t * +w).toFixed(1)} ${(+y0 - y * +amp).toFixed(1)}`);
      }
      el.setAttribute('d', 'M' + pts.join(' L'));
    });
  }

  /* ---------- trilha de progresso ---------- */
  function montaHud() {
    const grupos = document.createElement('div');
    grupos.className = 'grupos';
    let nome = null, g = null;
    slides.forEach(s => {
      if (s.dataset.grupo !== nome || !g) {
        g = document.createElement('div'); g.className = 'grupo';
        grupos.appendChild(g); nome = s.dataset.grupo;
      }
      const p = document.createElement('span'); p.className = 'ponto'; g.appendChild(p);
    });
    const numero = document.createElement('span'); numero.className = 'numero';
    hud.replaceChildren(grupos, numero);
  }
  function atualizaHud() {
    hud.querySelectorAll('.ponto').forEach((p, i) => {
      p.classList.toggle('passou', i < atual);
      p.classList.toggle('agora', i === atual);
    });
    const n = hud.querySelector('.numero');
    if (n) n.textContent = atual + 1;
  }

  /* ---------- notas e janela do apresentador ---------- */
  const titulo = s => s.dataset.titulo || '';
  const notaHTML = s => { const n = s.querySelector('.nota'); return n ? n.innerHTML : '<p>Sem notas.</p>'; };
  function atualizaNotas() {
    const s = slides[atual];
    notas.innerHTML = `<h4>Slide ${atual + 1} de ${slides.length}</h4><p><b>${titulo(s)}</b></p>${notaHTML(s)}`;
  }
  const doisDigitos = n => String(n).padStart(2, '0');
  function atualizaApresentador() {
    if (!apresentador || apresentador.closed) return;
    try {
      const d = apresentador.document, s = slides[atual], prox = slides[atual + 1];
      const falta = maxPasso(s) - passo;
      d.getElementById('n').textContent = `Slide ${atual + 1} de ${slides.length}` + (falta > 0 ? `  (faltam ${falta} clique${falta > 1 ? 's' : ''} neste slide)` : '');
      d.getElementById('t').textContent = titulo(s);
      d.getElementById('notas').innerHTML = notaHTML(s);
      d.getElementById('prox').textContent = prox ? `${atual + 2}. ${titulo(prox)}` : 'Fim';
    } catch (_) { /* janela fechada */ }
  }
  function atualizaRelogio() {
    if (!apresentador || apresentador.closed) return;
    try {
      const d = apresentador.document, seg = Math.floor((Date.now() - inicio) / 1000);
      d.getElementById('dec').textContent = `${doisDigitos(Math.floor(seg / 60))}:${doisDigitos(seg % 60)}`;
      const h = new Date();
      d.getElementById('hora').textContent = `${doisDigitos(h.getHours())}h${doisDigitos(h.getMinutes())}`;
    } catch (_) { /* janela fechada */ }
  }
  function abreApresentador() {
    apresentador = window.open('', 'apresentador-ia-alem-do-chat', 'width=1180,height=760');
    if (!apresentador) { mostraAviso('O navegador bloqueou a janela do apresentador. Permita pop-ups para este arquivo.'); return; }
    const d = apresentador.document;
    d.open();
    d.write(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Apresentador: IA além do chat</title><style>
      body{margin:0;font:19px/1.55 "Segoe UI",system-ui,sans-serif;background:#0D1119;color:#E6E9EF;display:grid;grid-template-columns:1fr 340px;height:100vh}
      main{padding:28px 40px;overflow:auto}aside{background:#151A26;padding:28px;display:flex;flex-direction:column;gap:22px}
      .n{font-size:15px;color:#9AA3B2}h1{font-size:30px;margin:6px 0 20px;line-height:1.15;color:#fff}#notas p{margin:0 0 12px;max-width:70ch}#notas b{color:#fff}
      .rot{font-size:14px;color:#9AA3B2}.relogio{font-size:54px;font-weight:700;font-variant-numeric:tabular-nums;line-height:1.05}
      #prox{font-size:19px;font-weight:600}.botoes{display:flex;gap:10px}
      button{font:600 17px "Segoe UI",sans-serif;padding:14px;border-radius:10px;border:0;background:#2350E6;color:#fff;cursor:pointer;flex:1}
      button.sec{background:#2A3142}button:focus-visible{outline:3px solid #FFE14D;outline-offset:2px}
    </style></head><body><main><div class="n" id="n"></div><h1 id="t"></h1><div id="notas"></div></main>
    <aside><div><div class="rot">Tempo desde que a janela abriu</div><div class="relogio" id="dec">00:00</div></div>
    <div><div class="rot">Hora</div><div class="relogio" id="hora" style="font-size:34px"></div></div>
    <div><div class="rot">Próximo slide</div><div id="prox"></div></div>
    <div class="botoes"><button class="sec" id="ant">Voltar</button><button id="av">Avançar</button></div>
    <button class="sec" id="zera">Zerar o tempo</button></aside></body></html>`);
    d.close();
    d.getElementById('av').onclick = proximo;
    d.getElementById('ant').onclick = anterior;
    d.getElementById('zera').onclick = () => { inicio = Date.now(); atualizaRelogio(); };
    d.addEventListener('keydown', teclas);
    inicio = Date.now();
    atualizaApresentador(); atualizaRelogio();
  }

  /* ---------- render e navegação ---------- */
  function render() {
    slides.forEach((s, i) => {
      const ativo = i === atual;
      s.classList.toggle('is-active', ativo);
      s.setAttribute('aria-hidden', ativo ? 'false' : 'true');
      if (ativo) s.querySelectorAll('[data-step]').forEach(e => e.classList.toggle('is-shown', +e.dataset.step <= passo));
    });
    const s = slides[atual];
    deck.dataset.tom = s.dataset.tom || 'claro';
    deck.dataset.hud = s.dataset.hud || 'sim';
    atualizaHud(); atualizaNotas(); atualizaApresentador();
    try { history.replaceState(null, '', '#' + (atual + 1) + (passo ? '.' + passo : '')); } catch (_) { /* sandbox */ }
    if (ultimo !== atual) {
      const g = s.dataset.gancho;
      if (g && ganchos[g]) ganchos[g](s, true);
      ultimo = atual;
    }
  }
  function proximo() {
    if (overview) { atual = limita(atual + 1); render(); return; }
    if (!estatico && passo < maxPasso(slides[atual])) { passo++; render(); return; }
    if (atual < slides.length - 1) { atual++; passo = 0; render(); }
  }
  function anterior() {
    if (overview) { atual = limita(atual - 1); render(); return; }
    if (!estatico && passo > 0) { passo--; render(); return; }
    if (atual > 0) { atual--; passo = estatico ? 0 : maxPasso(slides[atual]); render(); }
  }
  function ir(i, p = 0) { atual = limita(i); passo = p; render(); }

  /* ---------- escala, visão geral, lista ---------- */
  function layoutOverview() {
    const vw = viewport.clientWidth;
    const cols = vw > 1600 ? 6 : vw > 1150 ? 5 : vw > 820 ? 4 : 3;
    const w = Math.floor((vw - 22 * (cols + 1) - 18) / cols), sc = w / W;
    deck.style.setProperty('--ov-cols', cols);
    deck.style.setProperty('--ov-w', w + 'px');
    deck.style.setProperty('--ov-h', Math.round(H * sc) + 'px');
    deck.style.setProperty('--ov-s', sc.toFixed(5));
    return cols;
  }
  function ajusta() {
    const vw = doc.clientWidth || innerWidth, vh = innerHeight;
    const lista = params.has('lista') || (vw < 760 && vh > vw);
    doc.classList.toggle('lista', lista);
    if (lista) { deck.style.transform = ''; deck.style.setProperty('--ls', ((vw - 32) / W).toFixed(5)); return; }
    if (overview) { layoutOverview(); return; }
    const s = Math.min(vw / W, vh / H);
    deck.style.transform = `translate(${(vw - W * s) / 2}px, ${(vh - H * s) / 2}px) scale(${s})`;
  }
  function alternaOverview() {
    overview = !overview;
    viewport.classList.toggle('is-overview', overview);
    deck.classList.toggle('is-overview', overview);
    if (overview) {
      layoutOverview();
      slides[atual].scrollIntoView({ block: 'center' });
    } else { viewport.scrollTop = 0; passo = 0; ajusta(); }
    render();
  }

  /* ---------- tela cheia, aviso, edição ---------- */
  function telaCheia() {
    if (document.fullscreenElement) document.exitFullscreen();
    else if (doc.requestFullscreen) doc.requestFullscreen().catch(() => mostraAviso('Tela cheia indisponível aqui. Use F11.'));
  }
  function mostraAviso(txt, ms = 2600) {
    aviso.textContent = txt; aviso.classList.add('is-on');
    clearTimeout(avisoTimer);
    avisoTimer = setTimeout(() => aviso.classList.remove('is-on'), ms);
  }
  const EDITAVEIS = '.titulo,.frase,.grande,.corpo,.rotulo,.miudo,.fonte,.sec-titulo,[data-editavel]';
  function alternaEdicao() {
    editando = !editando;
    doc.classList.toggle('editando', editando);
    deck.querySelectorAll(EDITAVEIS).forEach(el => {
      if (editando) el.setAttribute('contenteditable', 'true'); else el.removeAttribute('contenteditable');
    });
    mostraAviso(editando ? 'Edição ligada: clique no texto. Ctrl+S salva uma cópia; Esc sai.' : 'Edição desligada', 4000);
  }
  /*SALVAR-INICIO*/
  function salvaCopia() {
    const clone = doc.cloneNode(true);
    clone.classList.remove('editando', 'static', 'lista');
    clone.querySelectorAll('[contenteditable]').forEach(el => el.removeAttribute('contenteditable'));
    ['is-active', 'is-shown', 'is-open', 'is-on', 'is-overview'].forEach(c =>
      clone.querySelectorAll('.' + c).forEach(el => el.classList.remove(c)));
    const d = clone.querySelector('#deck'); if (d) d.removeAttribute('style');
    const h = clone.querySelector('#hud'); if (h) h.innerHTML = '';
    const blob = new Blob(['<!doctype html>\n' + clone.outerHTML], { type: 'text/html' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'apresentacao-secim-visual-editada.html';
    document.body.appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
    mostraAviso('Cópia salva. Para mudar de vez, edite src/ e rode build.py.', 4000);
  }
  /*SALVAR-FIM*/

  /* ---------- teclado, toque, clique ---------- */
  function teclas(e) {
    const k = e.key;
    if (editando) {
      if (k === 'Escape') { alternaEdicao(); e.preventDefault(); }
      else if ((e.ctrlKey || e.metaKey) && k.toLowerCase() === 's') { e.preventDefault(); salvaCopia(); }
      return;
    }
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    if (/^[0-9]$/.test(k)) { digitos += k; mostraAviso(`Ir para o slide ${digitos} (Enter)`); e.preventDefault(); return; }
    if (k === 'Enter' && digitos) { ir(+digitos - 1); digitos = ''; aviso.classList.remove('is-on'); e.preventDefault(); return; }
    digitos = '';
    switch (k) {
      case 'ArrowRight': case 'PageDown': case ' ': proximo(); break;
      case 'ArrowDown': overview ? ir(atual + (+deck.style.getPropertyValue('--ov-cols') || 5)) : proximo(); break;
      case 'ArrowLeft': case 'PageUp': case 'Backspace': anterior(); break;
      case 'ArrowUp': overview ? ir(atual - (+deck.style.getPropertyValue('--ov-cols') || 5)) : anterior(); break;
      case 'Enter': overview ? alternaOverview() : proximo(); break;
      case 'Home': ir(0); break;
      case 'End': ir(slides.length - 1); break;
      case 'f': case 'F': telaCheia(); break;
      case 'o': case 'O': case 'g': case 'G': alternaOverview(); break;
      case 'n': case 'N': notas.classList.toggle('is-open'); break;
      case 'p': case 'P': abreApresentador(); break;
      case 'b': case 'B': case '.': breu.classList.toggle('is-on'); break;
      case 'e': case 'E': alternaEdicao(); break;
      case 'Escape':
        if (breu.classList.contains('is-on')) breu.classList.remove('is-on');
        else if (overview) alternaOverview();
        else notas.classList.remove('is-open');
        break;
      case '?': case 'h': case 'H':
        mostraAviso('Setas ou espaço: avançar e voltar. F tela cheia. O visão geral. N notas. P janela do apresentador. B tela preta. E editar. Número + Enter: ir ao slide.', 7000);
        break;
      default: return;
    }
    e.preventDefault();
  }
  document.addEventListener('keydown', teclas);
  let tx = null, ty = null;
  viewport.addEventListener('touchstart', e => {
    if (overview || doc.classList.contains('lista')) return;
    tx = e.touches[0].clientX; ty = e.touches[0].clientY;
  }, { passive: true });
  viewport.addEventListener('touchend', e => {
    if (tx === null) return;
    const dx = e.changedTouches[0].clientX - tx, dy = e.changedTouches[0].clientY - ty;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) (dx < 0 ? proximo : anterior)();
    tx = null;
  }, { passive: true });
  deck.addEventListener('click', e => {
    if (!overview) return;
    const s = e.target.closest('.slide');
    if (s) { atual = slides.indexOf(s); alternaOverview(); }
  });
  breu.addEventListener('click', () => breu.classList.remove('is-on'));
  addEventListener('resize', ajusta);
  addEventListener('hashchange', () => {
    const m = location.hash.match(/^#(\d+)(?:\.(\d+))?/);
    if (m) ir(+m[1] - 1, m[2] ? +m[2] : 0);
  });

  /* ---------- início ---------- */
  montaHud();
  desenhaOndas();
  slides.forEach(s => { const g = s.dataset.gancho; if (g && ganchos[g]) ganchos[g](s, false); });
  const m = location.hash.match(/^#(\d+)(?:\.(\d+))?/);
  if (m) { atual = limita(+m[1] - 1); passo = m[2] ? +m[2] : 0; }
  if (params.has('overview')) { overview = true; viewport.classList.add('is-overview'); deck.classList.add('is-overview'); layoutOverview(); }
  ajusta();
  if (m) ultimo = atual; // não reanima o slide aberto por link
  render();
  setInterval(atualizaRelogio, 1000);
  window.deckNav = { proximo, anterior, ir };
})();
