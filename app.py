# requirements:
# streamlit
# pandas
# plotly
# streamlit-option-menu

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Rubina Ahmed Mahar | Business Analytics Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
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
            radial-gradient(circle at 8% 8%, rgba(37, 99, 235, 0.18), transparent 28%),
            radial-gradient(circle at 92% 8%, rgba(124, 58, 237, 0.16), transparent 28%),
            linear-gradient(135deg, #020617 0%, #07111f 48%, #0f172a 100%);
        color: #f8fafc;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
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
        border-radius: 30px;
        overflow: hidden;
        background:
            linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.80)),
            radial-gradient(circle at 88% 22%, rgba(14, 165, 233, 0.24), transparent 28%),
            radial-gradient(circle at 18% 85%, rgba(124, 58, 237, 0.20), transparent 28%);
        border: 1px solid rgba(148, 163, 184, 0.28);
        box-shadow: 0 28px 90px rgba(0,0,0,0.45);
        min-height: 390px;
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
        background: rgba(37, 99, 235, 0.15);
        border: 1px solid rgba(147, 197, 253, 0.36);
        color: #bfdbfe !important;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 0.4px;
        text-transform: uppercase;
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 58px;
        line-height: 1;
        font-weight: 900;
        letter-spacing: -2.2px;
        margin-bottom: 18px;
        background: linear-gradient(90deg, #ffffff 0%, #bfdbfe 44%, #c4b5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 22px;
        line-height: 1.45;
        max-width: 1000px;
        color: #dbeafe !important;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .hero-text, .subtle {
        font-size: 16px;
        line-height: 1.8;
        color: #cbd5e1 !important;
    }

    .section-title {
        font-size: 32px;
        font-weight: 900;
        letter-spacing: -0.8px;
        margin: 22px 0 16px 0;
        color: #ffffff !important;
    }

    .small-muted {
        color: #94a3b8 !important;
        font-size: 13px;
        line-height: 1.6;
    }

    .badge, .badge-purple, .badge-green, .badge-orange, .badge-grey {
        display: inline-block;
        padding: 8px 13px;
        margin: 5px 6px 5px 0;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
    }

    .badge {
        background: rgba(59, 130, 246, 0.14);
        border: 1px solid rgba(147, 197, 253, 0.30);
        color: #dbeafe !important;
    }

    .badge-purple {
        background: rgba(124, 58, 237, 0.16);
        border: 1px solid rgba(196, 181, 253, 0.32);
        color: #ede9fe !important;
    }

    .badge-green {
        background: rgba(22, 163, 74, 0.14);
        border: 1px solid rgba(134, 239, 172, 0.30);
        color: #dcfce7 !important;
    }

    .badge-orange {
        background: rgba(234, 88, 12, 0.14);
        border: 1px solid rgba(253, 186, 116, 0.30);
        color: #ffedd5 !important;
    }

    .badge-grey {
        background: rgba(100, 116, 139, 0.18);
        border: 1px solid rgba(203, 213, 225, 0.20);
        color: #e2e8f0 !important;
    }

    .glass {
        padding: 24px;
        border-radius: 24px;
        background: rgba(15, 23, 42, 0.76);
        border: 1px solid rgba(148, 163, 184, 0.23);
        box-shadow: 0 16px 45px rgba(0,0,0,0.26);
        height: 100%;
    }

    .glass:hover {
        transform: translateY(-4px);
        border-color: rgba(125, 211, 252, 0.50);
        transition: all 0.22s ease;
    }

    .project-card {
        padding: 26px;
        border-radius: 26px;
        background:
            linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.84));
        border: 1px solid rgba(148, 163, 184, 0.24);
        box-shadow: 0 22px 58px rgba(0,0,0,0.32);
        margin-bottom: 18px;
    }

    .project-card:hover {
        transform: translateY(-3px);
        border-color: rgba(125, 211, 252, 0.50);
        transition: all 0.22s ease;
    }

    .timeline {
        padding: 20px 24px;
        border-left: 4px solid rgba(56, 189, 248, 0.85);
        margin-bottom: 18px;
        background: rgba(15, 23, 42, 0.74);
        border-radius: 20px;
        border: 1px solid rgba(148, 163, 184, 0.20);
        box-shadow: 0 16px 45px rgba(0,0,0,0.24);
    }

    .info-panel {
        padding: 26px;
        border-radius: 28px;
        background:
            radial-gradient(circle at 15% 15%, rgba(14, 165, 233, 0.18), transparent 25%),
            radial-gradient(circle at 82% 18%, rgba(124, 58, 237, 0.18), transparent 28%),
            rgba(15, 23, 42, 0.84);
        border: 1px solid rgba(148, 163, 184, 0.26);
        box-shadow: 0 24px 64px rgba(0,0,0,0.34);
    }

    .stat-number {
        font-size: 34px;
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
        box-shadow: 0 16px 38px rgba(0,0,0,0.26);
    }

    div[data-testid="stMetric"] label {
        color: #cbd5e1 !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-weight: 900 !important;
    }

    /* Dropdown, multiselect, and text input visibility fix */
    .stSelectbox label, .stMultiSelect label, .stTextInput label {
        color: #f8fafc !important;
        font-weight: 800 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] span {
        color: #020617 !important;
        font-weight: 650 !important;
    }

    div[data-baseweb="select"] svg {
        fill: #020617 !important;
    }

    div[role="listbox"] {
        background-color: #ffffff !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 12px !important;
    }

    div[role="listbox"] * {
        color: #020617 !important;
        background-color: #ffffff !important;
    }

    div[role="option"] {
        color: #020617 !important;
        background-color: #ffffff !important;
    }

    div[role="option"]:hover {
        background-color: #dbeafe !important;
        color: #020617 !important;
    }

    .stTextInput input {
        background-color: #ffffff !important;
        color: #020617 !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 12px !important;
    }

    .stTextInput input::placeholder {
        color: #475569 !important;
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
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.34), rgba(124, 58, 237, 0.34));
        border-color: rgba(125, 211, 252, 0.58);
    }

    a {
        color: #93c5fd !important;
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
        "name": "Business Process Automation Dashboard",
        "short_name": "Process Automation",
        "domain": "Business Process Automation",
        "role": "ICT Business Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Synthetic workflow dataset",
        "tools": ["Python", "SQL", "Power BI", "Process Mapping", "AI Recommendations"],
        "problem": "Manual workflows hide bottlenecks, errors, rework, and avoidable cost.",
        "solution": "Compare manual steps with automation-ready workflows and identify improvement opportunities.",
        "business_value": "Supports automation priority, time savings, error reduction, and cost control.",
        "pages": ["Executive Overview", "Process Flow", "Automation Impact", "Recommendations"],
        "kpis": ["Total cases", "Average processing time", "Manual hours saved", "Error rate", "Estimated cost savings"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Customer Churn and Retention Dashboard",
        "short_name": "Customer Retention",
        "domain": "Customer Analytics",
        "role": "Data Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Synthetic customer dataset",
        "tools": ["Python", "SQL", "Machine Learning", "Power BI", "Customer Segmentation"],
        "problem": "Businesses lose revenue when they do not identify at-risk customers early.",
        "solution": "Build churn risk scores, customer segments, and retention action recommendations.",
        "business_value": "Helps prioritise retention campaigns, protect revenue, and understand churn drivers.",
        "pages": ["Churn Overview", "Customer Segments", "Churn Drivers", "Action Plan"],
        "kpis": ["Churn rate", "Revenue at risk", "High-risk customers", "Retention opportunity value"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Marketing ROI and Campaign Performance Dashboard",
        "short_name": "Marketing Performance",
        "domain": "Marketing Analytics",
        "role": "Marketing Analyst",
        "status": "Planned",
        "difficulty": "Intermediate",
        "dataset": "Synthetic campaign data or public business data",
        "tools": ["Power BI", "Excel", "SQL", "Funnel Analysis", "ROI Analysis"],
        "problem": "Marketing teams need to know which campaigns and channels generate profitable outcomes.",
        "solution": "Analyze channel spend, conversions, revenue, profitability, and budget allocation.",
        "business_value": "Improves marketing budget decisions and connects campaigns with sales outcomes.",
        "pages": ["Campaign Overview", "Channel Performance", "Customer Funnel", "Budget Optimizer"],
        "kpis": ["Total spend", "Revenue", "ROAS", "Conversion rate", "CPA"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "HR Workforce and Attrition Dashboard",
        "short_name": "HR Analytics",
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
        "name": "Financial Performance and Cash Flow Dashboard",
        "short_name": "Financial Analytics",
        "domain": "Financial Analytics",
        "role": "Business Analyst",
        "status": "Planned",
        "difficulty": "Intermediate",
        "dataset": "Simulated financial dataset",
        "tools": ["Excel", "Power BI", "SQL", "Variance Analysis", "Accounting"],
        "problem": "Managers need to understand revenue, expenses, profit, cash flow, and budget variance.",
        "solution": "Create a finance dashboard that explains performance movement and cost control areas.",
        "business_value": "Connects accounting data with executive decision-making and budget control.",
        "pages": ["Financial Overview", "Revenue Analysis", "Expense and Budget Control", "Cash Flow"],
        "kpis": ["Revenue", "Gross profit", "Net profit", "Operating expenses", "Cash balance"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Public City Data for Small Business Dashboard",
        "short_name": "City Business Insights",
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
        "name": "AI Resume Screening and Recruitment Dashboard",
        "short_name": "Recruitment Analytics",
        "domain": "AI and HR Systems",
        "role": "ICT Business Analyst",
        "status": "Planned",
        "difficulty": "Advanced",
        "dataset": "Sample candidate dataset",
        "tools": ["Python", "NLP", "AI Automation", "Power BI", "Responsible AI"],
        "problem": "Recruitment teams need faster screening, but AI systems must stay transparent and fair.",
        "solution": "Build a candidate matching dashboard with skill extraction, pipeline analytics, and fairness checks.",
        "business_value": "Improves hiring pipeline visibility while keeping human review and responsible AI in the process.",
        "pages": ["Recruitment Overview", "Candidate Match", "Pipeline Analytics", "Fairness Check"],
        "kpis": ["Applicants", "Shortlisted candidates", "Average match score", "Hiring funnel conversion"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Supply Chain and Inventory Dashboard",
        "short_name": "Inventory Analytics",
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
        "name": "CSR Project Monitoring and Impact Dashboard",
        "short_name": "CSR Impact",
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
        "name": "RAG-Based Business Knowledge Assistant",
        "short_name": "Business Knowledge Assistant",
        "domain": "AI Automation",
        "role": "AI Automation Analyst",
        "status": "Planned",
        "difficulty": "Advanced Prototype",
        "dataset": "Sample company documents",
        "tools": ["Python", "LLMs", "RAG", "APIs", "Vector Databases", "Dashboard Monitoring"],
        "problem": "Business teams waste time searching policies, SOPs, reports, and project documents.",
        "solution": "Build a RAG assistant prototype that answers questions from sample business documents and tracks answer quality.",
        "business_value": "Improves knowledge access, document coverage, unresolved question tracking, and human review workflows.",
        "pages": ["Assistant Overview", "Document Knowledge Base", "Query Analytics", "Quality and Risk"],
        "kpis": ["Questions asked", "Answer success rate", "Response time", "Documents searched", "Unanswered questions"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    }
]

experience = [
    {
        "role": "Data Analyst",
        "company": "A. F. Ferguson & Co. | PwC Network",
        "duration": "Sep 2025 - Dec 2025",
        "location": "Pakistan",
        "details": "Prepared, cleaned, and structured multi-source datasets for KPI tracking, HR reporting, payroll data accuracy, and operational analysis. Supported Excel and SQL reporting workflows, built dashboards and analytical summaries, and conducted data validation checks.",
        "tags": ["Data Cleaning", "KPI Reporting", "SQL", "Excel", "Dashboards", "Data Validation"]
    },
    {
        "role": "Community Development Intern",
        "company": "Pakistan Petroleum Limited",
        "duration": "Jul 2025 - Aug 2025",
        "location": "Karachi, Pakistan",
        "details": "Supported CSR and community development projects across education, health, water supply, and welfare initiatives. Prepared Excel-based budget sheets, cost estimates, operational records, project trackers, documentation packs, and stakeholder follow-up records.",
        "tags": ["CSR", "Budgeting", "Documentation", "Stakeholder Coordination", "Reporting", "Project Tracking"]
    },
    {
        "role": "Quality Assurance Analyst",
        "company": "Oigetit Real-Time AI Intelligence Platform",
        "duration": "Aug 2024 - Nov 2024",
        "location": "Remote",
        "details": "Tested web-based product features, identified bugs, reviewed content quality, monitored RSS feeds, documented defects, and supported product improvement in a remote agile environment.",
        "tags": ["QA", "Testing", "AI Platform", "Issue Tracking", "Workflow Review", "Content Quality"]
    },
    {
        "role": "Data Science Intern",
        "company": "Prodigy InfoTech",
        "duration": "Jun 2024 - Aug 2024",
        "location": "Remote",
        "details": "Completed project-based data science tasks involving data cleaning, exploratory data analysis, visualization, and basic predictive modeling using Python.",
        "tags": ["Python", "EDA", "Visualization", "Machine Learning", "Pandas", "NumPy"]
    },
    {
        "role": "Data Science and AI Intern",
        "company": "SYNC INTERN'S",
        "duration": "Mar 2024 - Apr 2024",
        "location": "Remote",
        "details": "Completed hands-on analytics and AI tasks involving data preparation, customer analysis, experimentation, and business-focused data interpretation.",
        "tags": ["AI", "Customer Analysis", "Experimentation", "Analytics", "Business Interpretation"]
    },
    {
        "role": "Marketing Intern",
        "company": "AI DataYard",
        "duration": "Oct 2023 - Dec 2023",
        "location": "Remote",
        "details": "Created digital content to support online visibility, brand awareness, and AI service positioning. Supported social media engagement, content planning, and digital communication.",
        "tags": ["Digital Marketing", "Content Strategy", "AI Services", "Brand Awareness", "Communication"]
    },
    {
        "role": "Campus Ambassador",
        "company": "Paklaunch",
        "duration": "Jun 2023 - Sep 2023",
        "location": "Remote",
        "details": "Promoted initiatives through digital outreach, student engagement, event promotion, and community-building activities focused on entrepreneurship and professional development.",
        "tags": ["Community Engagement", "Outreach", "Event Promotion", "Public Speaking", "Communication"]
    },
    {
        "role": "Business Development Intern",
        "company": "GAOTek Inc.",
        "duration": "Jun 2023 - Sep 2023",
        "location": "Remote",
        "details": "Conducted market research, lead generation, competitive analysis, market mapping, and research on potential clients and industry segments.",
        "tags": ["Market Research", "Lead Generation", "Competitive Analysis", "Business Development", "Client Research"]
    }
]

certifications = [
    {"name": "Complete Data Analyst Bootcamp From Basics To Advanced", "issuer": "Udemy", "category": "Data Analytics"},
    {"name": "Complete N8N and AI Automation Masterclass", "issuer": "Udemy", "category": "AI Automation"},
    {"name": "IT System Engineer and Cloud System Administration", "issuer": "Udemy", "category": "IT and Cloud"},
    {"name": "IT Support Entry Level Job Training Course", "issuer": "Udemy", "category": "IT Support"},
    {"name": "AI Automation: Build LLM Apps and AI Agents with n8n and APIs", "issuer": "Udemy", "category": "AI Automation"},
    {"name": "The Complete AI Agents and AI Automation Course", "issuer": "Udemy", "category": "AI Automation"},
    {"name": "Become an IT Business Analyst: Learn, Apply, Succeed", "issuer": "Udemy", "category": "Business Analysis"},
    {"name": "Data and Programming Foundations for AI Skill Path", "issuer": "Codecademy", "category": "AI and Programming"},
    {"name": "Introduction to Artificial Intelligence", "issuer": "IBM", "category": "Artificial Intelligence"},
    {"name": "SQL for Data Science", "issuer": "University of California, Davis", "category": "SQL"},
    {"name": "CompTIA Data+", "issuer": "CompTIA", "category": "Data Analytics"},
    {"name": "Google Data Analytics", "issuer": "Google", "category": "Data Analytics"},
    {"name": "CS50 Python", "issuer": "Harvard / CS50", "category": "Python"},
    {"name": "Python 101", "issuer": "IBM", "category": "Python"},
    {"name": "Intermediate SQL", "issuer": "DataCamp", "category": "SQL"},
    {"name": "MySQL", "issuer": "Analyst Builder", "category": "SQL"},
    {"name": "PostgreSQL", "issuer": "Codecademy", "category": "SQL"},
    {"name": "Excel for Business Analysts", "issuer": "Online Course", "category": "Excel"},
    {"name": "Data Analyst Associate", "issuer": "Online Course", "category": "Data Analytics"},
    {"name": "Power BI Desktop", "issuer": "Online Course", "category": "Power BI"}
]

skills = [
    {"Skill": "Python", "Category": "Data Analytics", "Strength": 76},
    {"Skill": "SQL", "Category": "Data Analytics", "Strength": 70},
    {"Skill": "Power BI", "Category": "Dashboarding", "Strength": 74},
    {"Skill": "Excel", "Category": "Business Reporting", "Strength": 86},
    {"Skill": "DAX", "Category": "Dashboarding", "Strength": 58},
    {"Skill": "Pandas", "Category": "Data Analytics", "Strength": 78},
    {"Skill": "Scikit-learn", "Category": "Machine Learning", "Strength": 63},
    {"Skill": "Business Analysis", "Category": "Business Analysis", "Strength": 80},
    {"Skill": "Process Mapping", "Category": "Business Analysis", "Strength": 78},
    {"Skill": "Data Cleaning", "Category": "Data Quality", "Strength": 82},
    {"Skill": "KPI Reporting", "Category": "Business Reporting", "Strength": 78},
    {"Skill": "Financial Analysis", "Category": "Finance Analytics", "Strength": 68},
    {"Skill": "HR Analytics", "Category": "HR Analytics", "Strength": 70},
    {"Skill": "Marketing Analytics", "Category": "Marketing Analytics", "Strength": 66},
    {"Skill": "Customer Analytics", "Category": "Customer Analytics", "Strength": 68},
    {"Skill": "CSR Analytics", "Category": "CSR Analytics", "Strength": 82},
    {"Skill": "Inventory Analytics", "Category": "Operations Analytics", "Strength": 60},
    {"Skill": "AI Automation", "Category": "AI Automation", "Strength": 58},
    {"Skill": "LLM Tools", "Category": "AI Automation", "Strength": 52},
    {"Skill": "RAG Concepts", "Category": "AI Automation", "Strength": 48},
    {"Skill": "APIs", "Category": "AI Automation", "Strength": 50},
    {"Skill": "Stakeholder Reporting", "Category": "Business Analysis", "Strength": 84},
    {"Skill": "Documentation", "Category": "Business Analysis", "Strength": 86}
]

evidence = [
    {
        "claim": "Data cleaning and business reporting",
        "proof": "Prepared and structured multi-source datasets for reporting and KPI tracking.",
        "source": "A. F. Ferguson Data Analyst role",
        "confidence": "Strong"
    },
    {
        "claim": "Dashboard and KPI reporting",
        "proof": "Built HR dashboard work and analytical summaries for management-style reporting.",
        "source": "HR Analytics, A. F. Ferguson role",
        "confidence": "Strong"
    },
    {
        "claim": "Business process documentation",
        "proof": "Created CSR trackers, documentation packs, budget sheets, and status records.",
        "source": "Pakistan Petroleum Limited internship",
        "confidence": "Strong"
    },
    {
        "claim": "Machine learning for business use cases",
        "proof": "Built prediction and modeling projects using Python, Linear Regression, Random Forest, and classification workflows.",
        "source": "Portfolio ML projects",
        "confidence": "Developing"
    },
    {
        "claim": "AI automation capability",
        "proof": "Learning n8n, APIs, LLM workflows, RAG concepts, and AI automation dashboards.",
        "source": "Certifications and planned AI project",
        "confidence": "Developing"
    }
]

education = [
    {
        "degree": "MBA Global / Master of Science in Data Analytics",
        "institution": "University of Newcastle",
        "location": "Australia",
        "status": "Current"
    },
    {
        "degree": "BBA Honors",
        "institution": "Iqra University",
        "location": "Pakistan",
        "status": "Completed"
    }
]

project_df = pd.DataFrame(projects)
experience_df = pd.DataFrame(experience)
cert_df = pd.DataFrame(certifications)
skills_df = pd.DataFrame(skills)
evidence_df = pd.DataFrame(evidence)
education_df = pd.DataFrame(education)

# =========================================================
# HELPERS
# =========================================================

def tags_html(tags, color="blue"):
    klass = {
        "blue": "badge",
        "purple": "badge-purple",
        "green": "badge-green",
        "orange": "badge-orange",
        "grey": "badge-grey"
    }.get(color, "badge")
    return "".join([f'<span class="{klass}">{tag}</span>' for tag in tags])

def status_badge(status):
    if status == "Completed":
        return "badge-green"
    if status == "In Progress":
        return "badge-orange"
    if status == "Prototype":
        return "badge-purple"
    if status == "Planned":
        return "badge-grey"
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
    st.markdown("### Rubina Ahmed Mahar")
    st.caption("Business Analytics Portfolio")

    selected = option_menu(
        menu_title=None,
        options=[
            "Overview",
            "Projects",
            "Role Match",
            "Evidence",
            "Skills",
            "Experience",
            "Certifications",
            "Education",
            "Contact"
        ],
        icons=[
            "house", "grid", "person-check", "shield-check",
            "bar-chart", "briefcase", "award", "mortarboard", "envelope"
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
                "background": "linear-gradient(135deg, #2563eb, #7c3aed)",
                "color": "white",
                "font-weight": "800",
            },
        }
    )

    st.markdown("---")
    st.markdown("### Viewer Mode")
    viewer_mode = st.selectbox(
        "Select viewer type",
        [
            "Recruiter",
            "Data Analyst Hiring Manager",
            "Business Analyst Hiring Manager",
            "ICT Business Analyst Hiring Manager",
            "AI Automation Client"
        ]
    )

    st.markdown("### Focus Areas")
    st.markdown(
        """
        <span class="badge">Data Analytics</span>
        <span class="badge-purple">Business Analysis</span>
        <span class="badge-green">AI Automation</span>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# OVERVIEW
# =========================================================

if selected == "Overview":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <div class="eyebrow">Interactive Portfolio</div>
                <div class="hero-title">Business Analytics Portfolio</div>
                <div class="hero-subtitle">
                    Data Analytics, ICT Business Analysis, Dashboard Reporting, and AI Automation projects.
                </div>
                <p class="hero-text">
                    This portfolio brings together completed work, in-progress builds, and planned case studies.
                    Each project is designed around a practical business problem, with clear dashboards, KPIs,
                    tools, business value, and role alignment.
                </p>
                <span class="badge">Python</span>
                <span class="badge">SQL</span>
                <span class="badge">Power BI</span>
                <span class="badge">Excel</span>
                <span class="badge-purple">Business Analysis</span>
                <span class="badge-purple">Process Mapping</span>
                <span class="badge-green">AI Automation</span>
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
    m3.metric("Experience Roles", len(experience_df))
    m4.metric("Certifications", len(cert_df))

    st.markdown('<div class="section-title">Portfolio Summary</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 1])

    with c1:
        domain_count = project_df["domain"].value_counts().reset_index()
        domain_count.columns = ["Domain", "Projects"]
        fig = px.bar(
            domain_count,
            x="Domain",
            y="Projects",
            color="Domain",
            title="Projects by Domain",
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
            title="Project Status",
            template="plotly_dark",
            hole=0.58
        )
        st.plotly_chart(plotly_layout(fig2), use_container_width=True)

    st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

    featured_names = ["CSR Impact", "Customer Retention", "Process Automation", "HR Analytics"]
    featured = project_df[project_df["short_name"].isin(featured_names)]

    cols = st.columns(4)

    for col, (_, project) in zip(cols, featured.iterrows()):
        with col:
            st.markdown(
                f"""
                <div class="glass">
                    <h3>{project["short_name"]}</h3>
                    <p class="small-muted">{project["domain"]}</p>
                    <p class="subtle">{project["business_value"]}</p>
                    <span class="{status_badge(project["status"])}">{project["status"]}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# PROJECTS
# =========================================================

elif selected == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    st.write("Filter projects by role, domain, status, difficulty, or keyword.")

    f1, f2, f3 = st.columns(3)
    with f1:
        role_filter = st.multiselect("Role focus", sorted(project_df["role"].unique()))
    with f2:
        domain_filter = st.multiselect("Business domain", sorted(project_df["domain"].unique()))
    with f3:
        status_filter = st.multiselect("Project status", sorted(project_df["status"].unique()))

    f4, f5 = st.columns([1, 2])
    with f4:
        difficulty_filter = st.multiselect("Difficulty", sorted(project_df["difficulty"].unique()))
    with f5:
        search = st.text_input("Search projects", placeholder="Try AI, HR, finance, churn, CSR, SQL, Power BI")

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
                lambda row:
                s in str(row["name"]).lower()
                or s in str(row["short_name"]).lower()
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

        with st.expander("View project details"):
            t1, t2, t3 = st.tabs(["Business Case", "Dashboard Plan", "Interview Notes"])

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
                st.markdown(f"**How to explain it:** {project['business_value']}")
                st.markdown("**Skills shown:**")
                for tool in project["tools"]:
                    st.markdown(f"- {tool}")

            st.link_button("Open GitHub Repository", project["github"])

# =========================================================
# ROLE MATCH
# =========================================================

elif selected == "Role Match":
    st.markdown('<div class="section-title">Role Match</div>', unsafe_allow_html=True)
    st.write("Select a target role to see the most relevant portfolio projects.")

    role = st.selectbox(
        "Target role",
        [
            "Data Analyst",
            "Business Analyst",
            "ICT Business Analyst",
            "AI Automation Analyst",
            "Marketing Analyst",
            "Operations Analyst"
        ]
    )

    role_projects = project_df[project_df["role"] == role]

    st.markdown(
        f"""
        <div class="info-panel">
            <h2>{role}</h2>
            <p class="subtle">
                This section shows the projects that best match the selected role.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    r1, r2, r3 = st.columns(3)
    r1.metric("Matching Projects", len(role_projects))
    r2.metric("Main Role", role)
    r3.metric("Portfolio Type", "Case Study Based")

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
# EVIDENCE
# =========================================================

elif selected == "Evidence":
    st.markdown('<div class="section-title">Evidence</div>', unsafe_allow_html=True)
    st.write("This page connects portfolio claims with real proof from experience, projects, or learning.")

    confidence_filter = st.multiselect(
        "Confidence level",
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
# SKILLS
# =========================================================

elif selected == "Skills":
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

    category_filter = st.multiselect(
        "Skill category",
        sorted(skills_df["Category"].unique())
    )

    skill_view = skills_df.copy()

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
# EXPERIENCE
# =========================================================

elif selected == "Experience":
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

    for item in experience:
        st.markdown(
            f"""
            <div class="timeline">
                <h2>{item["role"]}</h2>
                <p><b>{item["company"]}</b></p>
                <p class="small-muted">{item["duration"]} | {item["location"]}</p>
                <p class="subtle">{item["details"]}</p>
                {tags_html(item["tags"], "blue")}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# CERTIFICATIONS
# =========================================================

elif selected == "Certifications":
    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

    cert_category = st.multiselect(
        "Certification category",
        sorted(cert_df["category"].unique())
    )

    issuer_filter = st.multiselect(
        "Issuer",
        sorted(cert_df["issuer"].unique())
    )

    cert_view = cert_df.copy()

    if cert_category:
        cert_view = cert_view[cert_view["category"].isin(cert_category)]

    if issuer_filter:
        cert_view = cert_view[cert_view["issuer"].isin(issuer_filter)]

    c1, c2 = st.columns([1.1, 1])

    with c1:
        fig = px.bar(
            cert_df["category"].value_counts().reset_index(),
            x="category",
            y="count",
            color="category",
            title="Certifications by Category",
            template="plotly_dark"
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(plotly_layout(fig), use_container_width=True)

    with c2:
        fig2 = px.pie(
            cert_df,
            names="issuer",
            title="Certifications by Issuer",
            template="plotly_dark",
            hole=0.55
        )
        st.plotly_chart(plotly_layout(fig2), use_container_width=True)

    st.markdown(f"Showing **{len(cert_view)}** certification(s).")

    rows = [cert_view.iloc[i:i+2] for i in range(0, len(cert_view), 2)]

    for row in rows:
        cols = st.columns(2)

        for col, (_, cert) in zip(cols, row.iterrows()):
            with col:
                st.markdown(
                    f"""
                    <div class="glass">
                        <h3>{cert["name"]}</h3>
                        <p class="small-muted">{cert["issuer"]}</p>
                        <span class="badge-purple">{cert["category"]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# =========================================================
# EDUCATION
# =========================================================

elif selected == "Education":
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

    for _, item in education_df.iterrows():
        st.markdown(
            f"""
            <div class="project-card">
                <h2>{item["degree"]}</h2>
                <p><b>{item["institution"]}</b></p>
                <p class="small-muted">{item["location"]}</p>
                <span class="badge-green">{item["status"]}</span>
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
                <div class="hero-title">Let’s Connect</div>
                <p class="hero-text">
                    Open to Data Analyst, Business Analyst, ICT Business Analyst,
                    Business Systems, and AI Automation opportunities.
                </p>
                <p><b>Email:</b> rubinaahmed301@gmail.com</p>
                <p><b>LinkedIn:</b> www.linkedin.com/in/rubina-ahmed-mahar-b03b39220</p>
                <p><b>GitHub:</b> github.com/rubinaahmedmahar2002-arch</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
