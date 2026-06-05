import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Rubina Ahmed Mahar | Portfolio Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #08111f 0%, #10243d 45%, #241233 100%);
        color: #ffffff;
    }

    [data-testid="stSidebar"] {
        background: rgba(5, 12, 24, 0.95);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    h1, h2, h3 {
        color: #ffffff;
    }

    .hero-card {
        padding: 35px;
        border-radius: 28px;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.14);
        box-shadow: 0 20px 60px rgba(0,0,0,0.25);
        backdrop-filter: blur(14px);
        margin-bottom: 25px;
    }

    .mini-card {
        padding: 22px;
        border-radius: 22px;
        background: rgba(255, 255, 255, 0.09);
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 12px 35px rgba(0,0,0,0.20);
        min-height: 150px;
    }

    .project-card {
        padding: 24px;
        border-radius: 22px;
        background: rgba(255,255,255,0.09);
        border: 1px solid rgba(255,255,255,0.12);
        margin-bottom: 18px;
        box-shadow: 0 14px 38px rgba(0,0,0,0.20);
    }

    .badge {
        display: inline-block;
        padding: 7px 12px;
        margin: 4px 5px 4px 0;
        border-radius: 999px;
        background: rgba(122, 92, 255, 0.22);
        border: 1px solid rgba(122, 92, 255, 0.45);
        color: #ffffff;
        font-size: 13px;
    }

    .soft-text {
        color: rgba(255,255,255,0.78);
        font-size: 17px;
        line-height: 1.7;
    }

    .big-name {
        font-size: 54px;
        font-weight: 800;
        line-height: 1.05;
        margin-bottom: 10px;
        background: linear-gradient(90deg, #ffffff, #bca7ff, #7dd3fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .role-line {
        font-size: 22px;
        color: #d7ccff;
        font-weight: 600;
        margin-bottom: 18px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 750;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .footer-card {
        padding: 25px;
        border-radius: 22px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        margin-top: 25px;
    }

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.12);
        padding: 18px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.08);
        border-radius: 999px;
        padding: 10px 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Animation loader
# ----------------------------

def load_lottie_url(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception:
        return None

lottie_dashboard = load_lottie_url(
    "https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json"
)

# ----------------------------
# Data
# ----------------------------

projects = [
    {
        "title": "AI-Powered Global Data & AI Job Market Intelligence",
        "type": "Machine Learning",
        "role": "Data Analyst",
        "tools": ["Python", "Pandas", "Scikit-learn", "Matplotlib"],
        "summary": "Analyzed global Data and AI job market trends, salary patterns, role demand, and regional differences.",
        "impact": "Built salary prediction models and turned job market data into career-focused insights.",
        "link": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "title": "HR Analytics Dashboard using Power BI",
        "type": "Dashboard",
        "role": "Data Analyst",
        "tools": ["Power BI", "Excel", "HR Metrics"],
        "summary": "Built an HR dashboard to track workforce demographics and key employee metrics.",
        "impact": "Created a clean reporting view for HR decision-making.",
        "link": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "title": "CSR Eye Camp Budget and Operations Tracker",
        "type": "Business Analysis",
        "role": "Business Analyst",
        "tools": ["Excel", "Budgeting", "Process Tracking"],
        "summary": "Designed a tracker for CSR eye camp cost planning, vendor estimates, patient volume, and reporting.",
        "impact": "Converted field project planning into a structured management tracker.",
        "link": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "title": "Global Mental Health Data Analysis and Modeling",
        "type": "Machine Learning",
        "role": "Data Analyst",
        "tools": ["Python", "Pandas", "Visualization", "Modeling"],
        "summary": "Analyzed global mental health indicators across countries, years, and population groups.",
        "impact": "Created insight-focused public health analysis with basic modeling.",
        "link": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "title": "Water Quality Exploratory Data Analysis",
        "type": "EDA",
        "role": "Data Analyst",
        "tools": ["Python", "Pandas", "Matplotlib"],
        "summary": "Explored water quality data to identify missing values, trends, and safety indicators.",
        "impact": "Built clear visual summaries for environmental data analysis.",
        "link": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "title": "Scholarship Disbursement Process Tracker",
        "type": "Business Analysis",
        "role": "ICT Business Analyst",
        "tools": ["Excel", "Documentation", "Status Reporting"],
        "summary": "Designed a tracker for scholarship records, university follow-ups, documentation status, and payment progress.",
        "impact": "Mapped a business process into a practical reporting system.",
        "link": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    }
]

skills_data = pd.DataFrame({
    "Skill": [
        "Python", "SQL", "Power BI", "Excel", "Business Analysis",
        "Data Cleaning", "Dashboard Reporting", "AI Automation",
        "APIs", "LLM Tools", "n8n", "Process Documentation"
    ],
    "Category": [
        "Data Analytics", "Data Analytics", "Dashboarding", "Business Reporting",
        "Business Analysis", "Data Analytics", "Dashboarding", "AI Automation",
        "AI Automation", "AI Automation", "AI Automation", "Business Analysis"
    ],
    "Level": [
        75, 70, 70, 85, 75, 80, 75, 55, 50, 50, 55, 80
    ]
})

experience = [
    {
        "role": "Data Analyst",
        "company": "A. F. Ferguson & Co. | PwC Network",
        "duration": "Sep 2025 - Dec 2025",
        "details": "Data cleaning, KPI reporting, dashboards, SQL and Excel workflows, and data validation."
    },
    {
        "role": "Community Development Intern",
        "company": "Pakistan Petroleum Limited",
        "duration": "Jul 2025 - Aug 2025",
        "details": "CSR documentation, budget tracking, stakeholder coordination, and project reporting."
    },
    {
        "role": "Quality Assurance Analyst",
        "company": "Oigetit Real-Time AI Intelligence Platform",
        "duration": "Aug 2024 - Nov 2024",
        "details": "Web testing, content quality checks, issue documentation, and workflow improvement."
    }
]

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.markdown("## Rubina Ahmed Mahar")
st.sidebar.caption("Portfolio Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Projects", "Skills", "Experience", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Focus")
st.sidebar.markdown(
    """
    <span class="badge">Data Analytics</span>
    <span class="badge">ICT Business Analysis</span>
    <span class="badge">AI Automation</span>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Home
# ----------------------------

if page == "Home":
    left, right = st.columns([1.6, 1])

    with left:
        st.markdown(
            """
            <div class="hero-card">
                <div class="big-name">Rubina Ahmed Mahar</div>
                <div class="role-line">ICT Business Analyst | Data Analytics | AI Automation</div>
                <p class="soft-text">
                    I build dashboards, reports, trackers, business analysis documents, and AI automation workflows.
                    My work connects business problems with data, systems, and practical digital solutions.
                </p>
                <span class="badge">Python</span>
                <span class="badge">SQL</span>
                <span class="badge">Power BI</span>
                <span class="badge">Excel</span>
                <span class="badge">Business Systems</span>
                <span class="badge">AI Automation</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        if lottie_dashboard:
            st_lottie(lottie_dashboard, height=300, key="dashboard_animation")
        else:
            st.markdown(
                """
                <div class="mini-card">
                    <h3>Portfolio Dashboard</h3>
                    <p class="soft-text">Interactive analytics-style portfolio built with Python and Streamlit.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projects", "8")
    col2.metric("Core Tools", "12+")
    col3.metric("Experience", "6 Roles")
    col4.metric("Focus", "Data + BA + AI")

    st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    cards = [
        ("AI Job Market Intelligence", "Machine learning project focused on salaries, roles, and global Data and AI trends."),
        ("HR Analytics Dashboard", "Power BI dashboard project focused on workforce reporting and employee metrics."),
        ("CSR Operations Tracker", "Business analysis tracker for budget planning, vendors, patient volume, and reporting.")
    ]

    for col, card in zip([c1, c2, c3], cards):
        with col:
            st.markdown(
                f"""
                <div class="mini-card">
                    <h3>{card[0]}</h3>
                    <p class="soft-text">{card[1]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="section-title">Portfolio Snapshot</div>', unsafe_allow_html=True)

    project_df = pd.DataFrame(projects)
    type_count = project_df["type"].value_counts().reset_index()
    type_count.columns = ["Project Type", "Count"]

    fig = px.bar(
        type_count,
        x="Project Type",
        y="Count",
        title="Projects by Type",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Projects
# ----------------------------

elif page == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

    project_df = pd.DataFrame(projects)

    role_filter = st.multiselect(
        "Filter by role focus",
        sorted(project_df["role"].unique())
    )

    type_filter = st.multiselect(
        "Filter by project type",
        sorted(project_df["type"].unique())
    )

    filtered = projects

    if role_filter:
        filtered = [p for p in filtered if p["role"] in role_filter]

    if type_filter:
        filtered = [p for p in filtered if p["type"] in type_filter]

    for project in filtered:
        tools_html = "".join([f'<span class="badge">{tool}</span>' for tool in project["tools"]])

        st.markdown(
            f"""
            <div class="project-card">
                <h3>{project["title"]}</h3>
                <p class="soft-text">{project["summary"]}</p>
                <p><b>Project type:</b> {project["type"]}</p>
                <p><b>Role focus:</b> {project["role"]}</p>
                <p><b>Outcome:</b> {project["impact"]}</p>
                {tools_html}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button("Open Project Repository", project["link"])

# ----------------------------
# Skills
# ----------------------------

elif page == "Skills":
    st.markdown('<div class="section-title">Skills Matrix</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Skill Table", "Skill Chart"])

    with tab1:
        st.dataframe(skills_data, use_container_width=True)

    with tab2:
        fig = px.bar(
            skills_data,
            x="Level",
            y="Skill",
            color="Category",
            orientation="h",
            title="Skill Strength by Category",
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Experience
# ----------------------------

elif page == "Experience":
    st.markdown('<div class="section-title">Experience Timeline</div>', unsafe_allow_html=True)

    for item in experience:
        st.markdown(
            f"""
            <div class="project-card">
                <h3>{item["role"]}</h3>
                <p><b>{item["company"]}</b></p>
                <p>{item["duration"]}</p>
                <p class="soft-text">{item["details"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ----------------------------
# Contact
# ----------------------------

elif page == "Contact":
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="footer-card">
            <h3>Let’s connect</h3>
            <p class="soft-text">
                I am open to Data Analyst, Business Analyst, ICT Business Analyst,
                Business Systems, and AI Automation opportunities.
            </p>
            <p><b>Email:</b> rubinaahmed301@gmail.com</p>
            <p><b>LinkedIn:</b> www.linkedin.com/in/rubina-ahmed-mahar-b03b39220</p>
            <p><b>GitHub:</b> github.com/rubinaahmedmahar2002-arch</p>
        </div>
        """,
        unsafe_allow_html=True
    )
