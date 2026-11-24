import json, base64, io, pathlib, streamlit as st
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "logo"

@st.cache_data
def load(name):
    return json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))

@st.cache_data
def img_b64(path, width=1400):
    """Resized base64 data-URI, so images can sit inside custom HTML/CSS."""
    p = pathlib.Path(path)
    im = Image.open(p); im.thumbnail((width, width))
    buf, png = io.BytesIO(), p.suffix.lower() == ".png"
    (im if png else im.convert("RGB")).save(buf, "PNG" if png else "JPEG", quality=82)
    return f"data:image/{'png' if png else 'jpeg'};base64," + base64.b64encode(buf.getvalue()).decode()

def css():
    st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@400;500;600&display=swap');
:root{--royal:#2E3192;--deep:#1b1f6b;--sky:#00AEEF;--red:#D7263D;--gold:#F5A623;--ink:#1c2340;--soft:#f3f8ff}
html,body,[class*="css"]{font-family:'Poppins',sans-serif;color:var(--ink)}
h1,h2,h3{font-family:'Playfair Display',serif!important;color:#4a52c8}
.block-container{max-width:1100px;padding-top:5rem}
.block-container h2{margin-top:2.2rem}
.block-container h2::after{content:"";display:block;width:56px;height:4px;border-radius:4px;margin-top:.35rem;background:linear-gradient(90deg,var(--sky),var(--royal))}
@keyframes up{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes drift{0%{background-position:0% 50%}100%{background-position:100% 50%}}
@keyframes bubble{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(18px,-22px) scale(1.08)}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(215,38,61,.55)}100%{box-shadow:0 0 0 14px rgba(215,38,61,0)}}
.rv{opacity:0;animation:up .7s ease forwards;animation-delay:var(--d,0s)}
.hero,.hero2{position:relative;overflow:hidden;color:#fff;border-radius:26px;margin-bottom:1.5rem;animation:up .7s ease both}
.hero{background:linear-gradient(120deg,#2E3192,#1b1f6b,#00AEEF,#2E3192);background-size:300% 300%;animation:up .7s ease both,drift 14s linear infinite alternate;padding:2.4rem 2.2rem}
.hero h1{color:#fff;font-size:2.4rem;margin:.4rem 0}.hero p{color:#e6efff;font-size:1.05rem;margin:0}
.hero2{background:linear-gradient(120deg,rgba(27,31,107,.95),rgba(46,49,146,.85) 55%,rgba(0,174,239,.5)),var(--bg) center/cover;padding:3.2rem 2.4rem;display:grid;grid-template-columns:1.7fr 1fr;gap:1.5rem;align-items:center}
.hero2 h1{color:#fff;font-size:2.8rem;line-height:1.15;margin:.6rem 0}.hero2 p{color:#e6efff;font-size:1.08rem;margin:.3rem 0}
.hero::before,.hero2::before,.hero2::after{content:"";position:absolute;border-radius:50%;background:rgba(255,255,255,.08);animation:bubble 9s ease-in-out infinite;pointer-events:none}
.hero::before,.hero2::before{width:220px;height:220px;right:-60px;top:-70px}
.hero2::after{width:140px;height:140px;left:38%;bottom:-50px;animation-delay:3s}
.hero2 .logo{width:100%;max-width:230px;margin:auto;display:block;background:#fff;border-radius:24px;padding:16px;box-shadow:0 18px 40px rgba(0,0,0,.35);animation:floaty 5s ease-in-out infinite}
.badge{display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);padding:.28rem .9rem;border-radius:99px;font-size:.8rem}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin:1.2rem 0}
.stat{background:#fff;border:1px solid #e3ebf8;border-radius:16px;padding:.9rem;text-align:center;box-shadow:0 4px 14px rgba(46,49,146,.07)}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:1.35rem;color:var(--royal)}.stat span{font-size:.8rem;color:#5a6690}
.card{background:#fff;border:1px solid #e3ebf8;border-radius:18px;padding:1.2rem;box-shadow:0 4px 14px rgba(46,49,146,.08);height:100%;transition:transform .25s,box-shadow .25s;position:relative;overflow:hidden}
.card:hover{transform:translateY(-6px);box-shadow:0 14px 28px rgba(46,49,146,.18)}
.card.top{border-top:5px solid var(--c,var(--royal))}
.card .ic{font-size:2rem;display:block;margin-bottom:.3rem;transition:transform .3s}.card:hover .ic{transform:scale(1.2) rotate(-6deg)}
.pill{display:inline-block;color:#fff;padding:.15rem .8rem;border-radius:99px;font-weight:600;font-size:.85rem;margin-bottom:.5rem}
.ph{background:var(--soft);border:2px dashed #9db8e8;border-radius:14px;padding:2rem;text-align:center;color:#4a5a8a}
[data-testid="stImage"] img{border-radius:16px;transition:transform .4s,box-shadow .4s}
[data-testid="stImage"]:hover img{transform:scale(1.03);box-shadow:0 12px 26px rgba(46,49,146,.22)}
.block-container [data-testid="stPageLink"] a{background:var(--royal);border-radius:99px;justify-content:center;padding:.6rem 1rem;transition:transform .2s,background .2s}
.block-container [data-testid="stPageLink"] a:hover{background:var(--sky);transform:translateY(-3px)}
.block-container [data-testid="stPageLink"] a *{color:#fff!important}
.cta{background:linear-gradient(120deg,var(--deep),var(--royal));color:#fff;border-radius:22px;padding:2rem;text-align:center;margin-top:2.2rem}
.cta h2{color:#fff!important}.cta h2::after{display:none}
.cta a{display:inline-block;background:var(--red);color:#fff!important;text-decoration:none;font-weight:600;border-radius:99px;padding:.7rem 1.8rem;margin:.4rem;animation:pulse 2s infinite}
.cta a.alt{background:#fff;color:var(--royal)!important;animation:none}
.foot{background:linear-gradient(135deg,var(--deep),var(--royal));color:#dbe6ff;border-radius:20px;padding:1.6rem;margin-top:2rem;font-size:.92rem}
.foot a{color:#8fd8ff}.foot b{color:#fff}
.stButton>button,.stFormSubmitButton>button{background:var(--royal);color:#fff;border-radius:99px;border:0;padding:.5rem 1.4rem;transition:transform .2s,background .2s}
.stButton>button:hover,.stFormSubmitButton>button:hover{background:var(--sky);color:#fff;transform:translateY(-2px)}
/* readable in light AND dark mode: custom panels carry their own colours */
.hero h1,.hero2 h1,.cta h2{color:#fff!important}
.hero p,.hero2 p,.cta p,.badge{color:#fff!important}
.card,.card :is(p,b,small,span,div,li,br){color:var(--ink)!important}
.card :is(h1,h2,h3){color:var(--royal)!important}
.card .pill{color:#fff!important}
.stat,.stat span{color:#5a6690!important}.stat b{color:var(--royal)!important}
.ph,.ph *{color:#3d4d80!important}
.foot,.foot :is(p,span,div,i){color:#dbe6ff!important}.foot b{color:#fff!important}.foot a{color:#8fd8ff!important}
.cta a{color:#fff!important}.cta a.alt{color:var(--royal)!important}
.topbar,.topbar *{color:#fff!important}
/* top navigation */
@keyframes shine{0%{background-position:-200% 0}100%{background-position:200% 0}}
header[data-testid="stHeader"]{background:rgba(255,255,255,.88)!important;backdrop-filter:blur(12px);border-bottom:3px solid transparent;border-image:linear-gradient(90deg,var(--royal),var(--sky),var(--gold),var(--red)) 1;box-shadow:0 6px 20px rgba(46,49,146,.12)}
header[data-testid="stHeader"] a{position:relative;border-radius:99px!important;padding:.45rem 1rem!important;font-weight:500;color:var(--ink)!important;transition:background .25s,color .25s,transform .25s,box-shadow .25s}
header[data-testid="stHeader"] a:hover{background:#eaf1ff!important;color:var(--royal)!important;transform:translateY(-2px);box-shadow:0 6px 14px rgba(46,49,146,.15)}
header[data-testid="stHeader"] a[aria-current="page"],header[data-testid="stHeader"] a[aria-selected="true"],header[data-testid="stHeader"] a[data-active="true"]{background:linear-gradient(120deg,var(--royal),var(--sky))!important;color:#fff!important;font-weight:600;box-shadow:0 6px 16px rgba(46,49,146,.35)}
header[data-testid="stHeader"] a[aria-current="page"] *,header[data-testid="stHeader"] a[aria-selected="true"] *,header[data-testid="stHeader"] a[data-active="true"] *{color:#fff!important}
.topbar{background:linear-gradient(100deg,var(--deep),var(--royal),var(--sky),var(--royal),var(--deep));background-size:300% 100%;animation:shine 12s linear infinite;color:#fff;border-radius:0 0 16px 16px;padding:.45rem 1rem;margin:0 0 1.2rem;text-align:center;font-size:.82rem}
.topbar a{color:#fff!important;font-weight:600;text-decoration:none}
@media(max-width:760px){.hero2{grid-template-columns:1fr;padding:1.8rem 1.3rem}.hero2 h1{font-size:1.9rem}.hero2 .logo{max-width:150px}.hero h1{font-size:1.7rem}.stats{grid-template-columns:repeat(2,1fr)}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;opacity:1!important}}
</style>""", unsafe_allow_html=True)

def topbar():
    s = load("school")
    st.markdown(f'<div class="topbar">✨ Admissions open for 2026/2027 · 📞 <a href="tel:{s["phone"]}">{s["phone"]}</a> · Calls {s["hours_call"].replace("Monday to Friday","Mon–Fri")}</div>', unsafe_allow_html=True)

def banner(title, sub=""):
    s = load("school")
    st.markdown(f'<div class="hero"><span class="badge">{s["name"]}</span><h1>{title}</h1><p>{sub}</p></div>', unsafe_allow_html=True)

def placeholder(text):
    st.markdown(f'<div class="ph">{text}</div>', unsafe_allow_html=True)

def footer():
    s = load("school")
    soc = " · ".join(f'<a href="{u}">{n}</a>' for n, u in s["socials"].items())
    st.markdown(f"""<div class="foot"><b>{s['name']}</b><br><i>{s['motto']}</i> · Established {s['founded']}<br><br>
📍 {s['address']} · <a href="{s['map_url']}" target="_blank">Get directions</a><br>
📞 <a href="tel:{s['phone']}">{s['phone']}</a> · ✉️ <a href="mailto:{s['email']}">{s['email']}</a><br>
🕙 Visits: {s['hours_visit']}<br>📞 Calls: {s['hours_call']}{('<br>'+soc) if soc else ''}<br><br>© 2026 {s['name']}</div>""", unsafe_allow_html=True)
