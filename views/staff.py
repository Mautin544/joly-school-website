import streamlit as st
from components.ui import load, banner, footer, ROOT
s, sd = load("school"), load("staff")
d = s["director"]
banner("Management & Staff", "Led by our Founder and Director")
a, b = st.columns([1, 2], gap="large")
a.image(str(ROOT / "assets/director/director_full.jpg"), caption=f'{d["name"]}, {d["title"]}')
with b:
    st.header(d["name"]); st.caption(f'{d["title"]} · {d["qualification"]}')
    for para in d["bio"]: st.markdown(para)
st.header("Director's Welcome")
for para in d["welcome"]: st.markdown(para)
st.markdown(f"**{d['name']}**  \n{d['title']}")
for k in ("teaching", "support"):
    sec = sd[k]
    st.header(sec["title"])
    if sec["show_section"] and sec["people"]:
        cols = st.columns(3)
        for i, p in enumerate(sec["people"]):
            with cols[i % 3]:
                if p.get("photo"): st.image(str(ROOT / p["photo"]), caption=p["name"])
                st.markdown(f'**{p["name"]}**  \n{p["designation"]}')
                if p.get("qualifications"): st.caption(p["qualifications"])
                if p.get("bio"): st.write(p["bio"])
    else:
        st.write(sec["note"])
footer()
