import streamlit as st, streamlit.components.v1 as comp
from components.ui import load, banner, footer, wa_link
from components.forms import enquiry_form
s = load("school")
banner("Contact Us", "We would love to hear from you")
a, b = st.columns(2, gap="large")
with a:
    st.markdown(f"**Address**  \n{s['address']}\n\n**Phone**  \n[{s['phone']}](tel:{s['phone']})\n\n**Email**  \n[{s['email']}](mailto:{s['email']})\n\n**Visiting hours**  \n{s['hours_visit']}\n\n**Call us**  \n{s['hours_call']}")
    st.link_button("Chat on WhatsApp", wa_link(s))
    st.link_button("Get directions", s["map_url"])
with b:
    comp.html(f'<iframe title="Map showing the location of {s["name"]}" src="https://maps.google.com/maps?q={s["lat"]},{s["lng"]}&z=17&output=embed" width="100%" height="300" style="border:0;border-radius:14px" loading="lazy"></iframe>', height=310)
st.header("Send us a message")
enquiry_form("contact")
footer()
