# Multi-Domain Intelligence Platform

**Student Name:**  Reshika Sahadew
**Course Title:** BSc Computer Science (Systems Engineering)
**Module Code:** CST1510

## Project Overview
This project implements a **Multi-Domain Intelligence Platform** developed using Python and Streamlit.  
The platform is designed to ingest, process, analyse, and interpret structured datasets in order to support **data-driven decision making** across multiple technical domains.

The primary implementation focuses on the **Cybersecurity Intelligence domain**, developed incrementally according to the coursework specification from **Week 7 to Week 12**, integrating software engineering principles, analytics, and AI-assisted insights.

---

## Project Objectives
- Apply structured software development practices
- Demonstrate Object-Oriented Programming (OOP)
- Implement full CRUD functionality with persistent storage
- Perform descriptive and trend-based data analytics
- Integrate AI-style decision support and interpretation
- Demonstrate both **theoretical understanding** and **practical implementation**

---

## Technologies Used
- Python 3
- Streamlit
- Pandas
- Matplotlib
- Git & GitHub

---

## System Architecture
The system follows a **layered, modular architecture** to ensure maintainability, scalability, and clarity.

models/ → Data models using OOP
services/ → Business logic, analytics, and AI reasoning
data/ → Persistent structured data storage (CSV)
app.py → Streamlit user interface and controller
README.md → Project documentation


### Architectural Layers
- **Model Layer**  
  Defines structured data entities (e.g. CyberIncident)

- **Service Layer**  
  Handles CRUD operations, analytics, trend computation, and AI-assisted insights.

- **Presentation Layer**  
  Streamlit-based interface for interaction, visualisation, and decision support.

---

## Weekly Implementation Summary

### Week 7 – Environment Setup & Foundations
- Python environment configuration
- Installation of required libraries
- Project folder structure setup
- Version control initialization using Git
- Introduction to Streamlit for UI development

---

### Week 8 – Core Platform & CRUD Operations
- Dataset ingestion from CSV files
- Dashboard layout and navigation
- Full CRUD functionality (Create, Read, Update, Delete)
- Initial data visualisation (incident severity and status)

---

### Week 9 – Software Engineering & OOP
- Object-Oriented Programming using dedicated model classes
- Separation of concerns via service layers
- Refactoring logic out of the UI layer
- Improved code maintainability and modularity

---

### Week 10 – Intelligent Dashboard & KPIs
- Implementation of Key Performance Indicators (KPIs)
- Aggregated metrics for operational monitoring
- Risk scoring logic for cybersecurity incidents
- Enhanced dashboard presentation and structure

---

### Week 11 – Advanced Analytics & Trend Analysis
- Time-based analysis of cybersecurity incidents
- Trend visualisation using line charts
- Severity distribution analysis
- Analytical interpretation of observed trends

---

### Week 12 – AI-Assisted Insights & Evaluation
- Automated risk and operational health assessment
- AI-style insight generation using explainable rule-based logic
- Decision support recommendations
- Fully integrated and polished cybersecurity intelligence dashboard

---

## AI and Analytics Approach
The platform integrates **AI-assisted analytics** using transparent, rule-based logic rather than complex machine learning models.  
This approach ensures interpretability, academic defensibility, and meaningful decision support.

Examples include:
- Cyber risk level assessment
- Incident response health evaluation
- Automated recommendations for mitigation and prioritisation

---

## Data Persistence and Database Concept
Cybersecurity incident data is stored using **structured CSV files**, designed to mirror relational database tables.  
All data access and manipulation are abstracted through a service layer, providing full CRUD functionality and enabling seamless migration to a SQL-based database if required.

---

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the project directory:

cd multi-domain-intelligence-platform


3. Install dependencies:

pip install -r requirements.txt


4. Run the application:

streamlit run app.py



