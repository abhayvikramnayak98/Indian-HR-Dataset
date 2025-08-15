num_records = 20000
seed = 42
date_format = "%d-%m-%Y"

# Age increment factor per year of age (industry norms for Indian IT)
# Values are in decimal (0.002 = 0.2%)
age_increment_range = (0.002, 0.004)  # 0.2% to 0.4% per year of age

# Age distribution by group (probabilities must sum to 1.0)
age_dist = {
    'under_25': 0.11,
    '25_34': 0.25,
    '35_44': 0.31,
    '45_54': 0.24,
    'over_55': 0.09
}

# Map each group to actual min/max age range
age_group = {
    'under_25': (20, 25),
    '25_34': (25, 35),
    '35_44': (35, 45),
    '45_54': (45, 55),
    'over_55': (56, 65)
}

dept_dist = {
    'Software Development': 0.25,         # Largest workforce
    'AI & Machine Learning': 0.10,        # High-growth area
    'Data & Analytics': 0.08,             # Big demand in data-driven roles
    'Cloud & DevOps': 0.07,               # Strong cloud adoption
    'Cybersecurity': 0.06,                 # Critical, but lean team
    'Quality Assurance & Testing': 0.07,  # Essential for delivery
    'UI/UX & Design': 0.04,               # Important for product-facing roles
    'Databases': 0.03,                    # Specialized skill sets
    'IT Support': 0.04,                   # Necessary infrastructure support
    'Sales & Marketing': 0.06,            # Business growth team
    'Product & Strategy': 0.05,           # Strategic leadership
    'Research & Development (R&D)': 0.03, # Innovation focus
    'Delivery & Client Services': 0.04,   # Customer delivery ensuring SLAs
    'Finance': 0.02,                      # Business enabler
    'HR & People Ops': 0.02,              # People management
    'Operations': 0.02,                   # Process and logistics
    'Administration': 0.01,               # Basic operations
    'Customer Service': 0.02,              # Customer-facing support
    'Legal & Compliance': 0.01            # Niche but crucial compliance
}

gender_prob = {'female' : 0.49, 'male' : 0.51}
overtime_dist = {'Yes' : 0.25, 'No' : 0.75}

termination_minGap = 6
termination_rate = 0.12
termination_prob = {
    2015: 0.03,
    2016: 0.05,
    2017: 0.07,
    2018: 0.10,
    2019: 0.13,
    2020: 0.12,
    2021: 0.17,
    2022: 0.15,
    2023: 0.10,
    2024: 0.05,
    2025: 0.03   # Only up to current date
}

hire_year_prob = {
    2015: 0.04,  # Old hires, small proportion
    2016: 0.05,
    2017: 0.06,
    2018: 0.08,  # Steady growth
    2019: 0.10,  # Pre-pandemic peak
    2020: 0.05,  # COVID slowdown
    2021: 0.12,  # Recovery & growth
    2022: 0.18,  # Hiring boom
    2023: 0.20,  # Strong hiring
    2024: 0.12   # Ongoing hiring but partial year
}

performance_prob = {
    'Star' : 0.08,
    'Exceeds' : 0.17,
    'Meets' : 0.55,
    'Partial' : 0.15,
    'Below' : 0.05
}

state_dist = {
    'Karnataka': 0.25,           # HQ state (Bengaluru)
    'Telangana': 0.10,           # Hyderabad (core branch)
    'Maharashtra': 0.10,         # Pune (core branch)
    'Odisha': 0.05,              # Bhubaneswar (core branch)
    'West Bengal': 0.05,         # Kolkata (core branch)
    'Delhi': 0.08,               # New Delhi (core branch)
    'Tamil Nadu': 0.07,          # Chennai (core branch)
    'Uttar Pradesh': 0.03,
    'Haryana': 0.02,
    'Gujarat': 0.02,
    'Kerala': 0.02,
    'Rajasthan': 0.02,
    'Madhya Pradesh': 0.02,
    'Punjab': 0.01,
    'Andhra Pradesh': 0.01,
    'Bihar': 0.01,
    'Chhattisgarh': 0.01,
    'Assam': 0.01,
    'Jharkhand': 0.01,
    'Chandigarh': 0.005,
    'Puducherry': 0.005,
    'Goa': 0.005
}

education_multiplier = {
    'High School': 1.00,
    'Diploma': 1.05,
    'Bachelor': 1.20,
    'Master': 1.40,
    'PhD': 1.60
}

# Base (working) locations reflecting HQ + core locations
base_locations = [
    "Bengaluru",   # HQ
    "Hyderabad",
    "Pune",
    "Bhubaneswar",
    "Kolkata",
    "New Delhi",
    "Chennai"
]

# Corresponding probabilities (must sum to 1.0)
base_location_prob = [
    0.35,  # Bengaluru (HQ)
    0.20,  # Hyderabad
    0.15,  # Pune
    0.10,  # Bhubaneswar
    0.08,  # Kolkata
    0.07,  # New Delhi
    0.05   # Chennai
]