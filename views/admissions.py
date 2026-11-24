import streamlit as st
from components.ui import load, banner, footer, placeholder
from components.forms import enquiry_form
s = load("school")
banner("Admissions", "Now admitting for the 2026/2027 school year")
st.write("We are admitting children into **Nursery**, **Primary** and **College**. To enquire, call, visit the school, or use the form below.")
st.header("Entry requirements, documents and timelines")
placeholder("Entry requirements, required documents, application procedure and dates will be published once confirmed by the school. Please call 08038471964 in the meantime.")
st.header("Frequently Asked Questions")
with st.expander("Which levels are open for admission?"): st.write("Nursery, Primary and College, for the 2026/2027 school year.")
with st.expander("How can I enquire or visit?"): st.write(f"Call {s['phone']} or visit us at {s['address']}. Visiting hours: {s['hours_visit']}. Calls: {s['hours_call']}.")
st.header("Admission Enquiry")
enquiry_form("admission", admission=True)
footer()
