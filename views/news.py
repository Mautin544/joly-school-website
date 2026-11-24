import streamlit as st
from components.ui import banner, footer
from components import events as ev
banner("News & Events", "Announcements and upcoming dates")
ev.style()
st.header("Upcoming Events")
up = ev.upcoming()
a, b = st.columns([1.4, 1], gap="large")
if up:
    a.markdown("".join(ev.event_card(x) for x in up), unsafe_allow_html=True)
else:
    a.info("No upcoming events have been announced yet. Please check back soon.")
b.markdown(ev.calendar_html(up), unsafe_allow_html=True)
st.header("Announcements")
q = st.text_input("Search announcements", placeholder="Type a word, e.g. admission").lower()
found = [x for x in ev.items() if q in (str(x.get("title")) + str(x.get("body")) + str(x.get("category"))).lower()]
st.markdown("".join(ev.announcement_card(x) for x in found), unsafe_allow_html=True)
if not found: st.info("No announcements match your search.")
footer()
