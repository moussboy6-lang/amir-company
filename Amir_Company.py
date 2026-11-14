"""Al Amir Quantum - lance le site complet depuis Python.
Utilisation :  python al_amir_quantum.py   (le navigateur s'ouvre tout seul)
"""
import http.server
import socketserver
import threading
import webbrowser
import os
PORT = int(os.environ.get("PORT", 8000))

HTML = r"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Al Amir Quantum</title>
<style>
:root{--bg:#02040c;--surface:rgba(8,16,36,.72);--text:#e6f6ff;--muted:#7f95b3;--c1:#00f0ff;--c2:#8a5cff;--c3:#ff3df2;--border:rgba(0,240,255,.22);
--grad:linear-gradient(120deg,var(--c1),var(--c2) 55%,var(--c3));color-scheme:dark}
*{box-sizing:border-box}
html{scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--text);font-family:"Segoe UI",system-ui,Arial,sans-serif;line-height:1.6;min-height:100%}
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:-2}
body::after{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,240,255,.03) 0 1px,transparent 1px 4px)}
header{position:sticky;top:0;z-index:9;display:flex;justify-content:space-between;align-items:center;padding:12px 20px;padding-top:calc(12px + env(safe-area-inset-top,0px));background:rgba(2,4,12,.8);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
.brand{font-family:"Courier New",monospace;font-weight:700;letter-spacing:.25em;text-decoration:none}
.g{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
nav a{color:var(--muted);text-decoration:none;margin-left:14px;font:.75rem "Courier New",monospace;letter-spacing:.1em;text-transform:uppercase}
nav a:hover{color:var(--c1)}
.view{max-width:920px;margin:0 auto;padding:36px 20px 70px}
.view[hidden]{display:none}
h1,h2{text-align:center;margin:0 0 10px;line-height:1.15}
h1{font-size:clamp(1.9rem,6vw,3.1rem)}
h2{font-size:clamp(1.6rem,5vw,2.3rem)}
.sub{text-align:center;color:var(--muted);margin:0 auto 24px;max-width:540px}
.tag{display:block;text-align:center;font:.75rem "Courier New",monospace;letter-spacing:.3em;color:var(--c1);margin-bottom:10px}
.core{display:block;width:100%;max-width:460px;margin:0 auto;overflow:visible}
.ring{fill:none;stroke:var(--c1);stroke-width:1;opacity:.55;transform-origin:200px 200px}
.r1{animation:spin 14s linear infinite}.r2{animation:spin 20s linear infinite reverse;stroke:var(--c2)}.r3{animation:spin 28s linear infinite;stroke:var(--c3)}
.e{fill:#fff;filter:drop-shadow(0 0 6px var(--c1))}
.pulse{animation:pl 3s ease-in-out infinite;transform-origin:200px 200px}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pl{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.15);opacity:1}}
.n{cursor:pointer;outline:none}
.n circle{fill:#050b1c;stroke:var(--c1);stroke-width:1.5;transition:.25s}
.n:hover circle,.n:focus circle{fill:rgba(0,240,255,.2);stroke:var(--c3);filter:drop-shadow(0 0 8px var(--c1))}
.n text{font:700 10px "Courier New",monospace;letter-spacing:.1em;fill:var(--text);text-anchor:middle;text-transform:uppercase}
.n .ic{font-size:13px;fill:var(--c1)}
.hint{text-align:center;color:var(--muted);font:.8rem "Courier New",monospace;margin-top:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:26px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px;backdrop-filter:blur(8px);transition:.25s}
.card:hover{border-color:var(--c1);box-shadow:0 0 28px rgba(0,240,255,.15);transform:translateY(-3px)}
.card.hl{border-color:var(--c3);box-shadow:0 0 30px rgba(255,61,242,.18)}
.num{font:.75rem "Courier New",monospace;letter-spacing:.2em;color:var(--c1)}
.card h3{margin:8px 0;font-size:1.1rem}
.card p{margin:0;color:var(--muted)}
.ava{width:52px;height:52px;border-radius:50%;background:var(--grad);color:#02040c;display:flex;align-items:center;justify-content:center;font-weight:800;margin-bottom:10px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:16px;text-align:center;border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:28px 0;margin-top:28px}
.stats b{display:block;font-size:2.2rem}
.stats span{color:var(--muted);font-size:.9rem}
.btn{display:inline-block;background:var(--grad);color:#02040c;padding:13px 28px;border-radius:999px;text-decoration:none;font-weight:700;box-shadow:0 0 28px rgba(138,92,255,.4)}
.back{display:block;width:max-content;margin:34px auto 0;color:var(--c1);text-decoration:none;border:1px solid var(--c1);padding:10px 22px;border-radius:999px;font:.85rem "Courier New",monospace}
.back:hover{background:rgba(0,240,255,.1)}
.center{text-align:center}
.tile{aspect-ratio:4/3;border:1px solid var(--border);border-radius:12px;background:linear-gradient(135deg,rgba(0,240,255,.08),rgba(138,92,255,.1));display:flex;align-items:center;justify-content:center;color:var(--c1);font:.8rem "Courier New",monospace;letter-spacing:.15em;text-transform:uppercase;transition:.25s}
.tile:hover{border-color:var(--c3);transform:translateY(-3px)}
footer{text-align:center;padding:22px 20px;color:var(--muted);font:.75rem "Courier New",monospace;border-top:1px solid var(--border)}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>
</head>
<body>
<canvas id="bg"></canvas>

<header>
  <a class="brand" href="#accueil"><span class="g">AL AMIR</span> <span style="color:var(--muted)">//Q</span></a>
  <nav><a href="#services">Services</a><a href="#apropos">Noyau</a><a href="#contact">Contact</a></nav>
</header>

<main>
<div class="view" id="accueil">
  <span class="tag">&gt; SYSTÈME EN LIGNE_</span>
  <h1>Bienvenue chez <span class="g">Al Amir Quantum</span></h1>
  <p class="sub">Entrez dans le noyau et explorez chaque module de notre univers numérique.</p>
  <svg class="core" viewBox="0 0 400 400" role="img" aria-label="Noyau quantique avec six modules">
    <defs><radialGradient id="cg"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="#00f0ff"/><stop offset="1" stop-color="#8a5cff" stop-opacity="0"/></radialGradient></defs>
    <g stroke="#00f0ff" stroke-opacity=".25"><path d="M200 200L340 200M200 200L270 321M200 200L130 321M200 200L60 200M200 200L130 79M200 200L270 79"/></g>
    <ellipse class="ring r1" cx="200" cy="200" rx="110" ry="40"/>
    <ellipse class="ring r2" cx="200" cy="200" rx="110" ry="40" style="transform:rotate(60deg)"/>
    <ellipse class="ring r3" cx="200" cy="200" rx="110" ry="40" style="transform:rotate(120deg)"/>
    <g class="r1"><circle class="e" cx="310" cy="200" r="4"/></g>
    <g class="r2"><circle class="e" cx="90" cy="200" r="4"/></g>
    <g class="r3"><circle class="e" cx="200" cy="160" r="4"/></g>
    <circle class="pulse" cx="200" cy="200" r="34" fill="url(#cg)"/>
    <g class="n" tabindex="0" onclick="location.hash='services'" onkeydown="if(event.key==='Enter')location.hash='services'"><circle cx="340" cy="200" r="22"/><text class="ic" x="340" y="205">⚙</text><text x="340" y="240">Services</text></g>
    <g class="n" tabindex="0" onclick="location.hash='tarifs'" onkeydown="if(event.key==='Enter')location.hash='tarifs'"><circle cx="270" cy="321" r="22"/><text class="ic" x="270" y="326">◆</text><text x="270" y="361">Tarifs</text></g>
    <g class="n" tabindex="0" onclick="location.hash='galerie'" onkeydown="if(event.key==='Enter')location.hash='galerie'"><circle cx="130" cy="321" r="22"/><text class="ic" x="130" y="326">▣</text><text x="130" y="361">Galerie</text></g>
    <g class="n" tabindex="0" onclick="location.hash='equipe'" onkeydown="if(event.key==='Enter')location.hash='equipe'"><circle cx="60" cy="200" r="22"/><text class="ic" x="60" y="205">☍</text><text x="60" y="240">Équipe</text></g>
    <g class="n" tabindex="0" onclick="location.hash='apropos'" onkeydown="if(event.key==='Enter')location.hash='apropos'"><circle cx="130" cy="79" r="22"/><text class="ic" x="130" y="84">◉</text><text x="130" y="48">Noyau</text></g>
    <g class="n" tabindex="0" onclick="location.hash='contact'" onkeydown="if(event.key==='Enter')location.hash='contact'"><circle cx="270" cy="79" r="22"/><text class="ic" x="270" y="84">✉</text><text x="270" y="48">Contact</text></g>
  </svg>
  <p class="hint">Touchez un nœud pour l’activer</p>
</div>

<div class="view" id="services" hidden>
  <span class="tag">&gt; MODULE_01</span>
  <h2><span class="g">Services</span></h2>
  <p class="sub">Des solutions de pointe, conçues pour accélérer votre activité.</p>
  <div class="grid">
    <div class="card"><div class="num">01</div><h3>Conseil &amp; stratégie</h3><p>Analyse de vos besoins et feuille de route claire pour atteindre vos objectifs.</p></div>
    <div class="card"><div class="num">02</div><h3>Accompagnement</h3><p>Un suivi personnalisé et réactif, à chaque étape de votre projet.</p></div>
    <div class="card"><div class="num">03</div><h3>Développement</h3><p>Des solutions modernes et sécurisées pour faire grandir votre activité.</p></div>
  </div>
  <a class="back" href="#accueil">← Retour au noyau</a>
</div>

<div class="view" id="apropos" hidden>
  <span class="tag">&gt; MODULE_02</span>
  <h2><span class="g">Le Noyau</span></h2>
  <p class="sub">Al Amir, « le prince » en arabe, incarne notre promesse : un service d’exception fondé sur la confiance, la qualité et le respect de vos engagements.</p>
  <div class="stats">
    <div><b class="g">10+</b><span>ans d’expérience</span></div>
    <div><b class="g">200+</b><span>clients satisfaits</span></div>
    <div><b class="g">100%</b><span>engagement</span></div>
  </div>
  <a class="back" href="#accueil">← Retour au noyau</a>
</div>

<div class="view" id="equipe" hidden>
  <span class="tag">&gt; MODULE_03</span>
  <h2><span class="g">L’Équipe</span></h2>
  <p class="sub">Les esprits qui font vivre le système.</p>
  <div class="grid">
    <div class="card"><div class="ava">A</div><h3>Le Directeur</h3><p>Vision, stratégie et sens du détail depuis plus de dix ans.</p></div>
    <div class="card"><div class="ava">R</div><h3>La Responsable clientèle</h3><p>Votre interlocutrice privilégiée, toujours à l’écoute.</p></div>
    <div class="card"><div class="ava">E</div><h3>L’Expert technique</h3><p>Il transforme vos idées en solutions solides et élégantes.</p></div>
  </div>
  <a class="back" href="#accueil">← Retour au noyau</a>
</div>

<div class="view" id="tarifs" hidden>
  <span class="tag">&gt; MODULE_04</span>
  <h2><span class="g">Tarifs</span></h2>
  <p class="sub">Des formules claires, adaptées à chaque ambition.</p>
  <div class="grid">
    <div class="card"><div class="num">ESSENTIEL</div><h3>Sur devis</h3><p>Conseil initial et plan d’action personnalisé.</p></div>
    <div class="card hl"><div class="num">PREMIUM</div><h3>Sur devis</h3><p>Conseil, accompagnement complet et suivi régulier.</p></div>
    <div class="card"><div class="num">QUANTUM</div><h3>Sur devis</h3><p>Prise en charge totale, de la stratégie à la réalisation.</p></div>
  </div>
  <div class="center" style="margin-top:28px"><a class="btn" href="#contact">Demander un devis</a></div>
  <a class="back" href="#accueil">← Retour au noyau</a>
</div>

<div class="view" id="galerie" hidden>
  <span class="tag">&gt; MODULE_05</span>
  <h2><span class="g">Galerie</span></h2>
  <p class="sub">Un aperçu de nos plus belles réalisations.</p>
  <div class="grid">
    <div class="tile">Projet 01</div><div class="tile">Projet 02</div><div class="tile">Projet 03</div>
    <div class="tile">Projet 04</div><div class="tile">Projet 05</div><div class="tile">Projet 06</div>
  </div>
  <a class="back" href="#accueil">← Retour au noyau</a>
</div>

<div class="view center" id="contact" hidden>
  <span class="tag">&gt; MODULE_06</span>
  <h2><span class="g">Contact</span></h2>
  <p class="sub">Envoyez-nous votre message : nous répondons sous 24 h.</p>
  <a class="btn" href="mailto:contact@alamir.com">contact@alamir.com</a>
  <a class="back" href="#accueil">← Retour au noyau</a>
</div>
</main>

<footer>© 2026 Al Amir Quantum. Tous droits réservés.</footer>

<script>
(function(){
  var ids=['services','apropos','contact','equipe','tarifs','galerie'];
  function show(){
    var h=location.hash.slice(1);
    var id=ids.indexOf(h)>-1?h:'accueil';
    document.querySelectorAll('.view').forEach(function(v){v.hidden=(v.id!==id)});
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',show);
  show();
})();
(function(){
  var c=document.getElementById('bg'),x=c.getContext('2d'),P=[],W,H,m={x:-999,y:-999};
  var still=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  function size(){W=c.width=innerWidth;H=c.height=innerHeight;
    var n=Math.min(90,Math.floor(W*H/14000));P=[];
    for(var i=0;i<n;i++)P.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5,h:Math.random()<.5?185:265});}
  addEventListener('resize',size);
  addEventListener('pointermove',function(e){m.x=e.clientX;m.y=e.clientY});
  function draw(){
    x.clearRect(0,0,W,H);
    for(var i=0;i<P.length;i++){
      var p=P[i];
      if(!still){p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1}
      for(var j=i+1;j<P.length;j++){
        var q=P[j],d=Math.hypot(p.x-q.x,p.y-q.y);
        if(d<130){x.strokeStyle='hsla('+p.h+',100%,60%,'+(.35*(1-d/130))+')';x.lineWidth=1;x.beginPath();x.moveTo(p.x,p.y);x.lineTo(q.x,q.y);x.stroke()}
      }
      var dm=Math.hypot(p.x-m.x,p.y-m.y);
      if(dm<160){x.strokeStyle='rgba(255,61,242,'+(.5*(1-dm/160))+')';x.beginPath();x.moveTo(p.x,p.y);x.lineTo(m.x,m.y);x.stroke()}
      x.fillStyle='hsl('+p.h+',100%,70%)';x.shadowColor='hsl('+p.h+',100%,60%)';x.shadowBlur=8;
      x.beginPath();x.arc(p.x,p.y,1.8,0,6.283);x.fill();x.shadowBlur=0;
    }
    if(!still)requestAnimationFrame(draw);
  }
  size();draw();
})();
</script>
</body>
</html>
"""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        data = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as server:
        url = f"http://localhost:{PORT}"
        print(f"Al Amir Quantum : {url}  (Ctrl+C pour arrêter)")
        
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Arrêt.")
