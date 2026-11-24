import streamlit as st
from components.ui import css, topbar, load, LOGO

s = load("school")
st.set_page_config(page_title=s["name"], page_icon=str(LOGO / "logo_nursery_primary.png"), layout="wide")
css()
topbar()
pages = [st.Page("views/home.py", title="Home", icon="🏠", default=True),
         st.Page("views/about.py", title="About", icon="🏫"),
         st.Page("views/academics.py", title="Academics", icon="📚"),
         st.Page("views/admissions.py", title="Admissions", icon="📝"),
         st.Page("views/staff.py", title="Management & Staff", icon="👥"),
         st.Page("views/school_life.py", title="School Life", icon="🎨"),
         st.Page("views/facilities.py", title="Facilities", icon="🏢"),
         st.Page("views/news.py", title="News & Events", icon="📣"),
         st.Page("views/contact.py", title="Contact", icon="📞")]
st.navigation(pages, position="top").run()
