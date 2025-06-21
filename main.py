import streamlit as st
from datetime import datetime

# --- Logo and Title ---
st.image("Kerala Ceramics  Logo.webp", width=100)
st.markdown("## 🔌 The Kerala Ceramics Limited, Kundara, Kollam")
st.markdown("#### 🛡️ *Electrician Duty Chart* (21 June 2025 - 29 June 2025)")

# --- Staff List ---
staff = {
    "Navin": "Assistant",
    "Rajeesh": "Grade I",
    "Vidul": "Grade II",
    "Anoop": "App.",
    "Habeeb": "App."
}

# --- Fixed Duty Schedule ---
duty_schedule = {
    "2025-06-21": "Habeeb",
    "2025-06-22": "Anoop",
    "2025-06-23": "Vidul",
    "2025-06-24": "Habeeb",
    "2025-06-25": "Anoop",
    "2025-06-26": "Vidul",
    "2025-06-27": "Anoop",
    "2025-06-28": "Habeeb",
    "2025-06-29": "Vidul"
}

# --- Password Control ---
st.sidebar.markdown("### 🔒 Admin Login")
password = st.sidebar.text_input("Enter password to enable editing", type="password")
is_admin = password == "1234"

# --- Show Staff List ---
with st.expander("📋 Staff List"):
    for name, role in staff.items():
        st.markdown(f"- **{name}** ({role})")

# --- Sort Duty Schedule ---
today = datetime.now().date()

today_list = []
upcoming_list = []
completed_list = []

for date_str, name in duty_schedule.items():
    duty_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    if duty_date == today:
        today_list.append((date_str, name))
    elif duty_date > today:
        upcoming_list.append((date_str, name))
    else:
        completed_list.append((date_str, name))

# --- Display Duties ---
st.markdown("### 🌙 Today's Duty")
for d, n in today_list:
    st.info(f"📅 **{d}** — 🛡️ {n}")

st.markdown("### 🔜 Upcoming Duties")
for d, n in upcoming_list:
    st.success(f"📅 **{d}** — 🛡️ {n}")

st.markdown("### ✅ Completed Duties")
for d, n in completed_list:
    st.warning(f"📅 **{d}** — 🛡️ {n}")

# --- Daily Message Box ---
st.markdown("## 💬 Duty Note")
if is_admin:
    msg = st.text_area("Type today's note (only visible for you to edit)", key="msg")
    st.button("💾 Save", help="Auto save not enabled in this demo")
else:
    st.write("🔒 Only admin can edit the message.")

