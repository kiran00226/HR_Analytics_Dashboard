create database hr_analysis;
show tables;
USE hr_analysis;

CREATE TABLE departments (
    department_id VARCHAR(10) PRIMARY KEY,
    department_name VARCHAR(100),
    description VARCHAR(255),
    budget_inr DECIMAL(15,2)
);

CREATE TABLE employees (
    employee_id VARCHAR(10) PRIMARY KEY,
    employee_name VARCHAR(100),
    gender VARCHAR(20),
    dob DATE,
    age INT,
    marital_status VARCHAR(30),
    city VARCHAR(50),
    state VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100),
    department_id VARCHAR(10),
    designation VARCHAR(100),
    education VARCHAR(50),
    experience_years DECIMAL(4,1),
    date_of_joining DATE,
    employment_status VARCHAR(30),
    exit_date DATE,
    monthly_basic_salary DECIMAL(12,2),
    satisfaction_score DECIMAL(3,1),

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE attendance (
    attendance_id VARCHAR(10) PRIMARY KEY,
    employee_id VARCHAR(10) NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(30),
    check_in TIME,
    check_out TIME,
    overtime_hours DECIMAL(4,1),
	FOREIGN KEY (employee_id)REFERENCES employees(employee_id)
    ON UPDATE CASCADE
	ON DELETE CASCADE
);

CREATE TABLE payroll (
    payroll_id VARCHAR(10) PRIMARY KEY,
    employee_id VARCHAR(10) NOT NULL,
    pay_month DATE NOT NULL,
    basic_salary DECIMAL(10,2) NOT NULL,
    hra DECIMAL(10,2) DEFAULT 0,
    bonus DECIMAL(10,2) DEFAULT 0,
    deductions DECIMAL(10,2) DEFAULT 0,
    net_pay DECIMAL(10,2) NOT NULL,
    payment_mode ENUM('Cash','Cheque','Bank Transfer') NOT NULL,

    CONSTRAINT fk_payroll_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE leaves (
    leave_id VARCHAR(10) PRIMARY KEY,
    employee_id VARCHAR(10) NOT NULL,
    leave_type VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    days_taken INT NOT NULL,
    status ENUM('Approved', 'Pending', 'Rejected') NOT NULL,

    CONSTRAINT fk_leaves_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE performance_reviews (
    review_id VARCHAR(10) PRIMARY KEY,
    employee_id VARCHAR(10) NOT NULL,
    review_period VARCHAR(10) NOT NULL,
    performance_rating DECIMAL(2,1) NOT NULL,
    productivity_score DECIMAL(5,2) NOT NULL,
    promotion_recommended ENUM('Yes', 'No') NOT NULL,
    manager_comments_flag ENUM('Yes', 'No') NOT NULL,

    CONSTRAINT fk_performance_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


CREATE TABLE job_applications (
    application_id VARCHAR(10) PRIMARY KEY,
    candidate_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    department_id VARCHAR(10),
    position_applied VARCHAR(100) NOT NULL,
    recruitment_source VARCHAR(50),
    application_date DATE NOT NULL,
    years_of_experience DECIMAL(4,1),
    expected_salary DECIMAL(10,2),
    status VARCHAR(30) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),

    CONSTRAINT fk_job_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

ALTER TABLE employees
ADD CONSTRAINT fk_employee_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

SELECT
    (SELECT COUNT(*) FROM departments) AS departments,
    (SELECT COUNT(*) FROM employees) AS employees,
    (SELECT COUNT(*) FROM attendance) AS attendance,
    (SELECT COUNT(*) FROM payroll) AS payroll,
    (SELECT COUNT(*) FROM leaves) AS leaves,
    (SELECT COUNT(*) FROM performance_reviews) AS performance_reviews,
    (SELECT COUNT(*) FROM job_applications) AS job_applications;

   
   
   
    