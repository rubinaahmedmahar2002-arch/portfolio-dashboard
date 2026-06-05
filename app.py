import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# =========================================================
# PAGE CONFIG
# =========================================================

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

    [data-testid="stHeader"] {
        background: rgba(2, 6, 23, 0.95) !important;
        border-bottom: 1px solid rgba(148, 163, 184, 0.18) !important;
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

    .stSelectbox label,
    .stMultiSelect label,
    .stTextInput label,
    .stSlider label {
        color: #f8fafc !important;
        font-weight: 800 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #0f172a !important;
        border: 1.5px solid #38bdf8 !important;
        border-radius: 12px !important;
        min-height: 46px !important;
    }

    div[data-baseweb="select"] * {
        color: #f8fafc !important;
        opacity: 1 !important;
    }

    div[data-baseweb="select"] svg {
        fill: #f8fafc !important;
        color: #f8fafc !important;
    }

    div[data-baseweb="popover"],
    div[data-baseweb="popover"] * {
        background-color: #0f172a !important;
        color: #f8fafc !important;
        opacity: 1 !important;
    }

    ul[role="listbox"] {
        background-color: #0f172a !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 12px !important;
        padding: 6px !important;
    }

    ul[role="listbox"] li,
    div[role="option"],
    li[role="option"] {
        background-color: #0f172a !important;
        color: #f8fafc !important;
        opacity: 1 !important;
        font-weight: 650 !important;
    }

    ul[role="listbox"] li:hover,
    div[role="option"]:hover,
    li[role="option"]:hover {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }

    div[role="option"][aria-selected="true"],
    li[role="option"][aria-selected="true"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    div[data-baseweb="tag"] {
        background-color: #1e40af !important;
        border: 1px solid #60a5fa !important;
    }

    div[data-baseweb="tag"] span {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    .stTextInput input {
        background-color: #0f172a !important;
        color: #f8fafc !important;
        border: 1.5px solid #38bdf8 !important;
        border-radius: 12px !important;
        min-height: 46px !important;
        font-weight: 650 !important;
    }

    .stTextInput input::placeholder {
        color: #cbd5e1 !important;
        opacity: 1 !important;
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
# PROJECT DATA
# =========================================================

projects = [
    {
        "name": "AI-Powered Global Data and AI Job Market Intelligence",
        "short_name": "AI Job Market",
        "domain": "Data Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Advanced",
        "dataset": "Global data and AI job market dataset",
        "tools": ["Python", "Pandas", "Scikit-learn", "Matplotlib", "Machine Learning"],
        "problem": "Students and early-career professionals need to understand job market trends, salaries, and skill demand in data and AI roles.",
        "solution": "Analyze global job market patterns and build salary prediction models using machine learning.",
        "business_value": "Turns job market data into career planning, salary insight, and role-demand intelligence.",
        "pages": ["Market Overview", "Salary Analysis", "Role and Skill Trends", "Prediction Model", "Recommendations"],
        "kpis": ["Average salary", "Top roles", "Top skills", "Salary by region", "Model performance"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "HR Analytics Dashboard using Power BI",
        "short_name": "HR Analytics",
        "domain": "HR Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Intermediate",
        "dataset": "HR analytics sample dataset",
        "tools": ["Power BI", "Excel", "HR Metrics", "Dashboard Design", "Data Cleaning"],
        "problem": "HR teams need clear visibility into employee structure, attrition, hiring, and workforce metrics.",
        "solution": "Build a Power BI dashboard to analyse workforce demographics, department metrics, and employee trends.",
        "business_value": "Supports HR reporting, workforce planning, and management decision-making.",
        "pages": ["Workforce Overview", "Attrition Analysis", "Department View", "Employee Insights"],
        "kpis": ["Total employees", "Attrition rate", "Average salary", "Average tenure", "Department headcount"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Project Management Tracker using Microsoft Excel",
        "short_name": "Project Tracker",
        "domain": "Business Reporting",
        "role": "Business Analyst",
        "status": "Completed",
        "difficulty": "Intermediate",
        "dataset": "Project tracking workbook",
        "tools": ["Excel", "Project Tracking", "Status Reporting", "Data Validation", "Conditional Formatting"],
        "problem": "Managers need a simple way to track project status, owners, timelines, delays, and completion progress.",
        "solution": "Create an Excel-based tracker for project monitoring, task ownership, deadlines, and reporting.",
        "business_value": "Improves project visibility, follow-up, accountability, and reporting discipline.",
        "pages": ["Project Overview", "Task Tracker", "Status Summary", "Risk and Delay View"],
        "kpis": ["Total tasks", "Completed tasks", "Delayed tasks", "Pending tasks", "Completion rate"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Python for Data Analysis: Pandas and NumPy",
        "short_name": "Python Data Analysis",
        "domain": "Data Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Foundation",
        "dataset": "Python practice datasets",
        "tools": ["Python", "Pandas", "NumPy", "Data Cleaning", "EDA"],
        "problem": "Raw data needs cleaning, exploration, and transformation before analysis.",
        "solution": "Use Pandas and NumPy to clean, reshape, summarise, and explore structured datasets.",
        "business_value": "Builds the foundation for practical analytics workflows and data preparation.",
        "pages": ["Data Loading", "Data Cleaning", "Feature Summary", "Exploratory Analysis"],
        "kpis": ["Rows cleaned", "Missing values", "Duplicate records", "Feature count", "Summary metrics"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Exploratory Data Analysis of Global Suicide Rates",
        "short_name": "Global Suicide EDA",
        "domain": "Public Health Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Intermediate",
        "dataset": "Global suicide rates dataset",
        "tools": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn"],
        "problem": "Public health datasets need clear visual analysis to identify vulnerable regions, groups, and trends.",
        "solution": "Analyze suicide rates across countries, years, age groups, gender, and socioeconomic indicators.",
        "business_value": "Supports public health storytelling, policy awareness, and evidence-based discussion.",
        "pages": ["Global Overview", "Country Trends", "Age and Gender Analysis", "Risk Pattern View"],
        "kpis": ["Suicide rate", "Country ranking", "Age group risk", "Gender comparison", "Trend movement"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Global Mental Health Data Analysis and Modeling",
        "short_name": "Mental Health Analytics",
        "domain": "Public Health Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Advanced",
        "dataset": "Global mental health dataset",
        "tools": ["Python", "Pandas", "Visualization", "Scikit-learn", "Modeling"],
        "problem": "Mental health indicators need structured analysis to reveal patterns across countries and populations.",
        "solution": "Analyze mental health indicators and apply basic modeling to understand trends and relationships.",
        "business_value": "Turns public health data into interpretable insights and research-style analytics.",
        "pages": ["Mental Health Overview", "Country Comparison", "Trend Analysis", "Modeling Summary"],
        "kpis": ["Indicator rate", "Country average", "Trend change", "Model score", "Risk pattern"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Heart Attack Analysis and Prediction",
        "short_name": "Heart Risk Prediction",
        "domain": "Healthcare Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Advanced",
        "dataset": "Heart attack risk dataset",
        "tools": ["Python", "Pandas", "Scikit-learn", "Classification", "EDA"],
        "problem": "Healthcare datasets need interpretable analysis to understand patient risk patterns.",
        "solution": "Analyze health indicators and build prediction-focused classification models.",
        "business_value": "Shows healthcare analytics, risk analysis, feature interpretation, and predictive modeling.",
        "pages": ["Health Overview", "Risk Factors", "Model Results", "Feature Analysis"],
        "kpis": ["Accuracy", "Risk class", "Feature impact", "Patient count", "Prediction score"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Water Quality Exploratory Data Analysis",
        "short_name": "Water Quality EDA",
        "domain": "Environmental Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Intermediate",
        "dataset": "Water quality dataset",
        "tools": ["Python", "Pandas", "Matplotlib", "EDA", "Data Quality Checks"],
        "problem": "Environmental data needs quality checks and trend analysis before it can support decisions.",
        "solution": "Explore water quality indicators, missing values, trends, and safety-related variables.",
        "business_value": "Demonstrates environmental analytics, public data interpretation, and data quality thinking.",
        "pages": ["Water Quality Overview", "Missing Values", "Indicator Trends", "Safety Summary"],
        "kpis": ["Quality score", "Missing values", "Indicator average", "Risk level", "Trend change"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Spotify User Behaviour and Pattern Recognition",
        "short_name": "Spotify User Analytics",
        "domain": "Customer Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Advanced",
        "dataset": "Spotify user behaviour dataset",
        "tools": ["Python", "Pandas", "Machine Learning", "Pattern Recognition", "EDA"],
        "problem": "Digital platforms need to understand user behaviour, engagement, and listening patterns.",
        "solution": "Analyze Spotify user behaviour and identify pattern groups using analytics and ML techniques.",
        "business_value": "Shows customer behaviour analysis, segmentation thinking, and product analytics.",
        "pages": ["User Overview", "Listening Patterns", "Segment Analysis", "Engagement Insights"],
        "kpis": ["Listening frequency", "User segment", "Engagement score", "Top pattern", "Cluster count"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Netflix Data Analytics Project",
        "short_name": "Netflix Analytics",
        "domain": "Content Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Intermediate",
        "dataset": "Netflix titles dataset",
        "tools": ["Python", "Pandas", "Visualization", "Content Analytics", "EDA"],
        "problem": "Streaming platforms need to understand content mix, genre trends, country contribution, and audience catalogue patterns.",
        "solution": "Analyze Netflix titles by genre, country, release year, duration, and content type.",
        "business_value": "Shows entertainment analytics and business storytelling through content data.",
        "pages": ["Catalogue Overview", "Country Analysis", "Genre Trends", "Duration and Release Patterns"],
        "kpis": ["Total titles", "Movie count", "TV show count", "Top countries", "Top genres"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Youth Job Opportunities Around the World",
        "short_name": "Youth Jobs Analytics",
        "domain": "Labour Market Analytics",
        "role": "Data Analyst",
        "status": "Completed",
        "difficulty": "Intermediate",
        "dataset": "Global youth job opportunity indicators",
        "tools": ["Python", "Pandas", "Scoring Model", "Visualization", "Business Storytelling"],
        "problem": "Young professionals need a structured way to compare job opportunity conditions across countries.",
        "solution": "Create a scoring system to compare countries based on employment and opportunity indicators.",
        "business_value": "Shows labour market analysis, index building, and decision-support thinking.",
        "pages": ["Country Ranking", "Opportunity Score", "Regional View", "Recommendation Summary"],
        "kpis": ["Opportunity score", "Country rank", "Employment indicator", "Risk level", "Recommendation"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Creating Financial Statements using Microsoft Excel",
        "short_name": "Financial Statements",
        "domain": "Financial Analytics",
        "role": "Business Analyst",
        "status": "Completed",
        "difficulty": "Foundation",
        "dataset": "Accounting and financial statement workbook",
        "tools": ["Excel", "Accounting", "Financial Statements", "Formulas", "Reporting"],
        "problem": "Businesses need structured financial statements to understand financial position and performance.",
        "solution": "Prepare financial statement formats and calculations using Excel.",
        "business_value": "Shows accounting knowledge, Excel reporting, and finance data structuring.",
        "pages": ["Income Statement", "Balance Sheet", "Cash Flow", "Summary"],
        "kpis": ["Revenue", "Expenses", "Profit", "Assets", "Liabilities"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Medical Cost Regression Analysis",
        "short_name": "Medical Cost Regression",
        "domain": "Healthcare Analytics",
        "role": "Data Analyst",
        "status": "In Progress",
        "difficulty": "Intermediate",
        "dataset": "Medical insurance cost dataset",
        "tools": ["Python", "Regression", "Pandas", "Scikit-learn", "EDA"],
        "problem": "Healthcare cost data needs analysis to understand how patient attributes influence insurance charges.",
        "solution": "Build regression models to predict medical cost and explain key cost drivers.",
        "business_value": "Shows regression modeling, feature interpretation, and healthcare analytics.",
        "pages": ["Cost Overview", "Feature Analysis", "Regression Model", "Prediction Results"],
        "kpis": ["MAE", "MSE", "R2 score", "Average charge", "Top cost driver"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "Soybean Sugar Content Prediction using Machine Learning",
        "short_name": "Soybean ML",
        "domain": "Agricultural Analytics",
        "role": "Data Analyst",
        "status": "In Progress",
        "difficulty": "Advanced",
        "dataset": "Advanced Soybean Agricultural Dataset",
        "tools": ["Python", "Linear Regression", "Random Forest", "GridSearchCV", "Feature Importance"],
        "problem": "Agricultural datasets can help predict crop characteristics and improve analysis of plant traits.",
        "solution": "Build regression models to predict soybean sugar content and compare model performance.",
        "business_value": "Shows end-to-end ML workflow, regression, model evaluation, and feature importance.",
        "pages": ["Data Cleaning", "EDA", "Model Comparison", "Feature Importance", "Residual Analysis"],
        "kpis": ["MSE", "R2 score", "Cross-validation score", "Feature importance", "Prediction error"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "K-Means Customer Support Clustering",
        "short_name": "K-Means Clustering",
        "domain": "Customer Analytics",
        "role": "Data Analyst",
        "status": "In Progress",
        "difficulty": "Intermediate",
        "dataset": "Technical support or customer service dataset",
        "tools": ["Python", "K-Means", "Elbow Method", "Silhouette Score", "Clustering"],
        "problem": "Support teams need to identify customer or ticket groups to improve service strategy.",
        "solution": "Apply K-Means clustering and evaluate cluster quality using elbow method and silhouette score.",
        "business_value": "Shows segmentation, unsupervised learning, and operational customer analytics.",
        "pages": ["Data Overview", "Cluster Selection", "Segment Profiles", "Recommendations"],
        "kpis": ["Cluster count", "Silhouette score", "Inertia", "Segment size", "Support priority"],
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    },
    {
        "name": "CSR Project Monitoring and Impact Dashboard",
        "short_name": "CSR Impact",
        "domain": "CSR Analytics",
        "role": "Business Analyst",
        "status": "Planned",
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
        "name": "AI-Powered Business Process Automation Dashboard",
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

# =========================================================
# EXPERIENCE DATA
# =========================================================

experience = [
    {
        "role": "Data Analyst",
        "company": "A. F. Ferguson & Co. | PwC Network",
        "duration": "Sep 2025 - Dec 2025",
        "location": "Pakistan",
        "details": "Prepared, cleaned, and structured multi-source datasets for KPI tracking, HR reporting, payroll data accuracy, and operational analysis. Supported Excel and SQL reporting workflows, built dashboards and analytical summaries, conducted data validation checks, and improved reporting workflows for internal teams.",
        "tags": ["Data Cleaning", "KPI Reporting", "SQL", "Excel", "Dashboards", "Data Validation", "Reporting Automation"]
    },
    {
        "role": "Community Development Intern",
        "company": "Pakistan Petroleum Limited",
        "duration": "Jul 2025 - Aug 2025",
        "location": "Karachi, Pakistan",
        "details": "Supported CSR and community development projects across education, health, water supply, and welfare initiatives. Prepared Excel-based budget sheets, cost estimates, operational records, project trackers, documentation packs, stakeholder follow-up records, and management reporting updates.",
        "tags": ["CSR", "Budgeting", "Documentation", "Stakeholder Coordination", "Reporting", "Project Tracking", "Compliance"]
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
        "details": "Completed project-based data science tasks involving data cleaning, exploratory data analysis, visualization, customer behaviour analysis, decision tree modeling, and business pattern identification using Python.",
        "tags": ["Python", "EDA", "Visualization", "Machine Learning", "Pandas", "NumPy", "Decision Tree"]
    },
    {
        "role": "Data Science and AI Intern",
        "company": "SYNC INTERN'S",
        "duration": "Mar 2024 - Apr 2024",
        "location": "Remote",
        "details": "Completed hands-on analytics and AI tasks involving data preparation, customer analysis, experimentation, uplift testing, and business-focused data interpretation.",
        "tags": ["AI", "Customer Analysis", "Experimentation", "Analytics", "Business Interpretation", "Uplift Testing"]
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
        "company": "PakLaunch",
        "duration": "Jul 2023 - Sep 2023",
        "location": "Remote",
        "details": "Promoted initiatives through digital outreach, student engagement, event promotion, and community-building activities focused on entrepreneurship and professional development.",
        "tags": ["Community Engagement", "Outreach", "Event Promotion", "Public Speaking", "Communication"]
    },
    {
        "role": "Business Development Intern",
        "company": "GAOTek Inc.",
        "duration": "Jun 2023 - Jul 2023",
        "location": "Remote",
        "details": "Conducted market research, lead generation, competitive analysis, market mapping, and research on potential clients and industry segments.",
        "tags": ["Market Research", "Lead Generation", "Competitive Analysis", "Business Development", "Client Research"]
    }
]

# =========================================================
# CERTIFICATIONS DATA
# =========================================================

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
    {"name": "CS50 Python", "issuer": "Harvard CS50", "category": "Python"},
    {"name": "Python 101", "issuer": "IBM", "category": "Python"},
    {"name": "Intermediate SQL", "issuer": "DataCamp", "category": "SQL"},
    {"name": "MySQL", "issuer": "Analyst Builder", "category": "SQL"},
    {"name": "PostgreSQL", "issuer": "Codecademy", "category": "SQL"},
    {"name": "Excel for Business Analysts", "issuer": "Online Course", "category": "Excel"},
    {"name": "Data Analyst Associate", "issuer": "Online Course", "category": "Data Analytics"},
    {"name": "Power BI Desktop", "issuer": "Online Course", "category": "Power BI"},
    {"name": "Business Process Management", "issuer": "Online Course", "category": "Business Analysis"},
    {"name": "SEO", "issuer": "Online Course", "category": "Digital Marketing"},
    {"name": "Exploratory Data Analysis", "issuer": "Online Course", "category": "Data Analytics"}
]

# =========================================================
# SKILLS DATA
# =========================================================

skills = [
    {"Skill": "Python", "Category": "Data Analytics", "Strength": 76},
    {"Skill": "SQL", "Category": "Data Analytics", "Strength": 72},
    {"Skill": "Power BI", "Category": "Dashboarding", "Strength": 75},
    {"Skill": "Excel", "Category": "Business Reporting", "Strength": 88},
    {"Skill": "DAX", "Category": "Dashboarding", "Strength": 58},
    {"Skill": "Pandas", "Category": "Data Analytics", "Strength": 80},
    {"Skill": "NumPy", "Category": "Data Analytics", "Strength": 74},
    {"Skill": "Matplotlib", "Category": "Visualization", "Strength": 72},
    {"Skill": "Seaborn", "Category": "Visualization", "Strength": 70},
    {"Skill": "Plotly", "Category": "Visualization", "Strength": 60},
    {"Skill": "Scikit-learn", "Category": "Machine Learning", "Strength": 64},
    {"Skill": "Linear Regression", "Category": "Machine Learning", "Strength": 68},
    {"Skill": "Random Forest", "Category": "Machine Learning", "Strength": 62},
    {"Skill": "Classification", "Category": "Machine Learning", "Strength": 62},
    {"Skill": "Clustering", "Category": "Machine Learning", "Strength": 60},
    {"Skill": "Model Evaluation", "Category": "Machine Learning", "Strength": 64},
    {"Skill": "Business Analysis", "Category": "Business Analysis", "Strength": 82},
    {"Skill": "Process Mapping", "Category": "Business Analysis", "Strength": 80},
    {"Skill": "Requirements Thinking", "Category": "Business Analysis", "Strength": 72},
    {"Skill": "Documentation", "Category": "Business Analysis", "Strength": 86},
    {"Skill": "Stakeholder Reporting", "Category": "Business Analysis", "Strength": 84},
    {"Skill": "Project Tracking", "Category": "Business Analysis", "Strength": 84},
    {"Skill": "Budget Tracking", "Category": "Business Reporting", "Strength": 86},
    {"Skill": "KPI Reporting", "Category": "Business Reporting", "Strength": 80},
    {"Skill": "Data Cleaning", "Category": "Data Quality", "Strength": 84},
    {"Skill": "Data Validation", "Category": "Data Quality", "Strength": 82},
    {"Skill": "EDA", "Category": "Data Analytics", "Strength": 82},
    {"Skill": "Financial Analysis", "Category": "Finance Analytics", "Strength": 68},
    {"Skill": "Accounting Basics", "Category": "Finance Analytics", "Strength": 70},
    {"Skill": "Cash Flow Analysis", "Category": "Finance Analytics", "Strength": 62},
    {"Skill": "HR Analytics", "Category": "HR Analytics", "Strength": 72},
    {"Skill": "Marketing Analytics", "Category": "Marketing Analytics", "Strength": 68},
    {"Skill": "Customer Analytics", "Category": "Customer Analytics", "Strength": 70},
    {"Skill": "CSR Analytics", "Category": "CSR Analytics", "Strength": 84},
    {"Skill": "Inventory Analytics", "Category": "Operations Analytics", "Strength": 60},
    {"Skill": "Public Data Analysis", "Category": "Public Data Analytics", "Strength": 68},
    {"Skill": "Geospatial Analytics", "Category": "Public Data Analytics", "Strength": 50},
    {"Skill": "AI Automation", "Category": "AI Automation", "Strength": 58},
    {"Skill": "n8n", "Category": "AI Automation", "Strength": 55},
    {"Skill": "LLM Tools", "Category": "AI Automation", "Strength": 54},
    {"Skill": "RAG Concepts", "Category": "AI Automation", "Strength": 50},
    {"Skill": "APIs", "Category": "AI Automation", "Strength": 52},
    {"Skill": "Vector Databases", "Category": "AI Automation", "Strength": 40},
    {"Skill": "QA Testing", "Category": "Quality Assurance", "Strength": 74},
    {"Skill": "Bug Reporting", "Category": "Quality Assurance", "Strength": 76},
    {"Skill": "Workflow Review", "Category": "Quality Assurance", "Strength": 76},
    {"Skill": "Digital Marketing", "Category": "Marketing", "Strength": 64},
    {"Skill": "SEO", "Category": "Marketing", "Strength": 60},
    {"Skill": "Market Research", "Category": "Business Development", "Strength": 68},
    {"Skill": "Lead Generation", "Category": "Business Development", "Strength": 62}
]

# =========================================================
# EDUCATION DATA
# =========================================================

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

# =========================================================
# EVIDENCE DATA
# =========================================================

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
        "claim": "CSR project tracking and budget reporting",
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
    },
    {
        "claim": "Quality assurance and product workflow review",
        "proof": "Tested web product features, documented bugs, reviewed workflow issues, and monitored content quality.",
        "source": "Oigetit QA Analyst role",
        "confidence": "Strong"
    },
    {
        "claim": "Business development and market research",
        "proof": "Conducted lead generation, competitor research, market mapping, and client research.",
        "source": "GAOTek Business Development internship",
        "confidence": "Strong"
    }
]

project_df = pd.DataFrame(projects)
experience_df = pd.DataFrame(experience)
cert_df = pd.DataFrame(certifications)
skills_df = pd.DataFrame(skills)
evidence_df = pd.DataFrame(evidence)
education_df = pd.DataFrame(education)

# =========================================================
# HELPER FUNCTIONS
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
    st.caption("Data Analytics | Business Analysis | AI Automation")

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Portfolio Projects",
            "Interactive Demo",
            "Role Fit",
            "Proof of Skills",
            "Technical Skills",
            "Work Experience",
            "Certifications",
            "Education",
            "Contact"
        ],
        icons=[
            "house", "grid", "calculator", "person-check", "shield-check",
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
# HOME PAGE
# =========================================================

if selected == "Home":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <div class="eyebrow">Portfolio Dashboard</div>
                <div class="hero-title">Business Analytics and AI Portfolio</div>
                <div class="hero-subtitle">
                    Data Analytics, Business Analysis, Dashboard Reporting, Machine Learning, and AI Automation projects.
                </div>
                <p class="hero-text">
                    A professional portfolio dashboard showcasing completed work, current builds, and planned case studies.
                    Each project is organised by business problem, tools, KPIs, dashboard plan, and role relevance.
                </p>
                <span class="badge">Python</span>
                <span class="badge">SQL</span>
                <span class="badge">Power BI</span>
                <span class="badge">Excel</span>
                <span class="badge-purple">Business Analysis</span>
                <span class="badge-purple">Process Mapping</span>
                <span class="badge-green">AI Automation</span>
                <span class="badge-green">Machine Learning</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Portfolio Projects", len(project_df))
    m2.metric("Business Domains", project_df["domain"].nunique())
    m3.metric("Work Experiences", len(experience_df))
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

    featured_names = [
        "AI Job Market",
        "HR Analytics",
        "CSR Impact",
        "Process Automation"
    ]

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
# PORTFOLIO PROJECTS PAGE
# =========================================================

elif selected == "Portfolio Projects":
    st.markdown('<div class="section-title">Portfolio Projects</div>', unsafe_allow_html=True)
    st.write("Explore project case studies by target role, business domain, project status, difficulty, or keyword.")

    f1, f2, f3 = st.columns(3)

    with f1:
        role_filter = st.multiselect(
            "Role focus",
            sorted(project_df["role"].unique()),
            placeholder="Select role"
        )

    with f2:
        domain_filter = st.multiselect(
            "Business domain",
            sorted(project_df["domain"].unique()),
            placeholder="Select domain"
        )

    with f3:
        status_filter = st.multiselect(
            "Project status",
            sorted(project_df["status"].unique()),
            placeholder="Select status"
        )

    f4, f5 = st.columns([1, 2])

    with f4:
        difficulty_filter = st.multiselect(
            "Difficulty",
            sorted(project_df["difficulty"].unique()),
            placeholder="Select difficulty"
        )

    with f5:
        search = st.text_input(
            "Search projects",
            placeholder="Search by topic, for example HR, finance, churn, CSR, SQL, Power BI"
        )

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
# INTERACTIVE DEMO PAGE
# =========================================================

elif selected == "Interactive Demo":
    st.markdown('<div class="section-title">Interactive Demo</div>', unsafe_allow_html=True)

    st.write(
        "This section shows a working business analytics calculator. "
        "It demonstrates how manual process data can be converted into automation impact estimates."
    )

    st.markdown(
        """
        <div class="info-panel">
            <h2>Automation Savings Calculator</h2>
            <p class="subtle">
                Estimate how much time and cost a business could save by automating a repetitive manual workflow.
                This fits business process automation, ICT business analysis, and AI automation projects.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Process Inputs")

        monthly_cases = st.slider(
            "Number of cases processed per month",
            min_value=50,
            max_value=10000,
            value=1200,
            step=50
        )

        minutes_per_case = st.slider(
            "Average manual minutes per case",
            min_value=1,
            max_value=120,
            value=18,
            step=1
        )

        hourly_cost = st.slider(
            "Average staff cost per hour",
            min_value=10,
            max_value=150,
            value=35,
            step=5
        )

        automation_rate = st.slider(
            "Expected automation percentage",
            min_value=5,
            max_value=95,
            value=45,
            step=5
        )

        error_rate_before = st.slider(
            "Current manual error rate",
            min_value=1,
            max_value=40,
            value=12,
            step=1
        )

        error_reduction = st.slider(
            "Expected error reduction after automation",
            min_value=5,
            max_value=90,
            value=50,
            step=5
        )

    total_manual_hours = (monthly_cases * minutes_per_case) / 60
    automated_hours = total_manual_hours * (automation_rate / 100)
    remaining_manual_hours = total_manual_hours - automated_hours

    monthly_cost_before = total_manual_hours * hourly_cost
    monthly_cost_saved = automated_hours * hourly_cost
    annual_cost_saved = monthly_cost_saved * 12

    error_rate_after = error_rate_before * (1 - error_reduction / 100)
    errors_before = monthly_cases * (error_rate_before / 100)
    errors_after = monthly_cases * (error_rate_after / 100)
    errors_reduced = errors_before - errors_after

    if automation_rate >= 70:
        impact_level = "High automation impact"
        impact_badge = "badge-green"
    elif automation_rate >= 40:
        impact_level = "Medium automation impact"
        impact_badge = "badge-orange"
    else:
        impact_level = "Early automation opportunity"
        impact_badge = "badge-purple"

    with col2:
        st.markdown("### Estimated Impact")

        m1, m2 = st.columns(2)
        m1.metric("Manual Hours / Month", f"{total_manual_hours:,.0f}")
        m2.metric("Hours Saved / Month", f"{automated_hours:,.0f}")

        m3, m4 = st.columns(2)
        m3.metric("Monthly Cost Saved", f"${monthly_cost_saved:,.0f}")
        m4.metric("Annual Cost Saved", f"${annual_cost_saved:,.0f}")

        m5, m6 = st.columns(2)
        m5.metric("Errors Reduced / Month", f"{errors_reduced:,.0f}")
        m6.metric("Remaining Manual Hours", f"{remaining_manual_hours:,.0f}")

        st.markdown(
            f"""
            <div class="project-card">
                <h3>Automation Recommendation</h3>
                <p class="subtle">
                    Based on the selected assumptions, this process has an estimated monthly saving of
                    <b>${monthly_cost_saved:,.0f}</b> and an estimated annual saving of
                    <b>${annual_cost_saved:,.0f}</b>.
                </p>
                <span class="{impact_badge}">{impact_level}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Before vs After Automation</div>', unsafe_allow_html=True)

    comparison_data = pd.DataFrame({
        "Metric": [
            "Monthly manual hours",
            "Monthly labour cost",
            "Error rate",
            "Estimated errors per month"
        ],
        "Before Automation": [
            round(total_manual_hours, 2),
            round(monthly_cost_before, 2),
            round(error_rate_before, 2),
            round(errors_before, 2)
        ],
        "After Automation": [
            round(remaining_manual_hours, 2),
            round(monthly_cost_before - monthly_cost_saved, 2),
            round(error_rate_after, 2),
            round(errors_after, 2)
        ]
    })

    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Metric": st.column_config.TextColumn("Metric", width="medium"),
            "Before Automation": st.column_config.NumberColumn("Before Automation", format="%.2f"),
            "After Automation": st.column_config.NumberColumn("After Automation", format="%.2f"),
        }
    )

    fig = px.bar(
        comparison_data,
        x="Metric",
        y=["Before Automation", "After Automation"],
        barmode="group",
        title="Before vs After Automation Comparison",
        template="plotly_dark"
    )

    st.plotly_chart(plotly_layout(fig), use_container_width=True)

    st.markdown('<div class="section-title">Business Analyst Notes</div>', unsafe_allow_html=True)

    with st.expander("How this connects to business analysis"):
        st.markdown(
            """
            This demo shows how a business analyst can translate a manual workflow into measurable improvement areas.

            It covers:

            - current process volume
            - time per transaction
            - labour cost
            - automation opportunity
            - error reduction
            - before vs after comparison
            - estimated financial impact
            """
        )

    with st.expander("How this connects to AI automation"):
        st.markdown(
            """
            This type of calculator can be connected to an AI automation project where repetitive tasks are handled through:

            - rule-based automation
            - document extraction
            - workflow routing
            - approval reminders
            - ticket classification
            - AI recommendations
            """
        )

    with st.expander("How to explain this in an interview"):
        st.markdown(
            """
            I built an automation savings calculator to show how manual process data can be converted into business impact.
            The user can change process volume, time per case, labour cost, automation percentage, and error reduction.
            The app then calculates time saved, cost saved, remaining manual work, and before-after improvement.
            """
        )

# =========================================================
# ROLE FIT PAGE
# =========================================================

elif selected == "Role Fit":
    st.markdown('<div class="section-title">Role Fit</div>', unsafe_allow_html=True)
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
# PROOF OF SKILLS PAGE
# =========================================================

elif selected == "Proof of Skills":
    st.markdown('<div class="section-title">Proof of Skills</div>', unsafe_allow_html=True)
    st.write("This page connects portfolio claims with real proof from experience, projects, or learning.")

    confidence_filter = st.multiselect(
        "Confidence level",
        sorted(evidence_df["confidence"].unique()),
        placeholder="Select confidence level"
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
# TECHNICAL SKILLS PAGE
# =========================================================

elif selected == "Technical Skills":
    st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)

    category_filter = st.multiselect(
        "Skill category",
        sorted(skills_df["Category"].unique()),
        placeholder="Select skill category"
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
# WORK EXPERIENCE PAGE
# =========================================================

elif selected == "Work Experience":
    st.markdown('<div class="section-title">Work Experience</div>', unsafe_allow_html=True)

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
# CERTIFICATIONS PAGE
# =========================================================

elif selected == "Certifications":
    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

    cert_category = st.multiselect(
        "Certification category",
        sorted(cert_df["category"].unique()),
        placeholder="Select category"
    )

    issuer_filter = st.multiselect(
        "Issuer",
        sorted(cert_df["issuer"].unique()),
        placeholder="Select issuer"
    )

    cert_view = cert_df.copy()

    if cert_category:
        cert_view = cert_view[cert_view["category"].isin(cert_category)]

    if issuer_filter:
        cert_view = cert_view[cert_view["issuer"].isin(issuer_filter)]

    c1, c2 = st.columns([1.1, 1])

    with c1:
        cert_count = cert_df["category"].value_counts().reset_index()
        cert_count.columns = ["Category", "Count"]

        fig = px.bar(
            cert_count,
            x="Category",
            y="Count",
            color="Category",
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
# EDUCATION PAGE
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
# CONTACT PAGE
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
