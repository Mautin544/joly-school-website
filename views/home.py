import streamlit as st
from components.ui import load, LOGO, ROOT, footer, img_b64, wa_link
from components import events as ev
s, p, fac = load("school"), load("programmes"), load("facilities")
d = s["director"]
bg = img_b64(ROOT / "assets/facilities/front_view.jpg", 1200)
logo = img_b64(LOGO / "logo_nursery_primary.png", 320)
st.markdown(f"""<div class="hero2" style="--bg:url({bg})"><div><span class="eyebrow">Admissions open · 2026/2027</span>
<h1>{s['name']}</h1><p><i>{s['motto']}.</i></p>
<p>A vibrant school in Ota, Ogun State, building strong foundations in knowledge, character and values for children from Nursery to College.</p></div>
<img class="logo" src="{logo}" alt="Joly Nursery and Primary School crest"></div>""", unsafe_allow_html=True)
c = st.columns(3)
c[0].page_link("views/admissions.py", label="Apply for Admission")
c[1].page_link("views/about.py", label="About Our School")
c[2].page_link("views/contact.py", label="Contact Us")
st.markdown(f"""<div class="stats"><div class="stat"><b>{s['founded']}</b><span>Established</span></div><div class="stat"><b>3 Levels</b><span>Nursery · Primary · College</span></div><div class="stat"><b>Mon–Fri</b><span>Visits 10am–3pm</span></div><div class="stat"><b>Ota</b><span>Ogun State</span></div></div>""", unsafe_allow_html=True)

st.header("Our Levels")
for i, (col, l) in enumerate(zip(st.columns(3), p["levels"])):
    col.markdown(f'<div class="card top rv" style="--c:{l["colour"]};--d:{i*.1}s"><span class="pill" style="background:{l["colour"]}">{l["name"].upper()}</span><p>{l["tagline"]}</p></div>', unsafe_allow_html=True)

st.header("Our Campus")
for col, x in zip(st.columns(3), [x for x in fac if x["category"] == "Campus"][:3]):
    col.image(str(ROOT / x["file"]), caption=x["caption"])
st.page_link("views/facilities.py", label="View more of our school")

st.header("Why Choose Us")
for i, (col, (t, desc)) in enumerate(zip(st.columns(5), s["why"])):
    col.markdown(f'<div class="card rv" style="--d:{i*.08}s"><span class="num">0{i+1}</span><b>{t}</b><br><small>{desc}</small></div>', unsafe_allow_html=True)

st.header("A Word from the Director")
x, y = st.columns([1, 2.4], vertical_alignment="center", gap="large")
x.image(str(ROOT / "assets/director/director_portrait.jpg"), caption=f'{d["name"]}, {d["title"]}')
y.markdown("### “Education is the greatest treasure.”")
y.markdown(d["short"])
y.page_link("views/staff.py", label="Read the full message")

ev.style()
up = ev.upcoming()[:3]
if up:
    st.header("Upcoming Events")
    st.markdown("".join(ev.event_card(e) for e in up), unsafe_allow_html=True)
    st.page_link("views/news.py", label="See the full calendar")
st.header("Latest Announcements")
st.markdown("".join(ev.announcement_card(e) for e in ev.items()[:3]), unsafe_allow_html=True)

st.markdown(f"""<div class="cta"><h2>Enrol your child today</h2><p>Admissions are open for the 2026/2027 school year.</p>
<a href="tel:{s['phone']}">Call {s['phone']}</a><a class="wa" href="{wa_link(s)}" target="_blank">WhatsApp us</a></div>""", unsafe_allow_html=True)
footer()
