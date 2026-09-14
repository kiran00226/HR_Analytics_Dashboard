# HR_Analytics_Dashboard
Interactive HR Analytics Dashboard built using Python, DAX &amp; Power BI for data-driven workforce insights.

<h2>HR Analytics Dashboard 📊</h2>

<h3>📌 Project Overview </h3>

The HR Analytics Dashboard is a Business Intelligence project designed to analyze and monitor key HR operations using Python, Pandas, NumPy, and Microsoft Power BI.

The project works with a synthetic but realistic Indian HR dataset containing employee, recruitment, attendance, leave, performance, and payroll information. The dataset includes intentional data-quality issues to simulate a real-world data analytics workflow.

---

<h3>🎯 Project Objectives</h3>

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

## 🔄 Project Workflow

Raw Data → Data Cleaning → Cleaned Data → Power BI Data Modeling → Dashboard Development → Insights

### 1️⃣ Raw Data

The original HR datasets contain employee, recruitment, attendance, leave, performance, payroll, and department-related information.

The raw datasets include:

- Departments
- Employees
- Job Applications
- Attendance
- Leaves
- Performance Reviews
- Payroll

The raw files are kept unchanged for reference and comparison.

<a href="https://github.com/kiran00226/HR_Analytics_Dashboard/tree/5a6faca96fd68e67f17219d8f6100f30051bcaf5/output"> Click Here</a>


### 2️⃣ Data Cleaning Using Python

Python and Pandas were used to clean and prepare the raw HR datasets for analysis.

The cleaning process included:

- Handling missing values
- Removing duplicate records
- Fixing inconsistent data formats
- Validating email and phone numbers
- Correcting data types
- Handling invalid values and outliers
- Checking foreign key relationships

<a href="https://github.com/kiran00226/HR_Analytics_Dashboard/blob/4db4534869be37f31917db5a008409696932a26d/HR_Analytics.ipynb"> Click Here</a>

### 3️⃣ Cleaned Data

After the cleaning process, the validated datasets were saved as cleaned CSV files.

These cleaned datasets were used for further analysis and Power BI dashboard development.

<a href="https://github.com/kiran00226/HR_Analytics_Dashboard/tree/51547963a14cc86765551710f64d6144fa7f1d49/cleaned%20file"> Click Here</a>

### 4️⃣ Power BI Data Modeling

The cleaned CSV files were imported into Power BI and relationships were created between the tables using common keys such as:

- `department_id`
- `employee_id`

The data model was structured to support integrated HR analysis.


### 5️⃣ Dashboard Development

Interactive HR dashboards were created in Power BI using:

- DAX Measures
- KPI Cards
- Charts
- Tables
- Slicers

The dashboards cover:

- Employee Analytics
- Recruitment Analytics
- Attendance Analytics
- Performance Analytics
- Payroll Analytics
- Executive Dashboard

<a href="https://github.com/kiran00226/HR_Analytics_Dashboard/tree/a2a6c7ab7169268d8204089c812461bce80b39bf/Dashboard"> Click Here</a>

### 6️⃣ Insights & Analysis

The final dashboard helps analyze workforce trends and provides insights into:

- Employee demographics
- Recruitment performance
- Attendance and absenteeism
- Employee performance
- Payroll costs
- Department-wise HR metrics

These insights can support data-driven HR decision-making.

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

<a href="https://github.com/kiran00226/HR_Analytics_Dashboard/blob/5d504e6a9e0ba77452e47679900917c533c0237f/Dashboard%20Screenshots/Employees%20Dashboard.png"><button>Click Here</button</a>

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
📌 Conclusion

This project demonstrates an end-to-end HR Analytics and Business Intelligence workflow, starting from raw and imperfect datasets and transforming them into an interactive Power BI dashboard.

The dashboard helps analyze workforce demographics, recruitment performance, attendance, employee performance, payroll, and key executive-level HR KPIs.


---

📌 Conclusion

This project demonstrates an end-to-end HR Analytics and Business Intelligence workflow, starting from raw and imperfect datasets and transforming them into an interactive Power BI dashboard.

The dashboard helps analyze workforce demographics, recruitment performance, attendance, employee performance, payroll, and key executive-level HR KPIs.

---

👩‍💻 Author

Kiran
Data Analytics | Python | SQL | Power BI
📌 Project: HR Analytics Dashboard
