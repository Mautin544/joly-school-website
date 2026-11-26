import streamlit as st
from components.ui import load, banner, footer, LOGO
p = load("programmes")
banner("Academics", "From Nursery through College")
for l in p["levels"]:
    a, b = st.columns([1, 4], vertical_alignment="center")
    a.image(str(LOGO / l["logo"]), width=110)
    b.subheader(l["name"]); b.write(l["tagline"])
    if l["subjects"]: b.write("Subjects: " + ", ".join(l["subjects"]))
for key, label in [("curriculum", "Curriculum"), ("methodology", "Teaching and Learning"), ("calendar", "Academic Calendar")]:
    if p[key]:
        st.header(label); st.write(p[key])
st.info("For details of the curriculum and subjects at each level, please contact the school or visit us during visiting hours.")
footer()
