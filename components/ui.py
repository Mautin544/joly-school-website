import json, base64, io, pathlib, streamlit as st
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "logo"

@st.cache_data
def load(name):
    return json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))

@st.cache_data
def img_b64(path, width=1400):
    p = pathlib.Path(path)
    im = Image.open(p); im.thumbnail((width, width))
    buf, png = io.BytesIO(), p.suffix.lower() == ".png"
    (im if png else im.convert("RGB")).save(buf, "PNG" if png else "JPEG", quality=70)
    return f"data:image/{'png' if png else 'jpeg'};base64," + base64.b64encode(buf.getvalue()).decode()

def wa_link(s):
    from urllib.parse import quote
    return f"https://wa.me/{s['whatsapp']}?text=" + quote("Hello, I would like to enquire about admission at Joly Nursery, Primary and College.")

def css():
    st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@400;500;600&display=swap');
:root{--royal:#2E3192;--deep:#161a5c;--sky:#00AEEF;--ink:#1c2340;--muted:#5a6690;--line:#e4e9f4;--soft:#f6f8fc;color-scheme:light only}
html,body,[class*="css"]{font-family:'Poppins',sans-serif;color:var(--ink)}
h1,h2,h3{font-family:'Playfair Display',serif!important;color:var(--royal);letter-spacing:-.01em}
.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background-color:#fff!important}
.stApp :is(p,li,label,span,small,h4,h5,h6){color:var(--ink)}
.block-container{max-width:1080px;padding-top:5rem;padding-bottom:3rem}
.block-container h2{margin-top:3rem;font-size:1.8rem}
.block-container h2::after{content:"";display:block;width:44px;height:3px;margin-top:.4rem;background:var(--sky)}
@keyframes up{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.rv{opacity:0;animation:up .5s ease forwards;animation-delay:var(--d,0s)}
header[data-testid="stHeader"]{background:#fff!important;border-bottom:1px solid var(--line);box-shadow:0 1px 8px rgba(22,26,92,.06)}
header[data-testid="stHeader"] a{border-radius:8px!important;padding:.4rem .9rem!important;font-weight:500;color:var(--ink)!important;transition:background .2s,color .2s}
header[data-testid="stHeader"] a:hover{background:var(--soft)!important;color:var(--royal)!important}
header[data-testid="stHeader"] a[aria-current="page"],header[data-testid="stHeader"] a[aria-selected="true"],header[data-testid="stHeader"] a[data-active="true"]{background:#eaeefb!important;color:var(--royal)!important;font-weight:600}
header[data-testid="stHeader"] a[aria-current="page"] *,header[data-testid="stHeader"] a[aria-selected="true"] *,header[data-testid="stHeader"] a[data-active="true"] *{color:var(--royal)!important}
.topbar{background:var(--deep);border-radius:0 0 10px 10px;padding:.4rem 1rem;margin:0 0 1.2rem;text-align:center;font-size:.78rem;letter-spacing:.02em}
.topbar,.topbar *{color:#fff!important}.topbar a{font-weight:600;text-decoration:none}
.pagehead{background:linear-gradient(110deg,var(--deep),var(--royal));border-radius:14px;padding:2.2rem 2rem;margin-bottom:1rem;border-bottom:4px solid var(--sky);animation:up .5s ease both}
.pagehead h1{color:#fff!important;font-size:2.2rem;margin:0}.pagehead p{color:#dbe3ff!important;margin:.4rem 0 0;font-size:1rem}
.hero2{border-radius:16px;padding:3.4rem 2.4rem;margin-bottom:1.2rem;display:grid;grid-template-columns:1.8fr 1fr;gap:2rem;align-items:center;background:linear-gradient(100deg,rgba(15,20,80,.94),rgba(22,26,92,.78)),var(--bg) center/cover;animation:up .6s ease both}
.hero2 h1{color:#fff!important;font-size:2.7rem;line-height:1.15;margin:.5rem 0 .6rem}
.hero2 p{color:#e3e9ff!important;font-size:1.05rem;margin:.3rem 0}
.hero2 .eyebrow{display:inline-block;color:#fff!important;border-bottom:2px solid var(--sky);padding-bottom:.2rem;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase}
.hero2 .logo{width:100%;max-width:210px;margin:auto;display:block;background:#fff;border-radius:16px;padding:14px;box-shadow:0 10px 30px rgba(0,0,0,.3)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line);border-radius:12px;margin:1.2rem 0;background:#fff}
.stat{padding:1rem;text-align:center;border-right:1px solid var(--line)}.stat:last-child{border:0}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:1.3rem;color:var(--royal)!important}.stat span{font-size:.78rem;color:var(--muted)!important}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:1.3rem;height:100%;transition:transform .25s,box-shadow .25s}
.card:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(22,26,92,.1)}
.card.top{border-top:3px solid var(--c,var(--royal))}
.card,.card :is(p,b,small,span,div,li,br){color:var(--ink)!important}
.card :is(h1,h2,h3){color:var(--royal)!important}
.card .num{font-family:'Playfair Display',serif;font-size:1.6rem;color:var(--sky)!important;display:block}
.card .pill{color:#fff!important}
.pill{display:inline-block;color:#fff;padding:.12rem .7rem;border-radius:6px;font-weight:600;font-size:.78rem;letter-spacing:.03em;margin-bottom:.5rem}
.ph,.ph *{color:#3d4d80!important}.ph{background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:1.5rem;text-align:center}
[data-testid="stImage"] img{border-radius:10px;transition:transform .4s}
[data-testid="stImage"]:hover img{transform:scale(1.02)}
[data-testid="stCaptionContainer"],[data-testid="stCaptionContainer"] *{color:var(--muted)!important}
.block-container [data-testid="stPageLink"] a{background:var(--royal);border-radius:8px;justify-content:center;padding:.65rem 1rem;transition:background .2s}
.block-container [data-testid="stPageLink"] a:hover{background:var(--deep)}
.block-container [data-testid="stPageLink"] a *{color:#fff!important}
.stButton p,.stFormSubmitButton p{color:#fff!important}
.stButton>button,.stFormSubmitButton>button{background:var(--royal);border-radius:8px;border:0;padding:.55rem 1.6rem}
.stButton>button:hover,.stFormSubmitButton>button:hover{background:var(--deep)}
.stApp input,.stApp textarea,.stApp [data-baseweb="select"]>div,.stApp [data-baseweb="input"],.stApp [data-baseweb="base-input"]{background-color:#fff!important;color:var(--ink)!important;border-color:#c9d6f0!important}
[data-testid="stExpander"] details{background:#fff;border-color:var(--line)}
.cta{background:linear-gradient(110deg,var(--deep),var(--royal));border-radius:14px;padding:2.2rem;text-align:center;margin-top:3rem}
.cta h2,.cta p{color:#fff!important}.cta h2::after{display:none}.cta h2{margin-top:0!important}
.cta a{display:inline-block;background:#fff;color:var(--royal)!important;text-decoration:none;font-weight:600;border-radius:8px;padding:.65rem 1.6rem;margin:.4rem}
.cta a.wa{background:transparent;border:2px solid #fff;color:#fff!important;padding:.55rem 1.5rem}
.foot{background:var(--deep);border-radius:14px;padding:2rem;margin-top:2.5rem;font-size:.9rem}
.foot,.foot :is(p,span,div,i){color:#cfd8ff!important}.foot b{color:#fff!important}.foot a{color:#8fd8ff!important}
.foot .fg{display:grid;grid-template-columns:1.4fr 1.4fr 1fr;gap:2rem}.foot .fg p{margin:.3rem 0}
.foot .copy{border-top:1px solid rgba(255,255,255,.18);margin-top:1.4rem;padding-top:1rem;font-size:.8rem}
.wa-fab{position:fixed;right:16px;bottom:16px;z-index:999;background:#1fa855;border-radius:99px;padding:.6rem 1.1rem;font-size:.85rem;font-weight:600;text-decoration:none!important;box-shadow:0 6px 16px rgba(0,0,0,.25)}
.wa-fab,.wa-fab:hover{color:#fff!important}
@media(max-width:760px){.hero2{grid-template-columns:1fr;padding:2rem 1.3rem}.hero2 h1{font-size:1.9rem}.hero2 .logo{max-width:130px}.stats{grid-template-columns:repeat(2,1fr)}.stat:nth-child(2){border-right:0}.stat:nth-child(-n+2){border-bottom:1px solid var(--line)}.foot .fg{grid-template-columns:1fr}.pagehead h1{font-size:1.7rem}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;opacity:1!important}}
</style>""", unsafe_allow_html=True)

def topbar():
    s = load("school")
    st.markdown(f'<div class="topbar">Admissions open for 2026/2027 &nbsp;|&nbsp; Call <a href="tel:{s["phone"]}">{s["phone"]}</a> &nbsp;|&nbsp; {s["hours_call"].replace("Monday to Friday","Mon–Fri")}</div>', unsafe_allow_html=True)

def banner(title, sub=""):
    st.markdown(f'<div class="pagehead"><h1>{title}</h1><p>{sub}</p></div>', unsafe_allow_html=True)

def placeholder(text):
    st.markdown(f'<div class="ph">{text}</div>', unsafe_allow_html=True)

def footer():
    s = load("school")
    soc = "".join(f'<a href="{u}">{n}</a> ' for n, u in s["socials"].items())
    st.markdown(f'<div class="foot"><div class="fg"><div><b>{s["name"]}</b><p><i>{s["motto"]}.</i></p><p>Established {s["founded"]}</p>{soc}</div><div><b>Contact</b><p>{s["address"]}<br><a href="{s["map_url"]}" target="_blank">Get directions</a></p><p>Phone: <a href="tel:{s["phone"]}">{s["phone"]}</a><br>WhatsApp: <a href="{wa_link(s)}" target="_blank">{s["whatsapp_display"]}</a><br>Email: <a href="mailto:{s["email"]}">{s["email"]}</a></p></div><div><b>Hours</b><p>Visits:<br>{s["hours_visit"]}</p><p>Calls:<br>{s["hours_call"]}</p></div></div><div class="copy">© 2026 {s["name"]}. All rights reserved.</div></div><a class="wa-fab" href="{wa_link(s)}" target="_blank" aria-label="Chat with us on WhatsApp">WhatsApp</a>', unsafe_allow_html=True)
