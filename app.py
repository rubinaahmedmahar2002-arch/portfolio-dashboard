import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Rubina Ahmed Mahar | Portfolio Dashboard",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("Portfolio Dashboard")

page = st.sidebar.radio(
    "Go to",
    ["Overview", "Projects", "Skills", "Experience", "Contact"]
)

if page == "Overview":
    st.title("Rubina Ahmed Mahar")
    st.subheader("ICT Business Analyst | Data Analytics | AI Automation")

    st.write(
        "I build dashboards, reports, trackers, business analysis documents, "
        "and AI automation workflows using Python, SQL, Power BI, Excel, APIs, and LLM tools."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Projects", "8")
    col2.metric("Tools", "12+")
    col3.metric("Focus", "Data, BA, AI")

elif page == "Projects":
    st.title("Projects")

    projects = [
        {
            "title": "AI-Powered Global Data & AI Job Market Intelligence",
            "type": "Data Analytics + Machine Learning",
            "tools": "Python, Pandas, Scikit-learn, Matplotlib",
            "summary": "Analyzed global Data and AI job market trends and built salary prediction models."
        },
        {
            "title": "HR Analytics Dashboard using Power BI",
            "type": "Dashboard",
            "tools": "Power BI, Excel",
            "summary": "Built an HR dashboard to track workforce and employee metrics."
        },
        {
            "title": "CSR Eye Camp Budget and Operations Tracker",
            "type": "Business Analysis",
            "tools": "Excel, Budget Tracking, Process Documentation",
            "summary": "Designed a tracker for CSR eye camp cost planning, vendor estimates, patient volume, and reporting."
        },
        {
            "title": "Global Mental Health Data Analysis and Modeling",
            "type": "Data Analytics + Machine Learning",
            "tools": "Python, Pandas, Matplotlib, Scikit-learn",
            "summary": "Analyzed global mental health indicators and created insight-focused analysis."
        }
    ]

    for project in projects:
        with st.container(border=True):
            st.subheader(project["title"])
            st.write(project["summary"])
            st.write("Type:", project["type"])
            st.write("Tools:", project["tools"])

elif page == "Skills":
    st.title("Skills")

    skills = {
        "Skill": [
            "Python", "SQL", "Power BI", "Excel", "Business Analysis",
            "Data Cleaning", "Dashboard Reporting", "AI Automation",
            "APIs", "LLM Tools"
        ],
        "Level": [
            "Intermediate", "Intermediate", "Intermediate", "Advanced",
            "Intermediate", "Intermediate", "Intermediate",
            "Beginner to Intermediate", "Beginner", "Beginner"
        ],
        "Used For": [
            "EDA, ML, dashboards",
            "Queries and reporting",
            "Dashboards",
            "Trackers, budgets, reports",
            "Process and requirements work",
            "Preparing analysis-ready datasets",
            "Management reporting",
            "n8n and workflow ideas",
            "Automation workflows",
            "RAG and AI agent learning"
        ]
    }

    skills_df = pd.DataFrame(skills)
    st.dataframe(skills_df, use_container_width=True)

elif page == "Experience":
    st.title("Experience")

    experience = [
        {
            "role": "Data Analyst",
            "company": "A. F. Ferguson & Co. | PwC Network",
            "duration": "Sep 2025 - Dec 2025",
            "details": "Worked on data cleaning, KPI reporting, dashboards, SQL and Excel reporting workflows, and data validation."
        },
        {
            "role": "Community Development Intern",
            "company": "Pakistan Petroleum Limited",
            "duration": "Jul 2025 - Aug 2025",
            "details": "Supported CSR project documentation, budget tracking, stakeholder coordination, and project reporting."
        },
        {
            "role": "Quality Assurance Analyst",
            "company": "Oigetit Real-Time AI Intelligence Platform",
            "duration": "Aug 2024 - Nov 2024",
            "details": "Tested web product features, reviewed content quality, documented issues, and supported product improvement."
        }
    ]

    for item in experience:
        with st.container(border=True):
            st.subheader(item["role"])
            st.write(item["company"])
            st.write(item["duration"])
            st.write(item["details"])

elif page == "Contact":
    st.title("Contact")

    st.write("Email: rubinaahmed301@gmail.com")
    st.write("LinkedIn: www.linkedin.com/in/rubina-ahmed-mahar-b03b39220")
    st.write("GitHub: github.com/rubinaahmedmahar2002-arch")
