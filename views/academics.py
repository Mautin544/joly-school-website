import streamlit as st
from components.ui import load, banner, footer, placeholder, LOGO
p = load("programmes")
banner("Academics", "From Nursery through College")
for l in p["levels"]:
    a, b = st.columns([1, 4], vertical_alignment="center")
    a.image(str(LOGO / l["logo"]), width=110)
    b.subheader(l["name"]); b.write(l["tagline"])
    if l["subjects"]: b.write(", ".join(l["subjects"]))
    else: b.caption("Subjects offered: to be provided by the school.")
for key, label in [("curriculum", "Curriculum"), ("methodology", "Teaching and learning"), ("calendar", "Academic calendar")]:
    st.header(label)
    if p[key]: st.write(p[key])
    else: placeholder(f"{label} information will be added soon.")
footer()
