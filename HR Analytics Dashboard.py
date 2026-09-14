"""
HR Analytics Dashboard - Raw Dataset Generator
Generates realistic, relational, dirty Indian HR datasets as CSV files.
"""

import os
import csv
import random
import string
from datetime import datetime, timedelta

random.seed(7)

OUTPUT_DIR = "output"

# ---------------------------------------------------------------------------
# Reference data (Indian context)
# ---------------------------------------------------------------------------

FIRST_NAMES_M = ["Aarav","Vivaan","Aditya","Vihaan","Arjun","Reyansh","Krishna","Ishaan",
                 "Rohan","Karan","Aman","Rahul","Saurabh","Nikhil","Manish","Suresh",
                 "Ramesh","Ajay","Vikram","Deepak","Anil","Sanjay","Gaurav","Naveen"]
FIRST_NAMES_F = ["Aadhya","Ananya","Diya","Isha","Kavya","Myra","Riya","Saanvi",
                  "Priya","Neha","Pooja","Anjali","Sneha","Kritika","Shreya","Meera",
                  "Divya","Nisha","Swati","Rekha","Sunita","Kavita","Sarika","Ritu"]
LAST_NAMES = ["Sharma","Verma","Gupta","Singh","Kumar","Patel","Reddy","Nair","Iyer",
              "Menon","Rao","Mishra","Yadav","Chaudhary","Joshi","Malhotra","Kapoor",
              "Agarwal","Bansal","Chopra","Desai","Ghosh","Bose","Pillai","Shetty"]
CITIES_STATES = [
    ("Delhi","Delhi"), ("Mumbai","Maharashtra"), ("Pune","Maharashtra"),
    ("Bengaluru","Karnataka"), ("Hyderabad","Telangana"), ("Chennai","Tamil Nadu"),
    ("Kolkata","West Bengal"), ("Ahmedabad","Gujarat"), ("Jaipur","Rajasthan"),
    ("Lucknow","Uttar Pradesh"), ("Ghaziabad","Uttar Pradesh"), ("Noida","Uttar Pradesh"),
    ("Nagpur","Maharashtra"), ("Indore","Madhya Pradesh"), ("Chandigarh","Chandigarh"),
    ("Surat","Gujarat"), ("Coimbatore","Tamil Nadu")
]
DEPARTMENTS = [
    ("Engineering","Software & Product Engineering"), ("Sales","Sales & Business Development"),
    ("Marketing","Marketing & Brand"), ("Human Resources","People Operations"),
    ("Finance","Finance & Accounts"), ("Customer Support","Customer Success"),
    ("Operations","Operations & Logistics"), ("IT Infrastructure","IT & Systems"),
    ("Legal","Legal & Compliance"), ("Procurement","Procurement & Vendor Management"),
    ("Quality Assurance","QA & Testing"), ("Administration","Admin & Facilities")
]
DESIGNATIONS = ["Associate","Senior Associate","Analyst","Senior Analyst","Executive",
                "Team Lead","Assistant Manager","Manager","Senior Manager","Deputy General Manager",
                "General Manager","Vice President","Intern","Consultant"]
EDUCATION = ["B.Tech","B.Com","B.A.","B.Sc","M.Tech","MBA","M.Com","M.Sc","Diploma","PhD"]
MARITAL_STATUS = ["Single","Married","Divorced"]
EMP_STATUS = ["Active","Active","Active","Active","Resigned","Terminated","On Notice Period"]
RECRUITMENT_SOURCES = ["Naukri","LinkedIn","Referral","Campus Placement","Indeed",
                        "Company Website","Walk-in","Recruitment Agency","Internshala"]
APPLICATION_STATUS = ["Applied","Shortlisted","Interviewed","Hired","Rejected","On Hold"]
APPLICATION_STATUS_WEIGHTS = [0.30, 0.22, 0.16, 0.10, 0.18, 0.04]
ATTENDANCE_STATUS = ["Present","Absent","On Leave","Work From Home","Half Day"]
ATTENDANCE_STATUS_WEIGHTS = [0.72, 0.06, 0.09, 0.10, 0.03]
LEAVE_TYPES = ["Casual Leave","Sick Leave","Earned Leave","Maternity Leave","Paternity Leave","Unpaid Leave"]
LEAVE_STATUS = ["Approved","Pending","Rejected"]
PERFORMANCE_PERIODS = ["2024-H1","2024-H2","2025-H1","2025-H2","2026-H1"]
PROMOTION_FLAGS = ["Yes","No","No","No","No"]
PAYMENT_MODE = ["Bank Transfer","Cheque","Cash"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def rand_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def make_name(gender: str) -> str:
    first = random.choice(FIRST_NAMES_M if gender == "Male" else FIRST_NAMES_F)
    last = random.choice(LAST_NAMES)
    return f"{first} {last}"

def make_phone(dirty=False):
    if dirty:
        choice = random.random()
        if choice < 0.3:
            return "".join(random.choices(string.digits, k=random.choice([5, 7, 15])))
        elif choice < 0.6:
            return "123456" + str(random.randint(1000, 9999))
        elif choice < 0.8:
            return ""
        else:
            return "+91-" + "".join(random.choices(string.digits, k=6))
    return "+91" + str(random.randint(6, 9)) + "".join(random.choices(string.digits, k=9))

def make_email(name, dirty=False):
    base = name.lower().replace(" ", ".")
    domain = random.choice(["gmail.com","yahoo.com","outlook.com","hotmail.com","rediffmail.com"])
    if dirty:
        choice = random.random()
        if choice < 0.35:
            return ""
        elif choice < 0.6:
            return f"{base}{domain}"
        elif choice < 0.8:
            return f"{base}@{domain.split('.')[0]}"
        else:
            return f"{base}@@{domain}"
    return f"{base}{random.randint(1,999)}@{domain}"

def messy_text(value):
    choice = random.random()
    if choice < 0.4:
        return value.upper()
    elif choice < 0.7:
        return value.lower()
    elif choice < 0.85:
        return f"  {value}  "
    return value

def maybe_blank(value, prob=0.05):
    return "" if random.random() < prob else value

def write_csv(filename, fieldnames, rows):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Generated {filename} ({len(rows)} rows)")

def inject_duplicates(rows, rate=0.02):
    n_dupes = max(1, int(len(rows) * rate))
    dupes = [dict(random.choice(rows)) for _ in range(n_dupes)]
    return rows + dupes

def broken_fk(valid_ids, prefix, rate=0.03):
    if random.random() < rate:
        return f"{prefix}{random.randint(90000,99999)}"
    return random.choice(valid_ids)

# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def generate_departments():
    rows = []
    for i, (name, desc) in enumerate(DEPARTMENTS, start=1):
        rows.append({
            "department_id": f"DEP{i:03d}",
            "department_name": name,
            "description": desc,
            "budget_inr": random.choice([2000000, 3500000, 5000000, 7500000, 10000000, 15000000])
        })
    return rows

def generate_employees(dept_ids, n=3200):
    rows = []
    for i in range(1, n + 1):
        emp_id = f"EMP{i:05d}"
        gender = random.choice(["Male", "Female", "Other"])
        name = make_name(gender if gender != "Other" else random.choice(["Male", "Female"]))
        city, state = random.choice(CITIES_STATES)
        age = random.randint(21, 60)
        dob_year = 2026 - age
        dob = datetime(dob_year, random.randint(1, 12), random.randint(1, 28))
        joining = rand_date(datetime(2015, 1, 1), datetime(2026, 6, 30))
        status = random.choice(EMP_STATUS)
        exit_date = ""
        if status in ("Resigned", "Terminated"):
            exit_candidate = joining + timedelta(days=random.randint(90, 2500))
            if exit_candidate < datetime(2026, 7, 22):
                exit_date = exit_candidate.strftime("%Y-%m-%d")
        experience_years = round(random.uniform(0, 30), 1)
        base_salary = random.choice([25000, 35000, 45000, 60000, 80000, 100000, 130000,
                                      160000, 200000, 250000, 320000])
        row = {
            "employee_id": emp_id,
            "employee_name": messy_text(name) if random.random() < 0.06 else name,
            "gender": gender,
            "dob": dob.strftime("%Y-%m-%d"),
            "age": age,
            "marital_status": random.choice(MARITAL_STATUS),
            "city": city,
            "state": state,
            "phone": make_phone(dirty=random.random() < 0.08),
            "email": make_email(name, dirty=random.random() < 0.08),
            "department_id": random.choice(dept_ids),
            "designation": random.choice(DESIGNATIONS),
            "education": random.choice(EDUCATION),
            "experience_years": experience_years,
            "date_of_joining": joining.strftime("%Y-%m-%d"),
            "employment_status": status,
            "exit_date": exit_date,
            "monthly_basic_salary": base_salary,
            "satisfaction_score": random.randint(1, 5)
        }
        if random.random() < 0.01:
            row["age"] = random.choice([16, 17, 85, 99])
        if random.random() < 0.01:
            row["experience_years"] = round(random.uniform(35, 50), 1)
        row["satisfaction_score"] = maybe_blank(row["satisfaction_score"], prob=0.04)
        rows.append(row)
    rows = inject_duplicates(rows, rate=0.02)
    return rows

def generate_job_applications(dept_ids, n=26000):
    rows = []
    for i in range(1, n + 1):
        gender = random.choice(["Male", "Female", "Other"])
        name = make_name(gender if gender != "Other" else random.choice(["Male", "Female"]))
        app_date = rand_date(datetime(2023, 1, 1), datetime(2026, 7, 22))
        status = random.choices(APPLICATION_STATUS, weights=APPLICATION_STATUS_WEIGHTS)[0]
        row = {
            "application_id": f"APP{i:06d}",
            "candidate_name": messy_text(name) if random.random() < 0.05 else name,
            "gender": gender,
            "department_id": broken_fk(dept_ids, "DEP", rate=0.02),
            "position_applied": random.choice(DESIGNATIONS),
            "recruitment_source": random.choice(RECRUITMENT_SOURCES),
            "application_date": app_date.strftime("%Y-%m-%d"),
            "years_of_experience": round(random.uniform(0, 20), 1),
            "expected_salary": random.choice([20000, 30000, 45000, 60000, 90000, 120000, 180000]),
            "status": status,
            "phone": make_phone(dirty=random.random() < 0.08),
            "email": make_email(name, dirty=random.random() < 0.08),
        }
        if random.random() < 0.01:
            row["years_of_experience"] = round(random.uniform(25, 40), 1)
        rows.append(row)
    rows = inject_duplicates(rows, rate=0.015)
    return rows

def generate_attendance(employee_ids, n=42000):
    rows = []
    for i in range(1, n + 1):
        att_date = rand_date(datetime(2025, 1, 1), datetime(2026, 7, 22))
        status = random.choices(ATTENDANCE_STATUS, weights=ATTENDANCE_STATUS_WEIGHTS)[0]
        overtime = 0
        if status == "Present" and random.random() < 0.2:
            overtime = round(random.uniform(0.5, 4), 1)
        row = {
            "attendance_id": f"ATT{i:06d}",
            "employee_id": broken_fk(employee_ids, "EMP", rate=0.02),
            "attendance_date": att_date.strftime("%Y-%m-%d"),
            "status": status,
            "check_in": f"{random.randint(8,10):02d}:{random.randint(0,59):02d}" if status in ("Present","Half Day","Work From Home") else "",
            "check_out": f"{random.randint(17,20):02d}:{random.randint(0,59):02d}" if status in ("Present","Half Day","Work From Home") else "",
            "overtime_hours": overtime
        }
        if random.random() < 0.01:
            row["overtime_hours"] = round(random.uniform(8, 15), 1)
        rows.append(row)
    rows = inject_duplicates(rows, rate=0.015)
    return rows

def generate_leaves(employee_ids, n=5200):
    rows = []
    for i in range(1, n + 1):
        start = rand_date(datetime(2025, 1, 1), datetime(2026, 7, 15))
        duration = random.randint(1, 10)
        row = {
            "leave_id": f"LV{i:05d}",
            "employee_id": broken_fk(employee_ids, "EMP", rate=0.02),
            "leave_type": random.choice(LEAVE_TYPES),
            "start_date": start.strftime("%Y-%m-%d"),
            "end_date": (start + timedelta(days=duration)).strftime("%Y-%m-%d"),
            "days_taken": duration,
            "status": random.choice(LEAVE_STATUS)
        }
        rows.append(row)
    rows = inject_duplicates(rows, rate=0.02)
    return rows

def generate_performance_reviews(employee_ids, n=6200):
    rows = []
    for i in range(1, n + 1):
        rating = random.choices([1,2,3,4,5], weights=[0.05,0.10,0.35,0.35,0.15])[0]
        row = {
            "review_id": f"PRF{i:05d}",
            "employee_id": broken_fk(employee_ids, "EMP", rate=0.02),
            "review_period": random.choice(PERFORMANCE_PERIODS),
            "performance_rating": rating,
            "productivity_score": round(random.uniform(40, 100), 1),
            "promotion_recommended": random.choice(PROMOTION_FLAGS),
            "manager_comments_flag": random.choice(["Yes", "No"])
        }
        if random.random() < 0.01:
            row["productivity_score"] = round(random.uniform(0, 10), 1)
        row["performance_rating"] = maybe_blank(row["performance_rating"], prob=0.03)
        rows.append(row)
    rows = inject_duplicates(rows, rate=0.015)
    return rows

def generate_payroll(employee_ids, n=32000):
    rows = []
    months = []
    d = datetime(2025, 1, 1)
    while d <= datetime(2026, 7, 1):
        months.append(d.strftime("%Y-%m"))
        d = (d.replace(day=28) + timedelta(days=4)).replace(day=1)
    for i in range(1, n + 1):
        basic = random.choice([25000, 35000, 45000, 60000, 80000, 100000, 130000,
                                 160000, 200000, 250000, 320000])
        hra = round(basic * 0.4, 2)
        bonus = random.choice([0, 0, 0, 2000, 5000, 10000, 15000, 25000])
        deductions = round(basic * random.uniform(0.05, 0.15), 2)
        net_pay = round(basic + hra + bonus - deductions, 2)
        row = {
            "payroll_id": f"PAY{i:06d}",
            "employee_id": broken_fk(employee_ids, "EMP", rate=0.02),
            "pay_month": random.choice(months),
            "basic_salary": basic,
            "hra": hra,
            "bonus": bonus,
            "deductions": deductions,
            "net_pay": net_pay,
            "payment_mode": random.choice(PAYMENT_MODE)
        }
        if random.random() < 0.01:
            row["net_pay"] = round(net_pay * random.uniform(3, 6), 2)  # outlier
        row["net_pay"] = maybe_blank(row["net_pay"], prob=0.02)
        rows.append(row)
    rows = inject_duplicates(rows, rate=0.015)
    return rows

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    departments = generate_departments()
    dept_ids = [d["department_id"] for d in departments]
    write_csv("departments.csv", list(departments[0].keys()), departments)

    employees = generate_employees(dept_ids, n=3200)
    employee_ids = [e["employee_id"] for e in employees]
    write_csv("employees.csv", list(employees[0].keys()), employees)

    job_applications = generate_job_applications(dept_ids, n=26000)
    write_csv("job_applications.csv", list(job_applications[0].keys()), job_applications)

    attendance = generate_attendance(employee_ids, n=42000)
    write_csv("attendance.csv", list(attendance[0].keys()), attendance)

    leaves = generate_leaves(employee_ids, n=5200)
    write_csv("leaves.csv", list(leaves[0].keys()), leaves)

    performance_reviews = generate_performance_reviews(employee_ids, n=6200)
    write_csv("performance_reviews.csv", list(performance_reviews[0].keys()), performance_reviews)

    payroll = generate_payroll(employee_ids, n=32000)
    write_csv("payroll.csv", list(payroll[0].keys()), payroll)

    print("\nAll datasets generated successfully in the 'output' folder.")


if __name__ == "__main__":
    main()