"""Announcements sorted by date, upcoming events, and a small month calendar."""
import calendar, datetime as dt, html
import streamlit as st
from components.ui import load

FORMATS = ("%Y-%m-%d", "%d/%m/%Y", "%d %B %Y", "%d %b %Y", "%B %d, %Y")

def parse(v):
    if not v: return None
    for f in FORMATS:
        try: return dt.datetime.strptime(str(v).strip(), f).date()
        except ValueError: pass
    return None

def today():  # Nigeria time (UTC+1)
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=1))).date()

def nice(d): return f"{d.day} {d:%B %Y}"
def esc(x): return html.escape(str(x or ""))

def items():
    """All entries, newest first. Entries without a readable date go last."""
    out = []
    for a in load("announcements"):
        a = dict(a); a["_pub"] = parse(a.get("date")); a["_ev"] = parse(a.get("event_date"))
        a["_key"] = a["_pub"] or a["_ev"]
        out.append(a)
    return sorted(out, key=lambda a: (a["_key"] is not None, a["_key"] or dt.date.min), reverse=True)

def upcoming():
    t = today()
    return sorted([a for a in items() if a["_ev"] and a["_ev"] >= t], key=lambda a: a["_ev"])

def announcement_card(a):
    when = nice(a["_pub"]) if a["_pub"] else esc(a.get("date"))
    line = ""
    if a["_ev"]:
        bits = [f"📅 {nice(a['_ev'])}"] + ([f"🕙 {esc(a['event_time'])}"] if a.get("event_time") else []) + ([f"📍 {esc(a['venue'])}"] if a.get("venue") else [])
        line = "<small>" + " · ".join(bits) + "</small><br>"
    return f'<div class="card top rv"><span class="pill" style="background:#2E3192">{esc(a.get("category"))}</span> <small>{when}</small><br><b>{esc(a.get("title"))}</b><br>{line}<p>{esc(a.get("body"))}</p></div><br>'

def event_card(a):
    d = a["_ev"]
    bits = ([f"🕙 {esc(a['event_time'])}"] if a.get("event_time") else []) + ([f"📍 {esc(a['venue'])}"] if a.get("venue") else [])
    sub = f"<small>{' · '.join(bits)}</small><br>" if bits else ""
    return f'<div class="ev rv"><div class="dt"><b>{d.day}</b><span>{d:%b}</span></div><div><b>{esc(a.get("title"))}</b><br>{sub}<small>{esc(a.get("body"))}</small></div></div>'

def calendar_html(events):
    t = today()
    days = {}
    for e in events: days.setdefault((e["_ev"].year, e["_ev"].month), {}).setdefault(e["_ev"].day, []).append(e["title"])
    months = sorted(days)[:3] or [(t.year, t.month)]
    out = ""
    for y, m in months:
        rows = ""
        for wk in calendar.Calendar(0).monthdayscalendar(y, m):
            cells = ""
            for d in wk:
                if not d: cells += "<td></td>"; continue
                cls = "on" if d in days.get((y, m), {}) else ""
                cls += " today" if (y, m, d) == (t.year, t.month, t.day) else ""
                tip = esc("; ".join(days.get((y, m), {}).get(d, [])))
                cells += f'<td class="{cls.strip()}" title="{tip}">{d}</td>'
            rows += f"<tr>{cells}</tr>"
        out += f'<table class="calbox"><caption>{calendar.month_name[m]} {y}</caption><tr><th>Mo</th><th>Tu</th><th>We</th><th>Th</th><th>Fr</th><th>Sa</th><th>Su</th></tr>{rows}</table>'
    return out

def style():
    st.markdown("""<style>
.ev{display:flex;gap:1rem;align-items:center;background:#fff;border:1px solid #e3ebf8;border-radius:16px;padding:.8rem 1rem;margin-bottom:.8rem;box-shadow:0 4px 14px rgba(46,49,146,.08);transition:transform .25s}
.ev:hover{transform:translateY(-4px)}
.ev,.ev :is(p,small,span,b,div,br){color:#1c2340!important}
.ev .dt{min-width:62px;text-align:center;background:linear-gradient(135deg,#2E3192,#00AEEF);border-radius:14px;padding:.5rem}
.ev .dt,.ev .dt *{color:#fff!important}.ev .dt b{display:block;font-size:1.6rem;line-height:1}.ev .dt span{text-transform:uppercase;font-size:.75rem}
.calbox{width:100%;border-collapse:separate;border-spacing:3px;background:#fff;border:1px solid #e3ebf8;border-radius:16px;padding:.6rem;margin-bottom:1rem;font-size:.82rem}
.calbox *{color:#1c2340!important}.calbox caption{font-weight:600;padding:.4rem;caption-side:top}.calbox th{color:#5a6690!important;font-weight:500}
.calbox td,.calbox th{text-align:center;padding:.35rem 0}
.calbox td.on{background:#2E3192;border-radius:9px;font-weight:600}.calbox td.on,.calbox td.on *{color:#fff!important}
.calbox td.today{outline:2px solid #00AEEF;border-radius:9px}
</style>""", unsafe_allow_html=True)
