import streamlit as st
from components.ui import load, banner, footer, ROOT
banner("Our Facilities", "A look at our school and classrooms")
items = load("facilities")
for cat, title in [("Campus", "School Premises"), ("Classrooms", "Classrooms")]:
    st.header(title)
    pics = [x for x in items if x["category"] == cat]
    for i in range(0, len(pics), 2):
        for col, x in zip(st.columns(2), pics[i:i + 2]):
            col.image(str(ROOT / x["file"]), caption=x["caption"])
footer()
