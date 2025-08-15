import random
import datetime
import pandas as pd
from tqdm import tqdm
from logic import *
from config import *
from mappings import *

names_df = pd.read_csv('data/names_dataset.csv')

# -----------------------------
# NAME & LOCATION
# -----------------------------
names_df['gender'] = names_df['gender'].str.strip().str.lower()

def generate_name_state_by_gender(gender):
    gender_lower = gender.strip().lower()
    filtered_df = names_df[names_df['gender'] == gender_lower]
    if filtered_df.empty:
        raise ValueError(f"No names found for gender '{gender_lower}'. Check CSV for mismatches.")
    row = filtered_df.sample(n=1).iloc[0]
    return row['first_name'], row['last_name'], row['state']

def generate_city_for_state(state):
    return random.choice(state_cities[state])

def generate_base_location():
    return pick_base_location()

# -----------------------------
# EMPLOYEE ID
# -----------------------------
def generate_employee_id(seq_num, dept = None):
    prefix = empId_prefixes.get(dept, "EMP")
    return f"{prefix} - {seq_num:05d}"

# -----------------------------
# DEPARTMENT & JOB TITLE
# -----------------------------
def generate_dept():
    return pick_weighted(dept_dist)

def pick_job_title(dept):
    job_title_probs = generate_jobtitle_probabilities(job_titles)[dept]
    titles = job_titles[dept]
    return random.choices(titles, weights=job_title_probs, k = 1)[0]

# -----------------------------
# DATES
# -----------------------------
def generate_hire_date():
    return generate_custom_date(hire_year_prob)

def generate_birthdate(hire_date_str, job_title, edu_level):
    hire_date = datetime.datetime.strptime(hire_date_str, date_format).date()
    age = pick_age_from_dist(age_dist, age_group)
    
    # Adjust min_age for senior/PhD roles
    if "Manager" in job_title and age < 30:
        age = random.randint(30, 65)
    elif edu_level == 'PhD' and age < 27:
        age = random.randint(27, 65)

    birth_year = hire_date.year - age
    dob = generate_date_from_year(birth_year)
    return dob.strftime(date_format)

def generate_termination_date_str(hire_date_str):
    hire_date_obj = datetime.datetime.strptime(hire_date_str, date_format).date()
    return generate_termination_date(hire_date_obj, termination_prob)

# -----------------------------
# OTHER ATTRIBUTES
# -----------------------------

def generate_education_level(job_title):
    return random.choice(job_qualifications.get(job_title, list(education_multiplier.keys())))

def generate_performance_rating():
    return pick_weighted(performance_prob)

def generate_gender():
    return pick_gender()

def generate_overtime():
    return pick_overtime()

# -----------------------------
# SALARY WITH ADJUSTED VALUE
# -----------------------------
def calculate_age(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, date_format).date()
    today = datetime.date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def generate_adjusted_salary(department, job_title, edu_level, birthdate):
    min_sal, max_sal = (
        salary_ranges.get(job_title) or salary_ranges.get(department) or (300000, 1000000)
    )
    base_salary = random.randint(min_sal, max_sal)
    multiplier = education_multiplier.get(edu_level, 1.0)
    adjusted_salary = base_salary * multiplier

    age = calculate_age(birthdate)
    min_inc, max_inc = age_increment_range
    age_increment = 1 + random.uniform(min_inc, max_inc) * age
    adjusted_salary *= age_increment

    adjusted_salary = max(adjusted_salary, base_salary)
    return base_salary, adjusted_salary

# -----------------------------
# RECORD GENERATION
# -----------------------------
def generate_record(seq_num):
    # Gender -> Name & State
    gender = generate_gender()
    fname, lname, state = generate_name_state_by_gender(gender)
    city = generate_city_for_state(state)
    base_location = generate_base_location()

    # Dept & Job
    dept = generate_dept()
    job_title = pick_job_title(dept)

    # Education & Performance
    qual = generate_education_level(job_title)
    perf = generate_performance_rating()

    # Dates
    hire_date = generate_hire_date()
    birthdate = generate_birthdate(hire_date, job_title, qual)
    term_date = generate_termination_date_str(hire_date)

    # Overtime
    overtime = generate_overtime()

    # Salary
    salary, adj_salary = generate_adjusted_salary(dept, job_title, qual, birthdate)

    # Employee ID
    emp_id = generate_employee_id(seq_num, dept)

    return {
        "employee_id": emp_id,
        "first_name": fname,
        "last_name": lname,
        "gender": gender,
        "department": dept,
        "job_title": job_title,
        "education_level": qual,
        "performance_rating": perf,
        "state": state,
        "home_city": city,
        "base_location" : base_location,
        "hiredate": hire_date,
        "birthdate": birthdate,
        "termination_date": term_date,
        "overtime": overtime,
        "salary": salary,
        "adjusted_salary": adj_salary
    }

def generate_dataset(show_progress = True):
    records = []
    iterator = range(num_records)
    if show_progress:
        iterator = tqdm(
            iterator,
            desc = '⚡ Generating Employee Records',
            unit = ' rec',
            ncols = 100,
            bar_format = "{l_bar}{bar} | {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            colour = "cyan"
        )
    for i in iterator:
        records.append(generate_record(i + 1))
    return records