import streamlit as st
from components.ui import load, banner, footer
s = load("school")
banner("About Our School", s["motto"])
st.header("Our Story")
st.write(f"{s['name']} was founded on {s['founded_full']} by {s['director']['name']}, with the belief that education is the greatest treasure. We are a vibrant school, building with care and purpose.")
a, b = st.columns(2)
a.markdown(f'<div class="card"><h3>Vision</h3>{s["vision"]}</div>', unsafe_allow_html=True)
b.markdown(f'<div class="card"><h3>Mission</h3>{s["mission"]}</div>', unsafe_allow_html=True)
st.header("Core Values")
cols = st.columns(3)
for i, (t, d) in enumerate(s["values"]):
    cols[i % 3].markdown(f'<div class="card"><b>{t}</b><br>{d}</div><br>', unsafe_allow_html=True)
st.header("Educational Objectives")
for o in s["objectives"]: st.markdown(f"- {o}")
st.header("Leadership")
st.write(f"The school is led directly by its Founder and Director, {s['director']['name']}.")
st.page_link("views/staff.py", label="Meet the Director")
footer()
