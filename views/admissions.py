import streamlit as st
from components.ui import load, banner, footer, wa_link
from components.forms import enquiry_form
s = load("school")
banner("Admissions", "Now admitting for the 2026/2027 school year")
st.write("We are admitting children into **Nursery**, **Primary** and **College**.")
st.header("How to Apply")
for i, (col, (t, d)) in enumerate(zip(st.columns(3), [
    ("Get in touch", f"Call {s['phone']}, message us on WhatsApp, or send the enquiry form below."),
    ("Visit the school", f"Visit us at {s['address']}. Visiting hours: {s['hours_visit']}."),
    ("Ask about requirements", "Entry requirements, required documents and fees are explained by the school on enquiry.")])):
    col.markdown(f'<div class="card"><span class="num">0{i+1}</span><b>{t}</b><br><small>{d}</small></div>', unsafe_allow_html=True)
st.link_button("Enquire on WhatsApp", wa_link(s))
st.header("Frequently Asked Questions")
with st.expander("Which levels are open for admission?"): st.write("Nursery, Primary and College, for the 2026/2027 school year.")
with st.expander("How can I enquire or visit?"): st.write(f"Call {s['phone']} or visit us at {s['address']}. Visiting hours: {s['hours_visit']}. Calls: {s['hours_call']}.")
st.header("Admission Enquiry")
enquiry_form("admission", admission=True)
footer()
