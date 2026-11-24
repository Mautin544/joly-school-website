import re, requests, streamlit as st

def _valid(name, email, phone, message):
    e = []
    if len(name.strip()) < 3: e.append("Please enter your full name.")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()): e.append("Please enter a valid email address.")
    if not re.fullmatch(r"\+?[0-9\s\-]{7,16}", phone.strip()): e.append("Please enter a valid phone number.")
    if len(message.strip()) < 10: e.append("Please write a message of at least 10 characters.")
    return e

def _send(payload):
    """Posts to a form service (e.g. Formspree) set in Streamlit secrets. True=sent, False=failed, None=not configured."""
    try:
        url = st.secrets.get("FORM_ENDPOINT", "")
    except Exception:
        url = ""
    if not url: return None
    try:
        return requests.post(url, json={**payload, "_subject": "New website enquiry: " + payload.get("form", "")}, headers={"Accept": "application/json"}, timeout=10).ok
    except requests.RequestException:
        return False

def enquiry_form(key, admission=False):
    with st.form(key, clear_on_submit=False):
        name = st.text_input("Full name *", max_chars=80)
        c1, c2 = st.columns(2)
        email = c1.text_input("Email *", max_chars=100)
        phone = c2.text_input("Phone *", max_chars=20)
        extra = {}
        if admission:
            extra["level"] = st.selectbox("Level of interest *", ["Nursery", "Primary", "College"])
            extra["child_name"] = st.text_input("Child's name (optional)", max_chars=80)
        message = st.text_area("Message *", max_chars=1000)
        ok = st.form_submit_button("Send enquiry")
    if not ok: return
    errs = _valid(name, email, phone, message)
    if errs:
        for e in errs: st.error(e)
        return
    res = _send({"form": key, "name": name, "email": email, "phone": phone, "message": message, **extra})
    if res: st.success("Thank you. Your enquiry has been sent. The school will get back to you.")
    elif res is None: st.warning("Your details look fine, but online submission is not connected yet, so nothing was sent. Please call 08038471964 or email jolynurseryandprimaryschool@gmail.com.")
    else: st.error("Sorry, we could not send your message. Please call 08038471964 instead.")
