import streamlit as st
from components.ui import css, topbar, load, LOGO

s = load("school")
st.set_page_config(page_title=s["name"], page_icon=str(LOGO / "logo_nursery_primary.png"), layout="wide")
css()
topbar()
pages = [st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
         st.Page("views/about.py", title="About", icon=":material/info:"),
         st.Page("views/academics.py", title="Academics", icon=":material/menu_book:"),
         st.Page("views/admissions.py", title="Admissions", icon=":material/how_to_reg:"),
         st.Page("views/staff.py", title="Management & Staff", icon=":material/groups:"),
         st.Page("views/facilities.py", title="Facilities", icon=":material/apartment:"),
         st.Page("views/news.py", title="News & Events", icon=":material/campaign:"),
         st.Page("views/contact.py", title="Contact", icon=":material/call:")]
st.navigation(pages, position="top").run()
