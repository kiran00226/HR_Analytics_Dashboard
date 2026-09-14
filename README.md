# HR_Analytics_Dashboard
Interactive HR Analytics Dashboard built using Python, DAX &amp; Power BI for data-driven workforce insights.

<h2>HR Analytics Dashboard </h2> 📊

📌 <h3> Project Overview </h3>

The HR Analytics Dashboard is a Business Intelligence project designed to analyze and monitor key HR operations using Python, Pandas, NumPy, and Microsoft Power BI.

The project works with a synthetic but realistic Indian HR dataset containing employee, recruitment, attendance, leave, performance, and payroll information. The dataset includes intentional data-quality issues to simulate a real-world data analytics workflow.

The project follows a complete analytics process:

Raw Data → Data Cleaning → Data Validation → Data Modeling → Power BI Dashboard → HR Insights

---

🎯 Project Objectives

- Clean and prepare raw HR data using Python
- Identify and handle missing values and duplicate records
- Validate email and phone-number formats
- Standardize inconsistent text data
- Detect and handle numerical outliers
- Check foreign-key relationships and data integrity
- Build a relational/star-schema-friendly data model
- Create interactive Power BI dashboards
- Generate meaningful HR insights for business decision-making

---

🗂️ Dataset

The project contains 7 interconnected CSV files:

Dataset| Description
"departments.csv"| Department master/dimension table
"employees.csv"| Employee information
"job_applications.csv"| Recruitment and job application records
"attendance.csv"| Employee attendance records
"leaves.csv"| Employee leave records
"performance_reviews.csv"| Employee performance reviews
"payroll.csv"| Monthly employee payroll records

The project brief defines "departments" and "employees" as dimension tables, while "job_applications", "attendance", "leaves", "performance_reviews", and "payroll" act as fact/transaction tables.

---

🧹 Data Cleaning

Python was used to clean and prepare the datasets before importing them into Power BI.

Cleaning activities included:

- Dataset shape and data-type inspection
- Missing-value analysis
- Duplicate-record detection
- Email validation
- Phone-number validation
- Text standardization
- Numerical outlier detection
- Foreign-key validation
- Data consistency checks
- Creation of cleaned CSV files

The project brief specifically identifies missing values, duplicates, invalid contact information, inconsistent casing, numerical outliers, and broken foreign keys as intentional data-quality issues.

---

🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Microsoft Power BI
- DAX
- CSV
- GitHub

---

📊 Power BI Dashboard

The Power BI report is organized into the following analytical modules.

1. 👥 Employee Analytics

This section provides insights into the organization's workforce, including:

- Total employee headcount
- Employee tenure
- Gender distribution
- Department-wise employee count
- Employee experience bands
- Employee age-group distribution

The experience analysis uses the following bands:

- 0–2 years
- 3–5 years
- 6–10 years
- 10+ years

---

2. 🎯 Recruitment Analytics

The Recruitment Dashboard analyzes the organization's hiring pipeline and recruitment sources.

Key analysis includes:

- Total job applications
- Application trend over time
- Shortlisted candidates vs. total applications
- Recruitment funnel
- Applied → Shortlisted → Interviewed → Hired
- Recruitment source effectiveness
- Hiring success by department
- Hiring success by recruitment source

---

3. 🕒 Attendance Analytics

The Attendance Dashboard provides insights into employee attendance and workforce availability.

Key analysis includes:

- Daily attendance trends
- Monthly attendance summary by department
- Leave analysis by type and department
- Absenteeism rate
- Overtime hours by department

The absenteeism rate is calculated based on:

Absent Days / Total Working Days

---

4. ⭐ Performance Analytics

The Performance Dashboard analyzes employee performance and productivity.

Key analysis includes:

- Performance rating distribution
- Department-wise average performance
- Top-performing employees
- Performance rating and productivity score
- Productivity trend by review period
- Promotion recommendation analysis

---

5. 💰 Payroll Analytics

The Payroll Dashboard provides insights into employee compensation and payroll costs.

Key analysis includes:

- Monthly payroll cost trend
- Salary distribution
- Department-wise payroll cost
- Bonus analysis
- Employee cost analysis

Employee cost is analyzed using:

Basic Salary + HRA + Bonus − Deductions

---

6. 📈 Executive Dashboard

The Executive Dashboard summarizes important HR metrics through KPI cards.

Key KPIs

- Total Employees
- Active Employees
- Total Departments
- Attrition Rate
- Average Salary
- Average Employee Satisfaction Score
- Hiring Rate
- Month-over-Month Workforce Growth

The project brief defines attrition as:

(Resigned + Terminated) / Total Employees

and hiring rate as:

Hired / Total Applications

---

🔗 Data Model

The Power BI data model follows a star-schema-friendly structure.

Main relationships

Departments
     │
     ├────────── Employees
     │              │
     │              ├── Attendance
     │              ├── Leaves
     │              ├── Performance Reviews
     │              └── Payroll
     │
     └────────── Job Applications

The project brief specifies one-to-many relationships from departments to employees/job applications and from employees to attendance, leaves, performance reviews, and payroll.

---

📁 Project Structure

HR-Analytics-Project/
│
├── output/
│   └── Raw CSV files
│
├── notebooks/
│   └── Python data-cleaning notebooks
│
├── cleaned_data/
│   └── Cleaned CSV files
│
├── dashboard/
│   └── HR Analytics Power BI Dashboard
│
└── README.md

This structure follows the organization suggested in the project brief.

---

💡 Key Learning Outcomes

Through this project, I worked on:

- Real-world style data cleaning
- Exploratory data analysis
- Data validation
- Data transformation
- Relational data modeling
- Power BI dashboard development
- DAX measures and KPIs
- HR analytics
- Business-oriented data visualization
- Converting raw data into actionable insights

---

🚀 Project Workflow

Raw HR CSV Files
       ↓
Python Data Cleaning
       ↓
Data Validation
       ↓
Cleaned CSV Files
       ↓
Power BI Data Model
       ↓
DAX Measures & KPIs
       ↓
Interactive HR Dashboard
       ↓
Business Insights

---

📌 Conclusion

This project demonstrates an end-to-end HR Analytics and Business Intelligence workflow, starting from raw and imperfect datasets and transforming them into an interactive Power BI dashboard.

The dashboard helps analyze workforce demographics, recruitment performance, attendance, employee performance, payroll, and key executive-level HR KPIs.
