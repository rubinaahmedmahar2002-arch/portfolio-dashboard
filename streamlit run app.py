import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Rubina Ahmed Mahar | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
html, body, [class*="css"] {font-family: 'Inter', sans-serif;}
.stApp {background: radial-gradient(circle at 8% 8%, rgba(37,99,235,.16), transparent 28%), radial-gradient(circle at 92% 8%, rgba(124,58,237,.16), transparent 28%), linear-gradient(135deg,#020617 0%,#07111f 48%,#0f172a 100%); color:#f8fafc;}
[data-testid="stHeader"] {background: rgba(2,6,23,.95)!important; border-bottom:1px solid rgba(148,163,184,.18)!important;}
[data-testid="stSidebar"] {background: linear-gradient(180deg,#020617 0%,#0f172a 100%); border-right:1px solid rgba(148,163,184,.24);}
[data-testid="stSidebar"] * {color:#f8fafc!important;}
h1,h2,h3,h4,h5,h6,p,span,div,label {color:#f8fafc!important;}
.block-container {padding-top:1.5rem; padding-bottom:2rem;}
.hero {position:relative; padding:44px; border-radius:30px; overflow:hidden; background:linear-gradient(135deg,rgba(15,23,42,.96),rgba(30,41,59,.82)), radial-gradient(circle at 88% 22%,rgba(14,165,233,.22),transparent 28%), radial-gradient(circle at 18% 85%,rgba(124,58,237,.20),transparent 28%); border:1px solid rgba(148,163,184,.28); box-shadow:0 28px 90px rgba(0,0,0,.45); min-height:350px; margin-bottom:18px;}
.hero::before {content:""; position:absolute; inset:0; background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px), linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px); background-size:34px 34px; mask-image:linear-gradient(to bottom,black,transparent 92%); pointer-events:none;}
.hero-content {position:relative; z-index:2;}
.eyebrow {display:inline-flex; padding:9px 15px; border-radius:999px; background:rgba(37,99,235,.15); border:1px solid rgba(147,197,253,.36); color:#bfdbfe!important; font-size:13px; font-weight:800; letter-spacing:.4px; text-transform:uppercase; margin-bottom:22px;}
.hero-title {font-size:58px; line-height:1; font-weight:900; letter-spacing:-2.2px; margin-bottom:18px; background:linear-gradient(90deg,#fff 0%,#bfdbfe 44%,#c4b5fd 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.hero-subtitle {font-size:22px; line-height:1.45; max-width:1000px; color:#dbeafe!important; font-weight:700; margin-bottom:18px;}
.hero-text,.subtle {font-size:16px; line-height:1.75; color:#cbd5e1!important;}
.section-title {font-size:32px; font-weight:900; letter-spacing:-.8px; margin:26px 0 16px 0; color:#fff!important;}
.small-muted {color:#94a3b8!important; font-size:13px; line-height:1.6;}
.badge,.badge-purple,.badge-green,.badge-orange,.badge-grey {display:inline-block; padding:8px 13px; margin:5px 6px 5px 0; border-radius:999px; font-size:13px; font-weight:800;}
.badge {background:rgba(59,130,246,.14); border:1px solid rgba(147,197,253,.30); color:#dbeafe!important;}
.badge-purple {background:rgba(124,58,237,.16); border:1px solid rgba(196,181,253,.32); color:#ede9fe!important;}
.badge-green {background:rgba(22,163,74,.14); border:1px solid rgba(134,239,172,.30); color:#dcfce7!important;}
.badge-orange {background:rgba(234,88,12,.14); border:1px solid rgba(253,186,116,.30); color:#ffedd5!important;}
.badge-grey {background:rgba(100,116,139,.18); border:1px solid rgba(203,213,225,.20); color:#e2e8f0!important;}
.glass,.project-card {padding:24px; border-radius:24px; background:rgba(15,23,42,.76); border:1px solid rgba(148,163,184,.23); box-shadow:0 16px 45px rgba(0,0,0,.26); height:100%;}
.project-card {padding:26px; background:linear-gradient(135deg,rgba(15,23,42,.96),rgba(30,41,59,.84)); margin-bottom:18px;}
.glass:hover,.project-card:hover {transform:translateY(-3px); border-color:rgba(125,211,252,.50); transition:all .22s ease;}
.timeline {padding:20px 24px; border-left:4px solid rgba(56,189,248,.85); margin-bottom:18px; background:rgba(15,23,42,.74); border-radius:20px; border:1px solid rgba(148,163,184,.20); box-shadow:0 16px 45px rgba(0,0,0,.24);}
.info-panel {padding:26px; border-radius:28px; background:radial-gradient(circle at 15% 15%,rgba(14,165,233,.18),transparent 25%), radial-gradient(circle at 82% 18%,rgba(124,58,237,.18),transparent 28%), rgba(15,23,42,.84); border:1px solid rgba(148,163,184,.26); box-shadow:0 24px 64px rgba(0,0,0,.34);}
.stat-number {font-size:30px; font-weight:900; color:#bae6fd!important;}
.stat-label {font-size:13px; color:#cbd5e1!important; font-weight:800; text-transform:uppercase; letter-spacing:.5px;}
div[data-testid="stMetric"] {background:rgba(15,23,42,.82); border:1px solid rgba(148,163,184,.24); padding:18px; border-radius:22px; box-shadow:0 16px 38px rgba(0,0,0,.26);}
div[data-testid="stMetric"] label {color:#cbd5e1!important; font-weight:800!important;}
div[data-testid="stMetricValue"] {color:#fff!important; font-weight:900!important;}
.stSelectbox label,.stMultiSelect label,.stTextInput label,.stSlider label,.stNumberInput label {color:#f8fafc!important; font-weight:800!important;}
div[data-baseweb="select"]>div,.stTextInput input,.stNumberInput input {background-color:#0f172a!important; color:#f8fafc!important; border:1.5px solid #38bdf8!important; border-radius:12px!important; min-height:46px!important;}
div[data-baseweb="select"] *, div[data-baseweb="popover"], div[data-baseweb="popover"] * {background-color:#0f172a!important; color:#f8fafc!important; opacity:1!important;}
ul[role="listbox"] {background-color:#0f172a!important; border:1px solid #38bdf8!important; border-radius:12px!important; padding:6px!important;}
ul[role="listbox"] li, div[role="option"], li[role="option"] {background-color:#0f172a!important; color:#f8fafc!important; opacity:1!important; font-weight:650!important;}
ul[role="listbox"] li:hover, div[role="option"]:hover, li[role="option"]:hover {background-color:#1e293b!important; color:#fff!important;}
div[role="option"][aria-selected="true"], li[role="option"][aria-selected="true"] {background-color:#2563eb!important; color:#fff!important; font-weight:800!important;}
div[data-baseweb="tag"] {background-color:#1e40af!important; border:1px solid #60a5fa!important;}
div[data-baseweb="tag"] span {color:#fff!important; font-weight:700!important;}
.stTabs [data-baseweb="tab-list"] {gap:10px;}
.stTabs [data-baseweb="tab"] {background:rgba(15,23,42,.82); border:1px solid rgba(148,163,184,.22); border-radius:999px; padding:12px 20px;}
.stTabs [aria-selected="true"] {background:linear-gradient(135deg,rgba(14,165,233,.34),rgba(124,58,237,.34)); border-color:rgba(125,211,252,.58);}
a {color:#93c5fd!important;}
</style>
""", unsafe_allow_html=True)


def p(name, short, domain, role, status, difficulty, dataset, tools, context, work, result, deliverable, evidence, pages, kpis):
    return {
        "name": name,
        "short_name": short,
        "domain": domain,
        "role": role,
        "status": status,
        "difficulty": difficulty,
        "dataset": dataset,
        "tools": tools,
        "context": context,
        "work": work,
        "result": result,
        "deliverable": deliverable,
        "evidence": evidence,
        "pages": pages,
        "kpis": kpis,
        "github": "https://github.com/rubinaahmedmahar2002-arch/Projects"
    }

projects = [
    p("AI-Powered Global Data and AI Job Market Intelligence", "AI Job Market", "Data Analytics", "Data Analyst", "Completed", "Advanced", "Global data and AI job market dataset", ["Python", "Pandas", "Scikit-learn", "Matplotlib", "Machine Learning"], "I wanted to understand salary patterns, role demand, and skill trends across data and AI jobs.", "I cleaned and explored a global job market dataset, analysed salary trends, and trained machine learning models to estimate salary outcomes.", "This project connects labour market data with salary insight, skill-demand analysis, and career planning.", "Python analysis, model workflow, salary trend views, and project notes.", "Completed analysis workflow and GitHub project reference.", ["Market overview", "Salary analysis", "Role and skill trends", "Prediction model", "Recommendations"], ["Average salary", "Top roles", "Top skills", "Salary by region", "Model performance"]),
    p("HR Analytics Dashboard using Power BI", "HR Analytics", "HR Analytics", "Data Analyst", "Completed", "Intermediate", "HR analytics sample dataset", ["Power BI", "Excel", "HR Metrics", "Dashboard Design", "Data Cleaning"], "I worked on HR-style reporting where employee structure, attrition, and workforce metrics needed to be easier to review.", "I prepared the HR dataset and created a Power BI dashboard covering workforce demographics, department metrics, and employee trends.", "The dashboard presents HR data in a format suitable for workforce planning and management reporting.", "Power BI dashboard structure, HR metrics, and cleaned reporting dataset.", "Dashboard workflow and GitHub project reference.", ["Workforce overview", "Attrition analysis", "Department view", "Employee insights"], ["Total employees", "Attrition rate", "Average salary", "Average tenure", "Department headcount"]),
    p("Project Management Tracker using Microsoft Excel", "Project Tracker", "Business Reporting", "Business Analyst", "Completed", "Intermediate", "Project tracking workbook", ["Excel", "Project Tracking", "Status Reporting", "Data Validation", "Conditional Formatting"], "I wanted a simple project tracker for tasks, owners, deadlines, delays, and progress updates.", "I created an Excel-based tracker with status logic, task ownership, deadlines, progress indicators, and reporting views.", "The tracker supports clearer project follow-up, accountability, and reporting discipline.", "Excel tracker, task status logic, reporting views, and delay monitoring.", "Completed workbook and GitHub project reference.", ["Project overview", "Task tracker", "Status summary", "Risk and delay view"], ["Total tasks", "Completed tasks", "Delayed tasks", "Pending tasks", "Completion rate"]),
    p("Python for Data Analysis: Pandas and NumPy", "Python Data Analysis", "Data Analytics", "Data Analyst", "Completed", "Foundation", "Python practice datasets", ["Python", "Pandas", "NumPy", "Data Cleaning", "EDA"], "I wanted to strengthen my foundation in preparing and exploring structured datasets with Python.", "I used Pandas and NumPy to load, clean, reshape, summarise, and explore different practice datasets.", "This project shows my core data preparation and exploratory analysis workflow.", "Python notebooks, data cleaning workflow, and exploratory summaries.", "Completed practice workflows and GitHub project reference.", ["Data loading", "Data cleaning", "Feature summary", "Exploratory analysis"], ["Rows cleaned", "Missing values", "Duplicate records", "Feature count", "Summary metrics"]),
    p("Exploratory Data Analysis of Global Suicide Rates", "Global Suicide EDA", "Public Health Analytics", "Data Analyst", "Completed", "Intermediate", "Global suicide rates dataset", ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn"], "I explored public health data to understand how suicide rates vary across countries, years, age groups, and gender.", "I cleaned the dataset, created visual comparisons, and reviewed patterns across demographic and regional dimensions.", "This project helped me practise sensitive public health storytelling with data.", "EDA notebook, demographic comparisons, and visual analysis.", "Completed analysis workflow and GitHub project reference.", ["Global overview", "Country trends", "Age and gender analysis", "Risk pattern view"], ["Suicide rate", "Country ranking", "Age group risk", "Gender comparison", "Trend movement"]),
    p("Global Mental Health Data Analysis and Modeling", "Mental Health Analytics", "Public Health Analytics", "Data Analyst", "Completed", "Advanced", "Global mental health dataset", ["Python", "Pandas", "Visualization", "Scikit-learn", "Modeling"], "I used mental health indicators to explore country-level patterns and relationships in public health data.", "I cleaned and analysed the dataset, compared indicators across countries, and applied basic modeling to understand relationships.", "The project combines EDA, public health context, and beginner-friendly predictive modeling.", "EDA workflow, model summary, and country-level comparison views.", "Completed analysis workflow and GitHub project reference.", ["Mental health overview", "Country comparison", "Trend analysis", "Modeling summary"], ["Indicator rate", "Country average", "Trend change", "Model score", "Risk pattern"]),
    p("Heart Attack Analysis and Prediction", "Heart Risk Prediction", "Healthcare Analytics", "Data Analyst", "Completed", "Advanced", "Heart attack risk dataset", ["Python", "Pandas", "Scikit-learn", "Classification", "EDA"], "I wanted to understand patient risk patterns using structured healthcare data.", "I explored the dataset, reviewed key health indicators, and trained classification models for heart risk prediction.", "This project shows healthcare analytics, model evaluation, and feature interpretation.", "Classification workflow, model evaluation, and feature review.", "Completed modeling workflow and GitHub project reference.", ["Health overview", "Risk factors", "Model results", "Feature analysis"], ["Accuracy", "Risk class", "Feature impact", "Patient count", "Prediction score"]),
    p("Water Quality Exploratory Data Analysis", "Water Quality EDA", "Environmental Analytics", "Data Analyst", "Completed", "Intermediate", "Water quality dataset", ["Python", "Pandas", "Matplotlib", "EDA", "Data Quality Checks"], "I explored environmental data to understand water quality indicators and data quality issues.", "I checked missing values, reviewed indicator distributions, created visual summaries, and highlighted safety-related patterns.", "This project shows environmental analytics, EDA, and data quality thinking.", "EDA notebook, data quality checks, and indicator summaries.", "Completed analysis workflow and GitHub project reference.", ["Water quality overview", "Missing values", "Indicator trends", "Safety summary"], ["Quality score", "Missing values", "Indicator average", "Risk level", "Trend change"]),
    p("Spotify User Behaviour and Pattern Recognition", "Spotify User Analytics", "Customer Analytics", "Data Analyst", "Completed", "Advanced", "Spotify user behaviour dataset", ["Python", "Pandas", "Machine Learning", "Pattern Recognition", "EDA"], "I explored digital platform data to understand listening behaviour, engagement patterns, and user groups.", "I analysed Spotify user behaviour and identified patterns using EDA and machine learning techniques.", "This project shows customer behaviour analysis, segmentation thinking, and product analytics.", "User behaviour analysis, pattern review, and segment-style summaries.", "Completed analysis workflow and GitHub project reference.", ["User overview", "Listening patterns", "Segment analysis", "Engagement insights"], ["Listening frequency", "User segment", "Engagement score", "Top pattern", "Cluster count"]),
    p("Netflix Data Analytics Project", "Netflix Analytics", "Content Analytics", "Data Analyst", "Completed", "Intermediate", "Netflix titles dataset", ["Python", "Pandas", "Visualization", "Content Analytics", "EDA"], "I explored a content catalogue dataset to understand trends in Netflix titles, genres, countries, and release years.", "I cleaned the dataset and created analysis views for content type, genre, country, release patterns, and duration.", "This project shows entertainment analytics and business storytelling through content data.", "Content catalogue analysis, visual summaries, and trend views.", "Completed analysis workflow and GitHub project reference.", ["Catalogue overview", "Country analysis", "Genre trends", "Duration and release patterns"], ["Total titles", "Movie count", "TV show count", "Top countries", "Top genres"]),
    p("Youth Job Opportunities Around the World", "Youth Jobs Analytics", "Labour Market Analytics", "Data Analyst", "Completed", "Intermediate", "Global youth job opportunity indicators", ["Python", "Pandas", "Scoring Model", "Visualization", "Business Storytelling"], "I wanted to compare youth employment opportunity indicators across countries in a structured way.", "I created a scoring approach, compared countries, and built visual summaries for employment and opportunity indicators.", "This project shows labour market analysis, index building, and decision-support thinking.", "Country score structure, rankings, visual comparisons, and recommendations.", "Completed analysis workflow and GitHub project reference.", ["Country ranking", "Opportunity score", "Regional view", "Recommendation summary"], ["Opportunity score", "Country rank", "Employment indicator", "Risk level", "Recommendation"]),
    p("Creating Financial Statements using Microsoft Excel", "Financial Statements", "Financial Analytics", "Business Analyst", "Completed", "Foundation", "Accounting and financial statement workbook", ["Excel", "Accounting", "Financial Statements", "Formulas", "Reporting"], "I worked on financial statement preparation to strengthen my accounting and Excel reporting foundation.", "I prepared financial statement formats and calculations in Excel using structured accounting data.", "This project shows accounting knowledge, Excel reporting, and finance data structuring.", "Excel financial statement workbook and reporting summaries.", "Completed workbook and GitHub project reference.", ["Income statement", "Balance sheet", "Cash flow", "Summary"], ["Revenue", "Expenses", "Profit", "Assets", "Liabilities"]),
    p("Medical Cost Regression Analysis", "Medical Cost Regression", "Healthcare Analytics", "Data Analyst", "In Progress", "Intermediate", "Medical insurance cost dataset", ["Python", "Regression", "Pandas", "Scikit-learn", "EDA"], "I am using healthcare cost data to understand how patient attributes affect insurance charges.", "Current work includes regression modeling, feature review, and cost driver interpretation.", "This project is strengthening my regression modeling and healthcare analytics skills.", "Work-in-progress notebook, regression workflow, and feature interpretation notes.", "Work-in-progress analysis and GitHub project reference.", ["Cost overview", "Feature analysis", "Regression model", "Prediction results"], ["MAE", "MSE", "R2 score", "Average charge", "Top cost driver"]),
    p("Soybean Sugar Content Prediction using Machine Learning", "Soybean ML", "Agricultural Analytics", "Data Analyst", "In Progress", "Advanced", "Advanced Soybean Agricultural Dataset", ["Python", "Linear Regression", "Random Forest", "GridSearchCV", "Feature Importance"], "I am using agricultural data to predict soybean sugar content from plant and environmental features.", "Current work includes regression comparison, feature importance review, and machine learning workflow documentation.", "This project strengthens my regression, model evaluation, and explainability skills.", "Work-in-progress model comparison, tuning notes, and feature importance workflow.", "Work-in-progress notebook and GitHub project reference.", ["Data cleaning", "EDA", "Model comparison", "Feature importance", "Residual analysis"], ["MSE", "R2 score", "Cross-validation score", "Feature importance", "Prediction error"]),
    p("K-Means Customer Support Clustering", "K-Means Clustering", "Customer Analytics", "Data Analyst", "In Progress", "Intermediate", "Technical support or customer service dataset", ["Python", "K-Means", "Elbow Method", "Silhouette Score", "Clustering"], "I am exploring customer support segmentation to identify different ticket or customer groups.", "Current work includes K-Means clustering, elbow method, silhouette score review, and segment profiling.", "This project strengthens my unsupervised learning and customer analytics skills.", "Work-in-progress clustering notebook, evaluation metrics, and segment profiles.", "Work-in-progress analysis and GitHub project reference.", ["Data overview", "Cluster selection", "Segment profiles", "Recommendations"], ["Cluster count", "Silhouette score", "Inertia", "Segment size", "Support priority"]),
    p("CSR Project Monitoring and Impact Dashboard", "CSR Impact", "CSR Analytics", "Business Analyst", "Roadmap", "Advanced", "Synthetic CSR project dataset inspired by internship workflows", ["Excel", "Power BI", "Budget Analysis", "Stakeholder Reporting", "Compliance Tracking"], "Case study concept based on CSR project monitoring, budget tracking, vendors, beneficiaries, and compliance records.", "Roadmap case study for a CSR dashboard covering health, education, water supply, and welfare project monitoring.", "This case study connects my PPL internship experience with analytics and reporting workflows.", "Roadmap item with dataset idea, dashboard sections, KPI structure, and business problem.", "Roadmap concept, not presented as completed work.", ["CSR portfolio overview", "Project category", "Budget and vendor", "Impact", "Compliance"], ["Projects", "Budget used", "Beneficiaries", "Completed projects", "Delayed projects"]),
    p("AI-Powered Business Process Automation Dashboard", "Process Automation", "Business Process Automation", "ICT Business Analyst", "Roadmap", "Advanced", "Synthetic workflow dataset", ["Python", "SQL", "Power BI", "Process Mapping", "AI Recommendations"], "Case study concept focused on manual workflows, bottlenecks, errors, rework, and avoidable cost.", "Roadmap case study comparing manual and automation-ready workflows with estimated improvement opportunities.", "This case study shows process analysis, automation planning, and business systems thinking.", "Roadmap item with workflow structure, KPI model, and dashboard sections.", "Roadmap concept, not presented as completed work.", ["Executive overview", "Process flow", "Automation impact", "Recommendations"], ["Total cases", "Average processing time", "Manual hours saved", "Error rate", "Estimated cost savings"]),
    p("Customer Churn and Retention Dashboard", "Customer Retention", "Customer Analytics", "Data Analyst", "Roadmap", "Advanced", "Synthetic customer dataset", ["Python", "SQL", "Machine Learning", "Power BI", "Customer Segmentation"], "Case study concept focused on identifying customers who may leave and understanding churn drivers.", "Roadmap case study covering churn risk scores, customer segments, and retention-focused dashboard views.", "This case study shows customer analytics, segmentation, and revenue protection thinking.", "Roadmap item with dataset idea, dashboard sections, and KPI structure.", "Roadmap concept, not presented as completed work.", ["Churn overview", "Customer segments", "Churn drivers", "Action plan"], ["Churn rate", "Revenue at risk", "High-risk customers", "Retention opportunity value"]),
    p("Marketing ROI and Campaign Performance Dashboard", "Marketing Performance", "Marketing Analytics", "Marketing Analyst", "Roadmap", "Intermediate", "Synthetic campaign data or public business data", ["Power BI", "Excel", "SQL", "Funnel Analysis", "ROI Analysis"], "Case study concept focused on campaign spend, conversions, revenue, profitability, and channel performance.", "Roadmap case study for a marketing dashboard that connects campaign results with budget and ROI reporting.", "This case study shows marketing analytics and budget decision support.", "Roadmap item with campaign dataset idea, funnel structure, and KPI model.", "Roadmap concept, not presented as completed work.", ["Campaign overview", "Channel performance", "Customer funnel", "Budget optimizer"], ["Total spend", "Revenue", "ROAS", "Conversion rate", "CPA"]),
    p("Financial Performance and Cash Flow Dashboard", "Financial Analytics", "Financial Analytics", "Business Analyst", "Roadmap", "Intermediate", "Simulated financial dataset", ["Excel", "Power BI", "SQL", "Variance Analysis", "Accounting"], "Case study concept focused on revenue, expenses, profit, cash flow, and budget variance.", "Roadmap case study for a finance dashboard explaining performance movement and cost control areas.", "This case study shows financial reporting, variance analysis, and decision support.", "Roadmap item with financial dataset idea, dashboard sections, and KPI model.", "Roadmap concept, not presented as completed work.", ["Financial overview", "Revenue analysis", "Expense and budget control", "Cash flow"], ["Revenue", "Gross profit", "Net profit", "Operating expenses", "Cash balance"]),
    p("Public City Data for Small Business Dashboard", "City Business Insights", "Public Data Analytics", "Data Analyst", "Roadmap", "Advanced", "Open city data", ["Python", "Public APIs", "Geospatial Analytics", "Power BI Maps", "Business Storytelling"], "Case study concept focused on location intelligence for small businesses using public city data.", "Roadmap case study using open data to compare suburbs by demand, competition, risk, and opportunity.", "This case study shows public data analytics, maps, and business location analysis.", "Roadmap item with open-data concept, map views, and scoring model.", "Roadmap concept, not presented as completed work.", ["Location score", "Map view", "Business opportunity", "Final recommendation"], ["Best suburbs", "Demand score", "Competition level", "Risk score", "Opportunity score"]),
    p("AI Resume Screening and Recruitment Dashboard", "Recruitment Analytics", "AI and HR Systems", "ICT Business Analyst", "Roadmap", "Advanced", "Sample candidate dataset", ["Python", "NLP", "AI Automation", "Power BI", "Responsible AI"], "Case study concept focused on recruitment analytics, candidate matching, pipeline visibility, and responsible AI checks.", "Roadmap case study for candidate matching, hiring funnel metrics, skill extraction, and fairness review.", "This case study shows HR systems thinking, AI awareness, and human-review workflow design.", "Roadmap item with sample candidate dataset idea, dashboard sections, and fairness review structure.", "Roadmap concept, not presented as completed work.", ["Recruitment overview", "Candidate match", "Pipeline analytics", "Fairness check"], ["Applicants", "Shortlisted candidates", "Average match score", "Hiring funnel conversion"]),
    p("Supply Chain and Inventory Dashboard", "Inventory Analytics", "Operations Analytics", "Operations Analyst", "Roadmap", "Advanced", "Retail inventory dataset", ["SQL", "Power BI", "Inventory Analytics", "Forecasting", "Operations Analysis"], "Case study concept focused on stockouts, overstocking, slow-moving inventory, and supplier delays.", "Roadmap case study for an inventory dashboard with reorder recommendations and supplier performance analysis.", "This case study shows operations analytics, inventory control, and supplier reporting.", "Roadmap item with retail inventory dataset idea, dashboard sections, and KPI model.", "Roadmap concept, not presented as completed work.", ["Inventory overview", "Product performance", "Supplier performance", "Reorder recommendation"], ["Inventory value", "Stockout risk", "Overstocked items", "Slow-moving stock", "Supplier delay rate"]),
    p("RAG-Based Business Knowledge Assistant", "Business Knowledge Assistant", "AI Automation", "AI Automation Analyst", "Roadmap", "Advanced Prototype", "Sample company documents", ["Python", "LLMs", "RAG", "APIs", "Vector Databases", "Dashboard Monitoring"], "Case study concept focused on helping teams search policies, SOPs, reports, and project documents more efficiently.", "Roadmap case study for a RAG-based assistant using sample business documents and answer-quality tracking.", "This case study shows knowledge management, document search, and AI automation workflow thinking.", "Roadmap item with sample document dataset, RAG workflow, and quality-monitoring plan.", "Roadmap concept, not presented as completed work.", ["Assistant overview", "Document knowledge base", "Query analytics", "Quality and risk"], ["Questions asked", "Answer success rate", "Response time", "Documents searched", "Unanswered questions"]),
]

experience = [
    {"role":"Data Analyst", "company":"A. F. Ferguson & Co. | PwC Network", "duration":"Sep 2025 - Dec 2025", "location":"Pakistan", "details":"I worked with multi-source datasets for KPI tracking, HR reporting, payroll data accuracy, and operational analysis. My work included Excel and SQL reporting, dashboard summaries, data validation checks, and reporting workflow improvements.", "tags":["Data Cleaning", "KPI Reporting", "SQL", "Excel", "Dashboards", "Data Validation", "Reporting Automation"]},
    {"role":"Community Development Intern", "company":"Pakistan Petroleum Limited", "duration":"Jul 2025 - Aug 2025", "location":"Karachi, Pakistan", "details":"I supported CSR and community development work across education, health, water supply, and welfare initiatives. My work included budget sheets, cost estimates, project trackers, documentation packs, stakeholder records, and management reporting updates.", "tags":["CSR", "Budgeting", "Documentation", "Stakeholder Coordination", "Reporting", "Project Tracking", "Compliance"]},
    {"role":"Quality Assurance Analyst", "company":"Oigetit Real-Time AI Intelligence Platform", "duration":"Aug 2024 - Nov 2024", "location":"Remote", "details":"I tested web product features, documented defects, reviewed content quality, monitored RSS feeds, and supported product improvement in a remote environment.", "tags":["QA", "Testing", "AI Platform", "Issue Tracking", "Workflow Review", "Content Quality"]},
    {"role":"Data Science Intern", "company":"Prodigy InfoTech", "duration":"Jun 2024 - Aug 2024", "location":"Remote", "details":"I completed project-based data science tasks using Python, EDA, visualisation, customer behaviour analysis, and machine learning models.", "tags":["Python", "EDA", "Visualization", "Machine Learning", "Pandas", "NumPy", "Decision Tree"]},
    {"role":"Data Science and AI Intern", "company":"SYNC INTERN'S", "duration":"Mar 2024 - Apr 2024", "location":"Remote", "details":"I completed analytics and AI tasks involving data preparation, customer analysis, experimentation, uplift testing, and business-focused interpretation.", "tags":["AI", "Customer Analysis", "Experimentation", "Analytics", "Business Interpretation", "Uplift Testing"]},
    {"role":"Marketing Intern", "company":"AI DataYard", "duration":"Oct 2023 - Dec 2023", "location":"Remote", "details":"I created digital content for online visibility, brand awareness, and AI service positioning. I also supported social media engagement and content planning.", "tags":["Digital Marketing", "Content Strategy", "AI Services", "Brand Awareness", "Communication"]},
    {"role":"Campus Ambassador", "company":"PakLaunch", "duration":"Jul 2023 - Sep 2023", "location":"Remote", "details":"I promoted initiatives through student engagement, digital outreach, event promotion, and community-building activities.", "tags":["Community Engagement", "Outreach", "Event Promotion", "Public Speaking", "Communication"]},
    {"role":"Business Development Intern", "company":"GAOTek Inc.", "duration":"Jun 2023 - Jul 2023", "location":"Remote", "details":"I supported market research, lead generation, competitive analysis, market mapping, and client research.", "tags":["Market Research", "Lead Generation", "Competitive Analysis", "Business Development", "Client Research"]}
]

certifications = [
    {"name":"Complete Data Analyst Bootcamp From Basics To Advanced", "issuer":"Udemy", "category":"Data Analytics", "status":"Completed"},
    {"name":"Complete N8N and AI Automation Masterclass", "issuer":"Udemy", "category":"AI Automation", "status":"Completed"},
    {"name":"IT System Engineer and Cloud System Administration", "issuer":"Udemy", "category":"IT and Cloud", "status":"Completed"},
    {"name":"IT Support Entry Level Job Training Course", "issuer":"Udemy", "category":"IT Support", "status":"Completed"},
    {"name":"AI Automation: Build LLM Apps and AI Agents with n8n and APIs", "issuer":"Udemy", "category":"AI Automation", "status":"Completed"},
    {"name":"The Complete AI Agents and AI Automation Course 2025: n8n", "issuer":"Udemy", "category":"AI Automation", "status":"Completed"},
    {"name":"Become an IT Business Analyst: Learn, Apply, Succeed", "issuer":"Udemy", "category":"Business Analysis", "status":"Completed"},
    {"name":"Master Statistics and Machine Learning: Intuition, Math, Code", "issuer":"Udemy", "category":"Statistics and Machine Learning", "status":"In Progress"},
    {"name":"AI Engineer Core Track: LLM Engineering, RAG, QLoRA, Agents", "issuer":"Udemy", "category":"AI Engineering", "status":"In Progress"},
    {"name":"Data and Programming Foundations for AI Skill Path", "issuer":"Codecademy", "category":"AI and Programming", "status":"Completed"},
    {"name":"Introduction to Artificial Intelligence", "issuer":"IBM", "category":"Artificial Intelligence", "status":"Completed"},
    {"name":"SQL for Data Science", "issuer":"University of California, Davis", "category":"SQL", "status":"Completed"},
    {"name":"CompTIA Data+", "issuer":"CompTIA", "category":"Data Analytics", "status":"Completed"},
    {"name":"Google Data Analytics", "issuer":"Google", "category":"Data Analytics", "status":"Completed"},
    {"name":"CS50 Python", "issuer":"Harvard CS50", "category":"Python", "status":"Completed"},
    {"name":"Python 101", "issuer":"IBM", "category":"Python", "status":"Completed"},
    {"name":"Intermediate SQL", "issuer":"DataCamp", "category":"SQL", "status":"Completed"},
    {"name":"MySQL", "issuer":"Analyst Builder", "category":"SQL", "status":"Completed"},
    {"name":"PostgreSQL", "issuer":"Codecademy", "category":"SQL", "status":"Completed"},
    {"name":"Excel for Business Analysts", "issuer":"Online Course", "category":"Excel", "status":"Completed"},
    {"name":"Data Analyst Associate", "issuer":"Online Course", "category":"Data Analytics", "status":"Completed"},
    {"name":"Power BI Desktop", "issuer":"Online Course", "category":"Power BI", "status":"Completed"},
    {"name":"Business Process Management", "issuer":"Online Course", "category":"Business Analysis", "status":"Completed"},
    {"name":"SEO", "issuer":"Online Course", "category":"Digital Marketing", "status":"Completed"},
    {"name":"Exploratory Data Analysis", "issuer":"Online Course", "category":"Data Analytics", "status":"Completed"}
]

skills = [
    {"Skill":"Python", "Category":"Data Analytics", "Level":"Intermediate", "Score":76}, {"Skill":"SQL", "Category":"Data Analytics", "Level":"Intermediate", "Score":72}, {"Skill":"Power BI", "Category":"Dashboarding", "Level":"Intermediate", "Score":75},
    {"Skill":"Excel", "Category":"Business Reporting", "Level":"Strong", "Score":88}, {"Skill":"Pandas", "Category":"Data Analytics", "Level":"Intermediate", "Score":80}, {"Skill":"NumPy", "Category":"Data Analytics", "Level":"Intermediate", "Score":74},
    {"Skill":"Scikit-learn", "Category":"Machine Learning", "Level":"Developing", "Score":64}, {"Skill":"Regression", "Category":"Machine Learning", "Level":"Intermediate", "Score":68}, {"Skill":"Classification", "Category":"Machine Learning", "Level":"Developing", "Score":62},
    {"Skill":"Clustering", "Category":"Machine Learning", "Level":"Developing", "Score":60}, {"Skill":"Business Analysis", "Category":"Business Analysis", "Level":"Strong", "Score":82}, {"Skill":"Process Mapping", "Category":"Business Analysis", "Level":"Intermediate", "Score":80},
    {"Skill":"Documentation", "Category":"Business Analysis", "Level":"Strong", "Score":86}, {"Skill":"Stakeholder Reporting", "Category":"Business Analysis", "Level":"Strong", "Score":84}, {"Skill":"KPI Reporting", "Category":"Business Reporting", "Level":"Intermediate", "Score":80},
    {"Skill":"Data Cleaning", "Category":"Data Quality", "Level":"Strong", "Score":84}, {"Skill":"Data Validation", "Category":"Data Quality", "Level":"Strong", "Score":82}, {"Skill":"EDA", "Category":"Data Analytics", "Level":"Strong", "Score":82},
    {"Skill":"AI Automation", "Category":"AI Automation", "Level":"Developing", "Score":58}, {"Skill":"n8n", "Category":"AI Automation", "Level":"Developing", "Score":55}, {"Skill":"LLM Tools", "Category":"AI Automation", "Level":"Developing", "Score":54},
    {"Skill":"RAG Concepts", "Category":"AI Automation", "Level":"Developing", "Score":50}, {"Skill":"APIs", "Category":"AI Automation", "Level":"Developing", "Score":52}, {"Skill":"QA Testing", "Category":"Quality Assurance", "Level":"Intermediate", "Score":74},
    {"Skill":"Market Research", "Category":"Business Development", "Level":"Intermediate", "Score":68}
]

education = [
    {"degree":"MBA Global / Master of Science in Data Analytics", "institution":"University of Newcastle", "location":"Australia", "status":"Current"},
    {"degree":"BBA Honors", "institution":"Iqra University", "location":"Pakistan", "status":"Completed"}
]

profile_summary = [
    {"area":"Data Analytics", "summary":"I work with Python, SQL, Excel, Power BI, data cleaning, EDA, KPI reporting, and dashboard-style analysis.", "source":"Portfolio projects and A. F. Ferguson data analyst role"},
    {"area":"Business Analysis", "summary":"I have worked on process tracking, documentation, stakeholder reporting, budget trackers, and business-focused project summaries.", "source":"PPL Community Development internship and project tracker work"},
    {"area":"Machine Learning", "summary":"My project work includes regression, classification, clustering, model evaluation, and feature interpretation.", "source":"AI job market, medical cost, soybean ML, heart risk, and clustering projects"},
    {"area":"AI Automation", "summary":"I am building my skills in n8n, LLM tools, RAG concepts, APIs, and workflow automation.", "source":"Certifications and roadmap case studies"},
    {"area":"Quality Assurance", "summary":"I have experience with web product testing, bug documentation, content quality review, and workflow testing.", "source":"Oigetit QA Analyst role"}
]

project_df = pd.DataFrame(projects)
experience_df = pd.DataFrame(experience)
cert_df = pd.DataFrame(certifications)
skills_df = pd.DataFrame(skills)
education_df = pd.DataFrame(education)
profile_summary_df = pd.DataFrame(profile_summary)


def assign_project_track(domain):
    business_analytics = ["Financial Analytics", "Marketing Analytics", "Business Reporting", "HR Analytics", "Customer Analytics", "Operations Analytics"]
    data_ml = ["Data Analytics", "Healthcare Analytics", "Agricultural Analytics", "Content Analytics", "Labour Market Analytics"]
    social_impact = ["Public Health Analytics", "Environmental Analytics", "CSR Analytics", "Public Data Analytics"]
    ai_systems = ["AI Automation", "AI and HR Systems", "Business Process Automation"]
    if domain in business_analytics:
        return "Business Analytics"
    if domain in data_ml:
        return "Data and Machine Learning"
    if domain in social_impact:
        return "Public and Social Impact Analytics"
    if domain in ai_systems:
        return "AI and Business Systems"
    return "General Analytics"

project_df["track"] = project_df["domain"].apply(assign_project_track)


def tags_html(tags, color="blue"):
    klass = {"blue":"badge", "purple":"badge-purple", "green":"badge-green", "orange":"badge-orange", "grey":"badge-grey"}.get(color, "badge")
    return "".join([f'<span class="{klass}">{tag}</span>' for tag in tags])


def status_badge(status):
    if status == "Completed":
        return "badge-green"
    if status == "In Progress":
        return "badge-orange"
    if status == "Roadmap":
        return "badge-grey"
    return "badge-purple"


def plotly_layout(fig):
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white", margin=dict(l=20, r=20, t=60, b=20))
    return fig


def render_project_card(project):
    st.markdown(f"""
    <div class="project-card">
        <h2>{project["name"]}</h2>
        <p class="subtle">{project["work"]}</p>
        <span class="{status_badge(project["status"])}">{project["status"]}</span>
        <span class="badge-purple">{project["role"]}</span>
        <span class="badge-green">{project["track"]}</span>
        <span class="badge">{project["domain"]}</span>
        <span class="badge-orange">{project["difficulty"]}</span>
        <br><br>{tags_html(project["tools"], "blue")}
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Project details"):
        t1, t2, t3 = st.tabs(["Overview", "Deliverables", "Dashboard Structure"])
        with t1:
            if project["status"] == "Completed":
                st.markdown(f"**Why I worked on it:** {project['context']}")
                st.markdown(f"**What I built:** {project['work']}")
                st.markdown(f"**Result:** {project['result']}")
                st.markdown(f"**Dataset:** {project['dataset']}")
            elif project["status"] == "In Progress":
                st.markdown(f"**Why I am working on it:** {project['context']}")
                st.markdown(f"**Current work:** {project['work']}")
                st.markdown(f"**Target outcome:** {project['result']}")
                st.markdown(f"**Dataset:** {project['dataset']}")
            else:
                st.markdown(f"**Case study concept:** {project['context']}")
                st.markdown(f"**Roadmap direction:** {project['work']}")
                st.markdown(f"**Expected value:** {project['result']}")
                st.markdown(f"**Dataset idea:** {project['dataset']}")
        with t2:
            st.markdown(f"**My role:** {project['role']}")
            st.markdown(f"**Deliverable:** {project['deliverable']}")
            st.markdown(f"**Evidence:** {project['evidence']}")
            st.markdown("**Tools:**")
            for tool in project["tools"]:
                st.markdown(f"- {tool}")
        with t3:
            st.markdown("**Dashboard sections:**")
            for page in project["pages"]:
                st.markdown(f"- {page}")
            st.markdown("**Metrics used:**")
            for kpi in project["kpis"]:
                st.markdown(f"- {kpi}")
        st.link_button("Open GitHub Repository", project["github"])

with st.sidebar:
    st.markdown("### Rubina Ahmed Mahar")
    st.caption("Business Analyst | Data Analytics | AI Automation")
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Process Calculator", "Role Fit", "Profile Summary", "Skills", "Experience", "Certifications", "Education", "Contact"],
        icons=["house", "grid", "calculator", "person-check", "stars", "bar-chart", "briefcase", "award", "mortarboard", "envelope"],
        default_index=0,
        styles={
            "container": {"padding":"0!important", "background-color":"transparent"},
            "icon": {"color":"#7dd3fc", "font-size":"18px"},
            "nav-link": {"font-size":"15px", "text-align":"left", "margin":"6px 0", "border-radius":"14px", "color":"#f8fafc", "background-color":"rgba(15,23,42,.55)"},
            "nav-link-selected": {"background":"linear-gradient(135deg,#2563eb,#7c3aed)", "color":"white", "font-weight":"800"},
        }
    )
    st.markdown("---")
    st.markdown("### Focus")
    st.markdown('<span class="badge">Data</span><span class="badge-purple">Business</span><span class="badge-green">AI</span>', unsafe_allow_html=True)

if selected == "Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <div class="eyebrow">Business Analyst | Data Analytics | AI Automation</div>
            <div class="hero-title">Rubina Ahmed Mahar</div>
            <div class="hero-subtitle">SQL, Python, Power BI, Excel, Machine Learning, LLMs, RAG, APIs, Cloud, Automation</div>
            <p class="hero-text">Selected work across analytics, reporting, business systems, machine learning, and automation.</p>
            <span class="badge">Python</span><span class="badge">SQL</span><span class="badge">Power BI</span><span class="badge">Excel</span>
            <span class="badge-purple">Business Analysis</span><span class="badge-purple">Business Systems</span>
            <span class="badge-green">AI Automation</span><span class="badge-green">Machine Learning</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Completed Projects", len(project_df[project_df["status"] == "Completed"]))
    m2.metric("In Progress", len(project_df[project_df["status"] == "In Progress"]))
    m3.metric("Roadmap", len(project_df[project_df["status"] == "Roadmap"]))
    m4.metric("Certifications", len(cert_df))

    st.markdown('<div class="section-title">What this portfolio shows</div>', unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="glass"><h3>Completed Work</h3><p class="subtle">Projects I have built using Python, Excel, Power BI, SQL, and machine learning workflows.</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="glass"><h3>Business Thinking</h3><p class="subtle">Each project is organised around a problem, dataset, tools, dashboard structure, and business value.</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="glass"><h3>Automation Direction</h3><p class="subtle">My current direction includes AI automation, LLM workflows, RAG concepts, APIs, and business systems.</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Overview</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1.1, 1])
    with c1:
        domain_count = project_df["domain"].value_counts().reset_index()
        domain_count.columns = ["Domain", "Projects"]
        fig = px.bar(domain_count, x="Domain", y="Projects", color="Domain", title="Projects by Domain", template="plotly_dark")
        fig.update_layout(showlegend=False)
        st.plotly_chart(plotly_layout(fig), use_container_width=True)
    with c2:
        status_count = project_df["status"].value_counts().reset_index()
        status_count.columns = ["Status", "Projects"]
        fig2 = px.pie(status_count, names="Status", values="Projects", title="Project Status", template="plotly_dark", hole=.58)
        st.plotly_chart(plotly_layout(fig2), use_container_width=True)

    st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)
    featured_names = ["AI Job Market", "HR Analytics", "Project Tracker", "Process Automation"]
    featured = project_df[project_df["short_name"].isin(featured_names)]
    cols = st.columns(4)
    for col, (_, project) in zip(cols, featured.iterrows()):
        with col:
            st.markdown(f'<div class="glass"><h3>{project["short_name"]}</h3><p class="small-muted">{project["track"]}</p><p class="subtle">{project["result"]}</p><span class="{status_badge(project["status"])}">{project["status"]}</span></div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    with f1:
        role_filter = st.multiselect("Role focus", sorted(project_df["role"].unique()), placeholder="Select role")
    with f2:
        track_filter = st.multiselect("Project track", sorted(project_df["track"].unique()), placeholder="Select track")
    with f3:
        domain_filter = st.multiselect("Domain", sorted(project_df["domain"].unique()), placeholder="Select domain")
    search = st.text_input("Search", placeholder="Search by topic, tool, domain, or project name")
    filtered = project_df.copy()
    if role_filter:
        filtered = filtered[filtered["role"].isin(role_filter)]
    if track_filter:
        filtered = filtered[filtered["track"].isin(track_filter)]
    if domain_filter:
        filtered = filtered[filtered["domain"].isin(domain_filter)]
    if search:
        s = search.lower()
        filtered = filtered[filtered.apply(lambda row: s in str(row["name"]).lower() or s in str(row["short_name"]).lower() or s in str(row["domain"]).lower() or s in str(row["track"]).lower() or s in str(row["tools"]).lower() or s in str(row["context"]).lower() or s in str(row["work"]).lower(), axis=1)]
    completed_tab, progress_tab, roadmap_tab = st.tabs(["Completed Work", "In Progress", "Case Study Roadmap"])
    with completed_tab:
        completed_projects = filtered[filtered["status"] == "Completed"]
        st.markdown(f"Showing **{len(completed_projects)}** completed project(s).")
        for _, project in completed_projects.iterrows():
            render_project_card(project)
    with progress_tab:
        progress_projects = filtered[filtered["status"] == "In Progress"]
        st.markdown(f"Showing **{len(progress_projects)}** in-progress project(s).")
        for _, project in progress_projects.iterrows():
            render_project_card(project)
    with roadmap_tab:
        roadmap_projects = filtered[filtered["status"] == "Roadmap"]
        st.markdown(f"Showing **{len(roadmap_projects)}** roadmap case study concept(s).")
        for _, project in roadmap_projects.iterrows():
            render_project_card(project)

elif selected == "Process Calculator":
    st.markdown('<div class="section-title">Process Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-panel"><h2>Business Process Savings Calculator</h2><p class="subtle">I created this calculator to estimate time savings, cost savings, and quality improvement for repetitive workflows.</p></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Inputs")
        monthly_cases = st.number_input("Cases processed per month", min_value=50, max_value=100000, value=1200, step=50)
        minutes_per_case = st.number_input("Manual minutes per case", min_value=1, max_value=240, value=18, step=1)
        hourly_cost = st.number_input("Average staff cost per hour", min_value=10, max_value=250, value=35, step=5)
        automation_rate = st.slider("Automation coverage", min_value=5, max_value=95, value=45, step=5)
        error_rate_before = st.slider("Current error rate", min_value=1, max_value=40, value=12, step=1)
        error_reduction = st.slider("Expected error reduction", min_value=5, max_value=90, value=50, step=5)
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
        impact_level, impact_badge = "High impact", "badge-green"
    elif automation_rate >= 40:
        impact_level, impact_badge = "Moderate impact", "badge-orange"
    else:
        impact_level, impact_badge = "Early opportunity", "badge-purple"
    with col2:
        st.markdown("### Results")
        m1, m2 = st.columns(2)
        m1.metric("Manual Hours / Month", f"{total_manual_hours:,.0f}")
        m2.metric("Hours Saved / Month", f"{automated_hours:,.0f}")
        m3, m4 = st.columns(2)
        m3.metric("Monthly Cost Saved", f"${monthly_cost_saved:,.0f}")
        m4.metric("Annual Cost Saved", f"${annual_cost_saved:,.0f}")
        m5, m6 = st.columns(2)
        m5.metric("Errors Reduced / Month", f"{errors_reduced:,.0f}")
        m6.metric("Remaining Manual Hours", f"{remaining_manual_hours:,.0f}")
        st.markdown(f'<div class="project-card"><h3>Impact Summary</h3><p class="subtle">Estimated monthly saving: <b>${monthly_cost_saved:,.0f}</b><br>Estimated annual saving: <b>${annual_cost_saved:,.0f}</b></p><span class="{impact_badge}">{impact_level}</span></div>', unsafe_allow_html=True)
    comparison_data = pd.DataFrame({"Metric": ["Monthly manual hours", "Monthly labour cost", "Error rate", "Estimated errors per month"], "Before": [round(total_manual_hours, 2), round(monthly_cost_before, 2), round(error_rate_before, 2), round(errors_before, 2)], "After": [round(remaining_manual_hours, 2), round(monthly_cost_before - monthly_cost_saved, 2), round(error_rate_after, 2), round(errors_after, 2)]})
    st.markdown('<div class="section-title">Before and After</div>', unsafe_allow_html=True)
    st.dataframe(comparison_data, use_container_width=True, hide_index=True, column_config={"Metric": st.column_config.TextColumn("Metric", width="medium"), "Before": st.column_config.NumberColumn("Before", format="%.2f"), "After": st.column_config.NumberColumn("After", format="%.2f")})
    fig = px.bar(comparison_data, x="Metric", y=["Before", "After"], barmode="group", title="Before and After Comparison", template="plotly_dark")
    st.plotly_chart(plotly_layout(fig), use_container_width=True)
    st.download_button("Download Calculation Summary", data=comparison_data.to_csv(index=False).encode("utf-8"), file_name="process_savings_summary.csv", mime="text/csv", use_container_width=True)

elif selected == "Role Fit":
    st.markdown('<div class="section-title">Role Fit</div>', unsafe_allow_html=True)
    role = st.selectbox("Target role", ["Data Analyst", "Business Analyst", "ICT Business Analyst", "AI Automation Analyst", "Marketing Analyst", "Operations Analyst"])
    role_projects = project_df[project_df["role"] == role]
    st.markdown(f'<div class="info-panel"><h2>{role}</h2><p class="subtle">Projects aligned with this target role.</p></div>', unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    r1.metric("Matching Projects", len(role_projects))
    r2.metric("Completed", len(role_projects[role_projects["status"] == "Completed"]))
    r3.metric("Roadmap", len(role_projects[role_projects["status"] == "Roadmap"]))
    for _, project in role_projects.iterrows():
        render_project_card(project)

elif selected == "Profile Summary":
    st.markdown('<div class="section-title">Profile Summary</div>', unsafe_allow_html=True)
    for _, item in profile_summary_df.iterrows():
        st.markdown(f'<div class="project-card"><h3>{item["area"]}</h3><p class="subtle">{item["summary"]}</p><p class="small-muted">{item["source"]}</p></div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    category_filter = st.multiselect("Skill category", sorted(skills_df["Category"].unique()), placeholder="Select skill category")
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
                    st.markdown(f'<div class="glass"><h3>{skill["Skill"]}</h3><p class="small-muted">{skill["Category"]}</p><div class="stat-number">{skill["Level"]}</div><div class="stat-label">Level</div></div>', unsafe_allow_html=True)
    with tab2:
        fig = px.bar(skill_view, x="Score", y="Skill", color="Category", orientation="h", title="Technical Skills by Category", template="plotly_dark", range_x=[0, 100])
        st.plotly_chart(plotly_layout(fig), use_container_width=True)
    with tab3:
        display_skills = skill_view[["Skill", "Category", "Level"]]
        st.dataframe(display_skills, use_container_width=True, hide_index=True)

elif selected == "Experience":
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
    for item in experience:
        st.markdown(f'<div class="timeline"><h2>{item["role"]}</h2><p><b>{item["company"]}</b></p><p class="small-muted">{item["duration"]} | {item["location"]}</p><p class="subtle">{item["details"]}</p>{tags_html(item["tags"], "blue")}</div>', unsafe_allow_html=True)

elif selected == "Certifications":
    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
    cert_category = st.multiselect("Certification category", sorted(cert_df["category"].unique()), placeholder="Select category")
    issuer_filter = st.multiselect("Issuer", sorted(cert_df["issuer"].unique()), placeholder="Select issuer")
    status_filter = st.multiselect("Status", sorted(cert_df["status"].unique()), placeholder="Select status")
    cert_view = cert_df.copy()
    if cert_category:
        cert_view = cert_view[cert_view["category"].isin(cert_category)]
    if issuer_filter:
        cert_view = cert_view[cert_view["issuer"].isin(issuer_filter)]
    if status_filter:
        cert_view = cert_view[cert_view["status"].isin(status_filter)]
    c1, c2 = st.columns([1.1, 1])
    with c1:
        cert_count = cert_df["category"].value_counts().reset_index()
        cert_count.columns = ["Category", "Count"]
        fig = px.bar(cert_count, x="Category", y="Count", color="Category", title="Certifications by Category", template="plotly_dark")
        fig.update_layout(showlegend=False)
        st.plotly_chart(plotly_layout(fig), use_container_width=True)
    with c2:
        status_count = cert_df["status"].value_counts().reset_index()
        status_count.columns = ["Status", "Count"]
        fig2 = px.pie(status_count, names="Status", values="Count", title="Certification Status", template="plotly_dark", hole=.55)
        st.plotly_chart(plotly_layout(fig2), use_container_width=True)
    st.markdown(f"Showing **{len(cert_view)}** certification(s).")
    rows = [cert_view.iloc[i:i+2] for i in range(0, len(cert_view), 2)]
    for row in rows:
        cols = st.columns(2)
        for col, (_, cert) in zip(cols, row.iterrows()):
            status_class = "badge-green" if cert["status"] == "Completed" else "badge-orange"
            with col:
                st.markdown(f'<div class="glass"><h3>{cert["name"]}</h3><p class="small-muted">{cert["issuer"]}</p><span class="badge-purple">{cert["category"]}</span><span class="{status_class}">{cert["status"]}</span></div>', unsafe_allow_html=True)

elif selected == "Education":
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    for _, item in education_df.iterrows():
        st.markdown(f'<div class="project-card"><h2>{item["degree"]}</h2><p><b>{item["institution"]}</b></p><p class="small-muted">{item["location"]}</p><span class="badge-green">{item["status"]}</span></div>', unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero"><div class="hero-content"><div class="eyebrow">Contact</div><div class="hero-title">Let’s Connect</div><p class="hero-text">Open to entry-level and graduate roles in data analytics, business analysis, reporting, business systems, and AI automation support.</p></div></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/rubina-ahmed-mahar-b03b39220", use_container_width=True)
    with c2:
        st.link_button("GitHub", "https://github.com/rubinaahmedmahar2002-arch", use_container_width=True)
    with c3:
        st.link_button("Email", "mailto:rubinaahmed301@gmail.com", use_container_width=True)
    st.markdown('<div class="project-card"><h3>Focus Areas</h3><span class="badge">Data Analytics</span><span class="badge">Dashboard Reporting</span><span class="badge-purple">Business Analysis</span><span class="badge-purple">Business Systems</span><span class="badge-green">AI Automation Support</span></div>', unsafe_allow_html=True)
