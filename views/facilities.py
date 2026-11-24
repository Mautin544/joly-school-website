import streamlit as st
from components.ui import load, banner, footer, placeholder, ROOT
banner("Our Facilities", "A look at our school and classrooms")
items = load("facilities")
for cat in ["Campus", "Classrooms"]:
    st.header("School Premises" if cat == "Campus" else "Classrooms")
    pics = [x for x in items if x["category"] == cat]
    for i in range(0, len(pics), 2):
        for col, x in zip(st.columns(2), pics[i:i + 2]):
            col.image(str(ROOT / x["file"]), caption=x["caption"])
st.header("More facilities")
placeholder("Photos of other facilities (library, laboratories, sports and play areas) will be added once supplied.")
footer()
