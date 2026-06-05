
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Rubina Ahmed Mahar | Analytics Command Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# STYLE
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(56, 189, 248, 0.22), transparent 28%),
            radial-gradient(circle at 92% 8%, rgba(168, 85, 247, 0.22), transparent 28%),
            radial-gradient(circle at 50% 95%, rgba(34, 197, 94, 0.10), transparent 26%),
            linear-gradient(135deg, #020617 0%, #07111f 46%, #111827 100%);
        color: #f8fafc;
    }

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #020617 0%, #0f172a 55%, #111827 100%);
        border-right: 1px solid rgba(148, 163, 184, 0.24);
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: #f8fafc !important;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .hero {
        position: relative;
        padding: 42px;
        border-radius: 34px;
        overflow: hidden;
        background:
            linear-gradient(135deg, rgba(15, 23, 42, 0.94), rgba(30, 41, 59, 0.76)),
            radial-gradient(circle at 88% 22%, rgba(14, 165, 233, 0.28), transparent 28%),
            radial-gradient(circle at 18% 85%, rgba(168, 85, 247, 0.23), transparent 28%);
        border: 1px solid rgba(148, 163, 184, 0.28);
        box-shadow: 0 28px 90px rgba(0,0,0,0.48);
        min-height: 430px;
    }

    .hero::before {
        content: "";
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px);
        background-size: 34px 34px;
        mask-image: linear-gradient(to bottom, black, transparent 92%);
        pointer-events: none;
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .eyebrow {
        display: inline-flex;
        padding: 9px 15px;
        border-radius: 999px;
        background: rgba(34, 211, 238, 0.12);
        border: 1px solid rgba(34, 211, 238, 0.36);
        color: #a5f3fc !important;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 0.4px;
        text-transform: uppercase;
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 66px;
        line-height: 0.98;
        font-weight: 900;
        letter-spacing: -2.8px;
        margin-bottom: 18px;
        background: linear-gradient(90deg, #ffffff 0%, #bfdbfe 36%, #c4b5fd 72%, #f0abfc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 24px;
        line-height: 1.45;
        max-width: 1000px;
        color: #dbeafe !important;
        font-weight: 700;
        margin-bottom: 22px;
    }

    .hero-text {
        font-size: 16px;
        line-height: 1.8;
        max-width: 940px;
        color: #cbd5e1 !important;
    }

    .section-title {
        font-size: 34px;
        font-weight: 900;
        letter-spacing: -1px;
        margin: 22px 0 16px 0;
        color: #ffffff !important;
    }

    .subtle {
        color: #cbd5e1 !important;
        line-height: 1.75;
    }

    .small-muted {
        color: #94a3b8 !important;
        font-size: 13px;
        line-height: 1.6;
    }

    .badge {
        display: inline-block;
        padding: 8px 13px;
        margin: 5px 6px 5px 0;
        border-radius: 999px;
        background: rgba(59, 130, 246, 0.14);
        border: 1px solid rgba(147, 197, 253, 0.30);
        color: #dbeafe !important;
        font-size: 13px;
        font-weight: 800;
    }

    .badge-purple {
        display: inline-block;
        padding: 8px 13px;
        margin: 5px 6px 5px 0;
        border-radius: 999px;
        background: rgba(168, 85, 247, 0.15);
        border: 1px solid rgba(216, 180, 254, 0.32);
        color: #f3e8ff !important;
        font-size: 13px;
        font-weight: 800;
    }

    .badge-green {
        display: inline-block;
        padding: 8px 13px;
        margin: 5px 6px 5px 0;
        border-radius: 999px;
        background: rgba(34, 197, 94, 0.14);
        border: 1px solid rgba(134, 239, 172, 0.30);
        color: #dcfce7 !important;
        font-size: 13px;
        font-weight: 800;
    }

    .badge-orange {
        display: inline-block;
        padding: 8px 13px;
        margin: 5px 6px 5px 0;
        border-radius: 999px;
        background: rgba(249, 115, 22, 0.14);
        border: 1px solid rgba(253, 186, 116, 0.30);
        color: #ffedd5 !important;
        font-size: 13px;
        font-weight: 800;
    }

    .glass {
        padding: 24px;
        border-radius: 26px;
        background: rgba(15, 23, 42, 0.76);
        border: 1px solid rgba(148, 163, 184, 0.23);
        box-shadow: 0 16px 45px rgba(0,0,0,0.28);
        height: 100%;
    }

    .glass:hover {
        transform: translateY(-5px);
        border-color: rgba(125, 211, 252, 0.55);
        transition: all 0.25s ease;
    }

    .project-card {
        padding: 26px;
        border-radius: 28px;
        background:
            linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.84));
        border: 1px solid rgba(148, 163, 184, 0.24);
        box-shadow: 0 22px 58px rgba(0,0,0,0.34);
        margin-bottom: 18px;
    }

    .project-card:hover {
        border-color: rgba(14, 165, 233, 0.58);
        transform: scale(1.01);
        transition: all 0.22s ease;
    }

    .timeline {
        padding: 20px 24px;
        border-left: 4px solid rgba(56, 189, 248, 0.85);
        margin-bottom: 18px;
        background: rgba(15, 23, 42, 0.74);
        border-radius: 20px;
        border: 1px solid rgba(148, 163, 184, 0.20);
        box-shadow: 0 16px 45px rgba(0,0,0,0.26);
    }

    .control-room {
        padding: 28px;
        border-radius: 30px;
        background:
            radial-gradient(circle at 15% 15%, rgba(34, 211, 238, 0.18), transparent 25%),
            radial-gradient(circle at 82% 18%, rgba(168, 85, 247, 0.20), transparent 28%),
            radial-gradient(circle at 50% 100%, rgba(34, 197, 94, 0.13), transparent 28%),
            rgba(15, 23, 42, 0.84);
        border: 1px solid rgba(148, 163, 184, 0.26);
        box-shadow: 0 24px 64px rgba(0,0,0,0.38);
    }

    .stat-number {
        font-size: 38px;
        font-weight: 900;
        color: #bae6fd !important;
    }

    .stat-label {
        font-size: 13px;
        color: #cbd5e1 !important;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    div[data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid rgba(148, 163, 184, 0.24);
        padding: 18px;
        border-radius: 22px;
        box-shadow: 0 16px 38px rgba(0,0,0,0.28);
    }

    div[data-testid="stMetric"] label {
        color: #cbd5e1 !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-weight: 900 !important;
    }

    .stSelectbox label, .stMultiSelect label, .stSlider label, .stTextInput label {
        color: #f8fafc !important;
        font-weight: 800 !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 999px;
        padding: 12px 20px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.34), rgba(168, 85, 247, 0.34));
        border-color: rgba(125, 211, 252, 0.58);
    }

    a { color: #93c5fd !important; }

    iframe {
        border-radius: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DATA
# =========================================================

projects = [
    {
        "name": "AutoFlow Intelligence",
        "full_title": "AI-Powered Business Process Automation Dashboard",
        "domain": "Business Process Automation",
        "role": "ICT Business Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Synthetic workflow dataset",
        "tools": ["Python", "SQL", "Power BI", "Process Mapping", "AI Recommendations"],
        "problem": "Manual business workflows often hide bottlenecks, error patterns, rework, and avoidable cost.",
        "solution": "Build a dashboard that compares manual steps with automation-ready workflows and highlights process improvement opportunities.",
        "business_value": "Supports management decisions around automation priority, time savings, error reduction, and cost control.",
        "pages": ["Executive Overview", "Process Flow", "Automation Impact", "AI Recommendations"],
        "kpis": ["Total cases", "Average processing time", "Manual hours saved", "Error rate", "Estimated cost savings"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "RetentionLab",
        "full_title": "Customer Churn and Retention Intelligence Dashboard",
        "domain": "Customer Analytics",
        "role": "Data Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Synthetic customer dataset",
        "tools": ["Python", "SQL", "Machine Learning", "Power BI", "Customer Segmentation"],
        "problem": "Businesses lose revenue when they do not identify at-risk customers early.",
        "solution": "Build churn risk scores, customer segments, and retention action recommendations.",
        "business_value": "Helps prioritise retention campaigns, save revenue, and understand churn drivers.",
        "pages": ["Churn Overview", "Customer Segments", "Churn Drivers", "Action Plan"],
        "kpis": ["Churn rate", "Revenue at risk", "High-risk customers", "Retention opportunity value"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "MarketSignal ROI",
        "full_title": "Marketing ROI and Campaign Performance Dashboard",
        "domain": "Marketing Analytics",
        "role": "Marketing Analyst",
        "status": "Planned",
        "difficulty": "Intermediate",
        "dataset": "Synthetic campaign data or public company signals",
        "tools": ["Power BI", "Excel", "SQL", "Funnel Analysis", "ROI Analysis"],
        "problem": "Marketing teams need to know which campaigns and channels generate profitable outcomes.",
        "solution": "Analyze channel spend, conversions, revenue, profitability, and budget allocation.",
        "business_value": "Improves marketing budget decisions and connects campaigns with sales outcomes.",
        "pages": ["Campaign Overview", "Channel Performance", "Customer Funnel", "Budget Optimizer"],
        "kpis": ["Total spend", "Revenue", "ROAS", "Conversion rate", "CPA"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "WorkforcePulse",
        "full_title": "HR Workforce Analytics and Attrition Dashboard",
        "domain": "HR Analytics",
        "role": "Data Analyst",
        "status": "In Progress",
        "difficulty": "Intermediate",
        "dataset": "HR sample dataset",
        "tools": ["Power BI", "DAX", "Excel", "HR Metrics", "Data Cleaning"],
        "problem": "Management needs visibility into attrition, hiring, salary gaps, and workforce structure.",
        "solution": "Build a workforce dashboard with attrition analysis, hiring trends, and retention recommendations.",
        "business_value": "Supports HR planning, salary review, hiring strategy, and retention decisions.",
        "pages": ["Workforce Overview", "Attrition Analysis", "Hiring and Promotion", "Management Insights"],
        "kpis": ["Employees", "Attrition rate", "Average salary", "Average tenure", "Gender ratio"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "CFO Control Room",
        "full_title": "Financial Performance and Cash Flow Analytics Dashboard",
        "domain": "Financial Analytics",
        "role": "Business Analyst",
        "status": "Planned",
        "difficulty": "Intermediate",
        "dataset": "Simulated financial dataset",
        "tools": ["Excel", "Power BI", "SQL", "Variance Analysis", "Accounting"],
        "problem": "Managers need to understand revenue, expenses, profit, cash flow, and budget variance.",
        "solution": "Create a CFO-style dashboard that explains performance movement and cost control areas.",
        "business_value": "Connects accounting data with executive decision-making and budget control.",
        "pages": ["Financial Overview", "Revenue Analysis", "Expense and Budget Control", "Cash Flow"],
        "kpis": ["Revenue", "Gross profit", "Net profit", "Operating expenses", "Cash balance"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "CityPulse Business Intelligence",
        "full_title": "Public City Data to Small Business Insights Dashboard",
        "domain": "Public Data Analytics",
        "role": "Data Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Open city data",
        "tools": ["Python", "Public APIs", "Geospatial Analytics", "Power BI Maps", "Business Storytelling"],
        "problem": "Small businesses need location intelligence but often cannot afford expensive market research.",
        "solution": "Use city open data to score suburbs for demand, competition, risk, and opportunity.",
        "business_value": "Helps cafes, clinics, cleaning companies, and retail stores choose better locations.",
        "pages": ["Location Score", "Map View", "Business Opportunity", "Final Recommendation"],
        "kpis": ["Best suburbs", "Demand score", "Competition level", "Risk score", "Opportunity score"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "TalentMatch AI",
        "full_title": "AI Resume Screening and Recruitment Analytics Dashboard",
        "domain": "AI + HR Systems",
        "role": "ICT Business Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Sample candidate dataset",
        "tools": ["Python", "NLP", "AI Automation", "Power BI", "Responsible AI"],
        "problem": "Recruitment teams need faster screening, but AI systems must stay transparent and fair.",
        "solution": "Build a candidate matching dashboard with skill extraction, pipeline analytics, and fairness checks.",
        "business_value": "Improves hiring pipeline visibility while keeping human review and responsible AI in the process.",
        "pages": ["Recruitment Overview", "Candidate Match", "Pipeline Analytics", "Bias and Fairness"],
        "kpis": ["Applicants", "Shortlisted candidates", "Average match score", "Hiring funnel conversion"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Inventory Control Tower",
        "full_title": "Supply Chain and Inventory Optimization Dashboard",
        "domain": "Operations Analytics",
        "role": "Operations Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Retail inventory dataset",
        "tools": ["SQL", "Power BI", "Inventory Analytics", "Forecasting", "Operations Analysis"],
        "problem": "Businesses lose money through stockouts, overstocking, slow-moving inventory, and supplier delays.",
        "solution": "Build an inventory dashboard with reorder recommendations and supplier performance analysis.",
        "business_value": "Supports purchasing decisions, stock control, supplier review, and margin protection.",
        "pages": ["Inventory Overview", "Product Performance", "Supplier Performance", "Reorder Recommendation"],
        "kpis": ["Inventory value", "Stockout risk", "Overstocked items", "Slow-moving stock", "Supplier delay rate"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "CSR Impact Monitor",
        "full_title": "CSR Project Monitoring and Impact Dashboard",
        "domain": "CSR Analytics",
        "role": "Business Analyst",
        "status": "In Progress",
        "difficulty": "Advanced",
        "dataset": "Synthetic CSR project dataset inspired by internship workflows",
        "tools": ["Excel", "Power BI", "Budget Analysis", "Stakeholder Reporting", "Compliance Tracking"],
        "problem": "CSR projects need clear tracking across budgets, vendors, beneficiaries, documents, and impact.",
        "solution": "Build a CSR dashboard for health, education, water supply, and welfare initiatives.",
        "business_value": "Connects project monitoring, budget control, beneficiary reporting, and compliance tracking.",
        "pages": ["CSR Portfolio Overview", "Project Category", "Budget and Vendor", "Impact", "Compliance"],
        "kpis": ["Projects", "Budget used", "Beneficiaries", "Completed projects", "Delayed projects"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "KnowledgeOps AI",
        "full_title": "RAG-Based Business Knowledge Assistant Dashboard",
        "domain": "AI Automation",
        "role": "AI Automation Analyst",
        "status": "Planned",
        "difficulty": "Expert",
        "dataset": "Sample company documents",
        "tools": ["Python", "LLMs", "RAG", "APIs", "Vector Databases", "Dashboard Monitoring"],
        "problem": "Business teams waste time searching policies, SOPs, reports, and project documents.",
        "solution": "Build a RAG-based assistant that answers questions from sample business documents and tracks answer quality.",
        "business_value": "Improves knowledge access, document coverage, unresolved question tracking, and human review workflows.",
        "pages": ["AI Assistant Overview", "Document Knowledge Base", "Query Analytics", "Quality and Risk"],
        "kpis": ["Questions asked", "Answer success rate", "Response time", "Documents searched", "Unanswered questions"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    }
]

skills = pd.DataFrame({
    "Skill": [
        "Python", "SQL", "Power BI", "Excel", "DAX", "Pandas", "Scikit-learn",
        "Business Analysis", "Process Mapping", "Data Cleaning", "KPI Reporting",
        "Financial Analysis", "HR Analytics", "Marketing Analytics", "Customer Analytics",
        "CSR Analytics", "Inventory Analytics", "AI Automation", "LLMs", "RAG", "APIs",
        "Stakeholder Reporting", "Documentation"
    ],
    "Category": [
        "Data Analytics", "Data Analytics", "Dashboarding", "Business Reporting", "Dashboarding",
        "Data Analytics", "Machine Learning", "Business Analysis", "Business Analysis",
        "Data Quality", "Business Reporting", "Finance Analytics", "HR Analytics",
        "Marketing Analytics", "Customer Analytics", "CSR Analytics", "Operations Analytics",
        "AI Automation", "AI Automation", "AI Automation", "AI Automation",
        "Business Analysis", "Business Analysis"
    ],
    "Strength": [76, 70, 74, 86, 58, 78, 63, 80, 78, 82, 78, 68, 70, 66, 68, 82, 60, 58, 52, 48, 50, 84, 86]
})

experience = [
    {
        "role": "Data Analyst",
        "company": "A. F. Ferguson & Co. | PwC Network",
        "duration": "Sep 2025 - Dec 2025",
        "details": "Prepared datasets, supported Excel and SQL reporting workflows, built dashboards, validated operational and workforce data, and supported KPI reporting.",
        "tags": ["Data Cleaning", "KPI Reporting", "SQL", "Excel", "Dashboards"]
    },
    {
        "role": "Community Development Intern",
        "company": "Pakistan Petroleum Limited",
        "duration": "Jul 2025 - Aug 2025",
        "details": "Supported CSR projects across education, health, water supply, and welfare. Prepared budget sheets, trackers, documentation packs, and stakeholder follow-up records.",
        "tags": ["CSR", "Budgeting", "Documentation", "Stakeholders", "Reporting"]
    },
    {
        "role": "Quality Assurance Analyst",
        "company": "Oigetit Real-Time AI Intelligence Platform",
        "duration": "Aug 2024 - Nov 2024",
        "details": "Tested web features, reviewed content quality, monitored RSS feeds, documented defects, and supported product workflow improvements.",
        "tags": ["QA", "Testing", "AI Platform", "Issue Tracking", "Workflow"]
    },
    {
        "role": "Data Science Intern",
        "company": "Prodigy InfoTech",
        "duration": "Jun 2024 - Aug 2024",
        "details": "Completed data cleaning, exploratory analysis, visualisation, and basic predictive modelling tasks using Python.",
        "tags": ["Python", "EDA", "Visualization", "ML Basics"]
    },
    {
        "role": "Data Science and AI Intern",
        "company": "SYNC INTERN'S",
        "duration": "Mar 2024 - Apr 2024",
        "details": "Completed analytics and AI tasks related to customer analysis, experimentation, and commercial data interpretation.",
        "tags": ["AI", "Customer Analysis", "Experimentation"]
    }
]

certifications = [
    "Complete Data Analyst Bootcamp From Basics To Advanced",
    "Complete N8N and AI Automation Masterclass",
    "AI Automation: Build LLM Apps and AI Agents with n8n and APIs",
    "The Complete AI Agents and AI Automation Course",
    "Become an IT Business Analyst: Learn, Apply, Succeed",
    "SQL for Data Science",
    "Introduction to Artificial Intelligence",
    "Data and Programming Foundations for AI",
    "IT Support Entry Level Job Training Course",
    "IT System Engineer and Cloud System Administration"
]

evidence = [
    {
        "claim": "I can clean and prepare business datasets",
        "proof": "Prepared and structured multi-source datasets for reporting and KPI tracking.",
        "source": "A. F. Ferguson Data Analyst role",
        "confidence": "Strong"
    },
    {
        "claim": "I can build dashboard-style reporting",
        "proof": "Built HR dashboard work and analytical summaries for management-style reporting.",
        "source": "HR Analytics, A. F. Ferguson role",
        "confidence": "Strong"
    },
    {
        "claim": "I can document business processes",
        "proof": "Created CSR trackers, documentation packs, budget sheets, and status records.",
        "source": "Pakistan Petroleum Limited internship",
        "confidence": "Strong"
    },
    {
        "claim": "I can apply machine learning to business problems",
        "proof": "Built prediction and modeling projects using Python, Linear Regression, Random Forest, and classification workflows.",
        "source": "Portfolio ML projects",
        "confidence": "Developing"
    },
    {
        "claim": "I am building AI automation capability",
        "proof": "Learning n8n, APIs, LLM workflows, RAG concepts, and AI automation dashboards.",
        "source": "Certifications and planned KnowledgeOps AI project",
        "confidence": "Developing"
    }
]

project_df = pd.DataFrame(projects)
evidence_df = pd.DataFrame(evidence)

# =========================================================
# HELPERS
# =========================================================

def tags_html(tags, color="blue"):
    klass = {
        "blue": "badge",
        "purple": "badge-purple",
        "green": "badge-green",
        "orange": "badge-orange"
    }.get(color, "badge")
    return "".join([f'<span class="{klass}">{tag}</span>' for tag in tags])

def status_badge(status):
    if status == "Completed":
        return "badge-green"
    if status == "In Progress":
        return "badge-orange"
    if status == "Prototype":
        return "badge-purple"
    return "badge"

def plotly_layout(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("### ⚡ Rubina Ahmed Mahar")
    st.caption("Analytics Command Center")

    selected = option_menu(
        menu_title=None,
        options=[
            "Command Center",
            "Project Galaxy",
            "Role Simulator",
            "Evidence Engine",
            "Skills Lab",
            "Experience Map",
            "Certificates",
            "Contact"
        ],
        icons=[
            "house", "stars", "person-check", "shield-check",
            "bar-chart", "diagram-3", "award", "envelope"
        ],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#7dd3fc", "font-size": "18px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "6px 0",
                "border-radius": "14px",
                "color": "#f8fafc",
                "background-color": "rgba(15, 23, 42, 0.55)",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #0ea5e9, #7c3aed)",
                "color": "white",
                "font-weight": "800",
            },
        }
    )

    st.markdown("---")
    st.markdown("### Portfolio Mode")
    viewer_mode = st.selectbox(
        "Choose viewer lens",
        [
            "Recruiter",
            "Data Analyst Hiring Manager",
            "Business Analyst Hiring Manager",
            "ICT Business Analyst Hiring Manager",
            "AI Automation Client"
        ]
    )

    st.markdown("### Focus")
    st.markdown(
        """
        <span class="badge">Data</span>
        <span class="badge-purple">Business</span>
        <span class="badge-green">AI</span>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# COMMAND CENTER
# =========================================================

if selected == "Command Center":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <div class="eyebrow">Interactive Portfolio Dashboard</div>
                <div class="hero-title">Rubina’s Analytics Command Center</div>
                <div class="hero-subtitle">
                    A large-scale portfolio system for Data Analytics, ICT Business Analysis, Business Systems, and AI Automation.
                </div>
                <p class="hero-text">
                    This portfolio is designed like a live business intelligence product. It connects projects,
                    skills, evidence, dashboards, process thinking, automation ideas, and career-role fit into
                    one interactive command center.
                </p>
                <span class="badge">Python</span>
                <span class="badge">SQL</span>
                <span class="badge">Power BI</span>
                <span class="badge">Excel</span>
                <span class="badge-purple">Business Analysis</span>
                <span class="badge-purple">Process Mapping</span>
                <span class="badge-green">AI Automation</span>
                <span class="badge-green">LLMs</span>
                <span class="badge-green">RAG</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Portfolio Projects", len(project_df))
    m2.metric("Business Domains", project_df["domain"].nunique())
    m3.metric("Core Skills", len(skills))
    m4.metric("Career Tracks", project_df["role"].nunique())

    st.markdown('<div class="section-title">Portfolio Control Room</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 1])

    with c1:
        type_count = project_df["domain"].value_counts().reset_index()
        type_count.columns = ["Domain", "Projects"]
        fig = px.bar(
            type_count,
            x="Domain",
            y="Projects",
            color="Domain",
            title="Projects by Business Domain",
            template="plotly_dark"
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(plotly_layout(fig), use_container_width=True)

    with c2:
        status_count = project_df["status"].value_counts().reset_index()
        status_count.columns = ["Status", "Projects"]
        fig2 = px.pie(
            status_count,
            names="Status",
            values="Projects",
            title="Project Build Status",
            template="plotly_dark",
            hole=0.58
        )
        st.plotly_chart(plotly_layout(fig2), use_container_width=True)

    st.markdown('<div class="section-title">Project Roadmap</div>', unsafe_allow_html=True)

    roadmap_cols = st.columns(5)
    roadmap_items = [
        ("01", "CSR Impact Monitor", "Most personal project"),
        ("02", "RetentionLab", "Job-ready analytics"),
        ("03", "AutoFlow", "ICT BA fit"),
        ("04", "WorkforcePulse", "HR reporting"),
        ("05", "KnowledgeOps AI", "Advanced AI direction"),
    ]

    for col, item in zip(roadmap_cols, roadmap_items):
        with col:
            st.markdown(
                f"""
                <div class="glass">
                    <div class="stat-number">{item[0]}</div>
                    <h3>{item[1]}</h3>
                    <p class="small-muted">{item[2]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# PROJECT GALAXY
# =========================================================

elif selected == "Project Galaxy":
    st.markdown('<div class="section-title">Project Galaxy</div>', unsafe_allow_html=True)
    st.write("Explore all 10 projects by role, domain, status, difficulty, tools, and keyword.")

    f1, f2, f3 = st.columns(3)
    with f1:
        role_filter = st.multiselect("Role focus", sorted(project_df["role"].unique()))
    with f2:
        domain_filter = st.multiselect("Business domain", sorted(project_df["domain"].unique()))
    with f3:
        status_filter = st.multiselect("Build status", sorted(project_df["status"].unique()))

    f4, f5 = st.columns([1, 2])
    with f4:
        difficulty_filter = st.multiselect("Difficulty", sorted(project_df["difficulty"].unique()))
    with f5:
        search = st.text_input("Search", placeholder="Try AI, HR, finance, churn, CSR, SQL, Power BI")

    filtered = project_df.copy()

    if role_filter:
        filtered = filtered[filtered["role"].isin(role_filter)]
    if domain_filter:
        filtered = filtered[filtered["domain"].isin(domain_filter)]
    if status_filter:
        filtered = filtered[filtered["status"].isin(status_filter)]
    if difficulty_filter:
        filtered = filtered[filtered["difficulty"].isin(difficulty_filter)]
    if search:
        s = search.lower()
        filtered = filtered[
            filtered.apply(
                lambda row: s in str(row["name"]).lower()
                or s in str(row["full_title"]).lower()
                or s in str(row["domain"]).lower()
                or s in str(row["tools"]).lower()
                or s in str(row["problem"]).lower()
                or s in str(row["solution"]).lower(),
                axis=1
            )
        ]

    st.markdown(f"Showing **{len(filtered)}** project(s).")

    for _, project in filtered.iterrows():
        st.markdown(
            f"""
            <div class="project-card">
                <h2>{project["name"]}</h2>
                <h3>{project["full_title"]}</h3>
                <p class="subtle">{project["solution"]}</p>
                <span class="{status_badge(project["status"])}">{project["status"]}</span>
                <span class="badge-purple">{project["role"]}</span>
                <span class="badge-green">{project["domain"]}</span>
                <span class="badge-orange">{project["difficulty"]}</span>
                <br><br>
                {tags_html(project["tools"], "blue")}
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("Open project blueprint"):
            t1, t2, t3 = st.tabs(["Business Case", "Dashboard Pages", "Interview Talking Points"])

            with t1:
                st.markdown(f"**Problem:** {project['problem']}")
                st.markdown(f"**Solution:** {project['solution']}")
                st.markdown(f"**Business value:** {project['business_value']}")
                st.markdown(f"**Dataset:** {project['dataset']}")

            with t2:
                st.markdown("**Dashboard pages:**")
                for page in project["pages"]:
                    st.markdown(f"- {page}")

                st.markdown("**Core KPIs:**")
                for kpi in project["kpis"]:
                    st.markdown(f"- {kpi}")

            with t3:
                st.markdown(f"**How I would explain it:** {project['business_value']}")
                st.markdown("**Skills proved:**")
                for tool in project["tools"]:
                    st.markdown(f"- {tool}")

            st.link_button("Open GitHub Repository", project["github"])

# =========================================================
# ROLE SIMULATOR
# =========================================================

elif selected == "Role Simulator":
    st.markdown('<div class="section-title">Role Simulator</div>', unsafe_allow_html=True)
    st.write("Pick a role. The dashboard will show the most relevant projects, skills, and proof.")

    role = st.selectbox(
        "Select target role",
        [
            "Data Analyst",
            "Business Analyst",
            "ICT Business Analyst",
            "AI Automation Analyst",
            "Marketing Analyst",
            "Operations Analyst"
        ]
    )

    role_map = {
        "Data Analyst": ["Data Analyst"],
        "Business Analyst": ["Business Analyst"],
        "ICT Business Analyst": ["ICT Business Analyst"],
        "AI Automation Analyst": ["AI Automation Analyst"],
        "Marketing Analyst": ["Marketing Analyst"],
        "Operations Analyst": ["Operations Analyst"]
    }

    role_projects = project_df[project_df["role"].isin(role_map[role])]

    st.markdown(
        f"""
        <div class="control-room">
            <h2>{role} View</h2>
            <p class="subtle">
                This view highlights the projects that best support this career path.
                Use it during interviews to explain what each project proves.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    r1, r2, r3 = st.columns(3)
    r1.metric("Relevant Projects", len(role_projects))
    r2.metric("Main Proof Area", role)
    r3.metric("Portfolio Status", "Build Roadmap")

    for _, project in role_projects.iterrows():
        st.markdown(
            f"""
            <div class="project-card">
                <h2>{project["name"]}</h2>
                <p class="subtle">{project["business_value"]}</p>
                <span class="{status_badge(project["status"])}">{project["status"]}</span>
                <span class="badge-purple">{project["domain"]}</span>
                <br><br>
                {tags_html(project["tools"], "blue")}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# EVIDENCE ENGINE
# =========================================================

elif selected == "Evidence Engine":
    st.markdown('<div class="section-title">Evidence Engine</div>', unsafe_allow_html=True)
    st.write("This page connects portfolio claims with real proof. This keeps the portfolio strong and honest.")

    confidence_filter = st.multiselect(
        "Filter by confidence",
        sorted(evidence_df["confidence"].unique())
    )

    ev = evidence_df.copy()
    if confidence_filter:
        ev = ev[ev["confidence"].isin(confidence_filter)]

    for _, item in ev.iterrows():
        badge = "badge-green" if item["confidence"] == "Strong" else "badge-purple"

        st.markdown(
            f"""
            <div class="project-card">
                <h3>{item["claim"]}</h3>
                <p class="subtle"><b>Proof:</b> {item["proof"]}</p>
                <p class="subtle"><b>Source:</b> {item["source"]}</p>
                <span class="{badge}">{item["confidence"]}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    fig = px.pie(
        evidence_df,
        names="confidence",
        title="Evidence Strength",
        template="plotly_dark",
        hole=0.55
    )
    st.plotly_chart(plotly_layout(fig), use_container_width=True)

# =========================================================
# SKILLS LAB
# =========================================================

elif selected == "Skills Lab":
    st.markdown('<div class="section-title">Skills Lab</div>', unsafe_allow_html=True)

    category_filter = st.multiselect(
        "Filter skill category",
        sorted(skills["Category"].unique())
    )

    skill_view = skills.copy()
    if category_filter:
        skill_view = skill_view[skill_view["Category"].isin(category_filter)]

    tab1, tab2, tab3 = st.tabs(["Skill Cards", "Skill Chart", "Skill Table"])

    with tab1:
        rows = [skill_view.iloc[i:i+4] for i in range(0, len(skill_view), 4)]
        for row in rows:
            cols = st.columns(4)
            for col, (_, skill) in zip(cols, row.iterrows()):
                with col:
                    st.markdown(
                        f"""
                        <div class="glass">
                            <h3>{skill["Skill"]}</h3>
                            <p class="small-muted">{skill["Category"]}</p>
                            <div class="stat-number">{skill["Strength"]}%</div>
                            <div class="stat-label">Portfolio Strength</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    with tab2:
        fig = px.bar(
            skill_view,
            x="Strength",
            y="Skill",
            color="Category",
            orientation="h",
            title="Skill Strength by Category",
            template="plotly_dark",
            range_x=[0, 100]
        )
        st.plotly_chart(plotly_layout(fig), use_container_width=True)

    with tab3:
        st.dataframe(skill_view, use_container_width=True, hide_index=True)

# =========================================================
# EXPERIENCE MAP
# =========================================================

elif selected == "Experience Map":
    st.markdown('<div class="section-title">Experience Map</div>', unsafe_allow_html=True)

    for item in experience:
        st.markdown(
            f"""
            <div class="timeline">
                <h2>{item["role"]}</h2>
                <p><b>{item["company"]}</b></p>
                <p class="small-muted">{item["duration"]}</p>
                <p class="subtle">{item["details"]}</p>
                {tags_html(item["tags"], "blue")}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# CERTIFICATES
# =========================================================

elif selected == "Certificates":
    st.markdown('<div class="section-title">Certificates</div>', unsafe_allow_html=True)
    st.write("Certificates grouped around Data Analytics, AI Automation, IT, SQL, and Business Analysis.")

    cert_cols = st.columns(2)
    for idx, cert in enumerate(certifications):
        with cert_cols[idx % 2]:
            st.markdown(
                f"""
                <div class="glass">
                    <h3>{cert}</h3>
                    <p class="small-muted">Listed as a learning credential or certification on the profile.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# CONTACT
# =========================================================

elif selected == "Contact":
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <div class="eyebrow">Open to Opportunities</div>
                <div class="hero-title">Let’s connect</div>
                <p class="hero-text">
                    Open to Data Analyst, Business Analyst, ICT Business Analyst,
                    Business Systems, and AI Automation opportunities in Australia.
                </p>
                <p><b>Email:</b> rubinaahmed301@gmail.com</p>
                <p><b>LinkedIn:</b> www.linkedin.com/in/rubina-ahmed-mahar-b03b39220</p>
                <p><b>GitHub:</b> github.com/rubinaahmedmahar2002-arch</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
