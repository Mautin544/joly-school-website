import streamlit as st
from components.ui import load, banner, footer
banner("News & Events", "Announcements from the school")
q = st.text_input("Search announcements", placeholder="Type a word, e.g. admission").lower()
items = [i for i in load("announcements") if q in (i["title"] + i["body"]).lower()]
for i in items:
    st.markdown(f'<div class="card"><span class="pill" style="background:#2E3192">{i["category"]}</span> <small>{i["date"]}</small><br><b>{i["title"]}</b><p>{i["body"]}</p></div><br>', unsafe_allow_html=True)
if not items: st.info("No announcements match your search.")
footer()
