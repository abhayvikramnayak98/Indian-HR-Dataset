import random
import datetime
import numpy as np
from config import *

def init_random():
    random.seed(seed)
    np.random.seed(seed)

init_random()

def weighted_choice(options, weights):
    """Pick a random option based on weighted probabilities."""
    return random.choices(options, weights=weights, k=1)[0]

def pick_weighted(prob_dict):
    """Pick a key from a probability dictionary."""
    return weighted_choice(list(prob_dict.keys()), list(prob_dict.values()))

def pick_gender():
    return pick_weighted(gender_prob).strip().lower()

def pick_overtime():
    return pick_weighted(overtime_dist)

def days_in_month(year, month):
    if month == 2:
        is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        return 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    
def random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + datetime.timedelta(days = random.randint(0, delta.days))

def generate_date_from_year(year):
    month = random.randint(1, 12)
    day = random.randint(1, days_in_month(year, month))
    return datetime.date(year, month, day)

def generate_custom_date(year_weights):
    year = pick_weighted(year_weights)
    return generate_date_from_year(year).strftime(date_format)

def pick_age_from_dist(age_dist, age_group):
    group = pick_weighted(age_dist)
    min_age, max_age = age_group[group]
    return random.randint(min_age, max_age)

def sample_terminate_year(hire_year, terminate_probs):
    valid_years = list(terminate_probs.keys())
    # Filter only years >= hire year
    valid_years = [int(y) for y in valid_years if y >= hire_year]

    if not valid_years:
        return None  # No termination year possible

    probs = [terminate_probs[y] for y in valid_years]
    total = sum(probs)
    if total == 0:
        return None

    # Normalize probabilities
    probs = [p/total for p in probs]

    # Choose a year
    valid_years = np.array(valid_years, dtype=int)
    return int(np.random.choice(valid_years, p=probs))

def validate_min_gap(start_date, end_date, months = termination_minGap):
    if isinstance(start_date, str):
        start_date = datetime.datetime.strptime(start_date, date_format).date()
    if isinstance(end_date, str):
        end_date = datetime.datetime.strptime(end_date, date_format).date()
    delta_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return delta_months >= months

def generate_termination_date(hire_date_obj, terminate_probs):
    today = datetime.date.today()
    if not validate_min_gap(hire_date_obj, today):
        return None
    if random.random() < termination_rate:
        hire_year = hire_date_obj.year
        term_year = sample_terminate_year(hire_year, terminate_probs)
        if term_year:
            term_date = generate_date_from_year(term_year)
            if validate_min_gap(hire_date_obj, term_date):
                return term_date.strftime(date_format)
    return None

def generate_jobtitle_probabilities(job_titles_dict):
    senior_keywords = ["Manager", "Lead", "Principal", "Chief", "Architect", "Director", "Head"]
    mid_keywords = ["Senior", "Consultant", "Specialist", "Analyst", "Scientist", "Owner"]
    junior_keywords = ["Engineer", "Developer", "Programmer", "Designer", "Tester", "Executive", "Coordinator", "Writer"]

    job_probabilities = {}

    for dept, titles in job_titles_dict.items():
        weights = []
        for title in titles:
            if any(k.lower() in title.lower() for k in senior_keywords):
                weights.append(1)   # Rare senior role
            elif any(k.lower() in title.lower() for k in mid_keywords):
                weights.append(3)   # Mid-level role
            elif any(k.lower() in title.lower() for k in junior_keywords):
                weights.append(5)   # Common role
            else:
                weights.append(3)   # Default
        total = sum(weights)
        probs = [round(w / total, 4) for w in weights]
        job_probabilities[dept] = probs

    return job_probabilities

def pick_base_location():
    return np.random.choice(base_locations, p = base_location_prob)