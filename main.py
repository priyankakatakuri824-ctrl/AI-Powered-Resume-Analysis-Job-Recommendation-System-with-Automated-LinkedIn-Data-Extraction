# main.py
import streamlit as st
from utils.database import init_db, migrate_saved_jobs_table

# -----------------------------
# FRONTEND PAGES
# -----------------------------
from frontend.login import login_page
from frontend.registration import registration_page
from frontend.dashboard import dashboard_page
from frontend.my_profile import my_profile_page
from frontend.upload_resume import upload_resume_page
from frontend.analysis_page import analysis_page
from frontend.skills_gap_page import skills_gap_page
from frontend.score_page import score_page
from frontend.suggestions_page import suggestions_page
from frontend.job_recommendations import job_recommendations_page
from frontend.job_preferences import job_preferences_page

from backend.auth import logout_user

from utils.database import (
    init_db,
    migrate_saved_jobs_table,
    migrate_resume_analysis_table,
    migrate_users_table
)

init_db()
migrate_saved_jobs_table()
migrate_resume_analysis_table()
migrate_users_table()

# GLOBAL SIDEBAR
def sidebar_navigation():

    st.sidebar.markdown("""
    <style>
        .nav-btn {
            width:100%;
            text-align:left;
            padding:10px 14px;
            margin-bottom:6px;
            border-radius:10px;
            font-weight:600;
            border:none;
            background:#f1f5f9;
            color:#1f2937;
            cursor:pointer;
        }
        .nav-btn:hover {
            background:#dbeafe;
        }
        .nav-active {
            background:#2563eb !important;
            color:white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("## 📍 Navigation")

    nav_items = [
        ("🏠 Dashboard", "dashboard"),
        ("👤 My Profile", "profile"),
        ("📤 Upload Resume", "upload"),
        ("📊 Resume Analysis", "analysis"),
        ("🧠 Skills Gap", "skills_gap"),
        ("📈 Resume Scoring", "scoring"),
        ("⚙ Job Preferences", "job_preferences"),
        ("💼 Job Recommendations", "jobs"),
        ("🛠 Suggestions", "suggestions"),
        ("🚪 Logout", "logout"),
    ]

    current_page = st.session_state.get("page", "dashboard")
    resume_uploaded = st.session_state.get("resume_uploaded", False)

    # 🔒 Pages that require resume
    locked_pages = {"analysis", "skills_gap", "scoring"}

    for label, page_key in nav_items:

        # 👉 THIS IS WHERE YOUR CODE GOES
        if page_key in locked_pages and not resume_uploaded:
            label = f"🔒 {label}"

        clicked = st.sidebar.button(
            label,
            key=f"nav_{page_key}",
            use_container_width=True
        )

        if clicked:
            st.session_state["page"] = page_key
            st.rerun()


# MAIN APP
def main():

    # ---------- PAGE CONFIG ----------
    st.set_page_config(
        page_title="AI Resume System",
        page_icon="📄",
        layout="wide"
    )

    # ---------- INIT DB ----------
    init_db()
    migrate_saved_jobs_table()

    # ---------- SESSION DEFAULTS ----------
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("page", "login")
    st.session_state.setdefault("resume_uploaded", False)

    # 🔐 AUTH FLOW (NO SIDEBAR)
    if not st.session_state["logged_in"]:

        if st.session_state["page"] == "login":
            login_page()

        elif st.session_state["page"] == "register":
            registration_page()

        return

    # 📍 SIDEBAR (ALL PAGES)
    sidebar_navigation()

    # 📄 PAGE ROUTER
    page = st.session_state["page"]
    resume_uploaded = st.session_state.get("resume_uploaded", False)

    if page == "dashboard":
        dashboard_page()

    elif page == "profile":
        my_profile_page()

    elif page == "upload":
        upload_resume_page()

    elif page == "analysis":
        if resume_uploaded:
            analysis_page(st.session_state.get("resume_text", ""))
        else:
            st.warning("⚠ Please upload a resume first.")
            st.session_state["page"] = "upload"
            st.rerun()

    elif page == "skills_gap":
        if resume_uploaded:
            skills_gap_page()
        else:
            st.warning("⚠ Please upload a resume first.")
            st.session_state["page"] = "upload"
            st.rerun()

    elif page == "scoring":
        if resume_uploaded:
            score_page()
        else:
            st.warning("⚠ Please upload a resume first.")
            st.session_state["page"] = "upload"
            st.rerun()

    elif page == "job_preferences":
        job_preferences_page()

    elif page == "jobs":
        job_recommendations_page()

    elif page == "suggestions":
        suggestions_page()

    elif page == "logout":
        logout_user()
        st.session_state.clear()
        st.session_state["page"] = "login"
        st.rerun()


# RUN
if __name__ == "__main__":
    main()
