# mappings.py

# State to City Mapping (home/native location of employees)
state_cities = {
    "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Dharwad", "Hubli", "Belgaum"],
    "Maharashtra": ["Mumbai", "Nagpur", "Nashik", "Pune"],
    "Telangana": ["Hyderabad", "Khammam", "Nalgonda", "Warangal"],
    "Tamilnadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli"],
    "Delhi": ["New Delhi"],
    "Haryana": ["Faridabad", "Gurugram", "Panchkula", "Rohtak", "Kurukshetra"],
    "Uttar Pradesh": ["Kanpur", "Lucknow", "Noida", "Prayagraj", "Varanasi"],
    "West Bengal": ["Kolkata", "Durgapur", "Kharagpur"],
    "Gujarat": ["Ahmedabad", "Gandhinagar", "Surat", "Vadodara"],
    "Kerala": ["Kochi", "Kozhikode", "Palakkad", "Thiruvananthapuram"],
    "Rajasthan": ["Jaipur", "Bharatpur", "Bikaner", "Udaipur", "Jodhpur"],
    "Madhya Pradesh": ["Bhopal", "Gwalior", "Indore", "Jabalpur", "Ujjain"],
    "Punjab": ["Amritsar", "Chandigarh", "Jalandhar", "Ludhiana", "Mohali"],
    "Andhra Pradesh": ["Amaravati", "Kakinada", "Tirupati", "Vijayawada", "Visakhapatnam"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur"],
    "Bihar": ["Patna"],
    "Chhattisgarh": ["Bhilai", "Raipur"],
    "Assam": ["Guwahati", "Silchar"],
    "Jharkhand": ["Dhanbad", "Jamshedpur", "Ranchi"],
    "Chandigarh": ["Chandigarh"],
    "Puducherry": ["Puducherry", "Karaikal"],
    "Goa": ["Panaji", "Margao"],
    "Sikkim": ["Gangtok", "Namchi", "Geyzing", "Mangan"],
    "Arunachal Pradesh": ["Itanagar", "Tawang", "Ziro", "Pasighat"],
    "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Mandi"],
    "Jammu & Kashmir": ["Srinagar", "Jammu", "Anantnag", "Baramulla"],
    "Manipur": ["Imphal", "Thoubal", "Churachandpur"],
    "Meghalaya": ["Shillong", "Tura", "Jowai"],
    "Mizoram": ["Aizawl", "Lunglei", "Saiha"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Rishikesh"]
}

# Reverse lookup: city to state
city_state_map = {city : state for state, cities in state_cities.items() for city in cities}

# Dept to Job mapping
job_titles = {
    'Software Development': [
        'Software Engineer', 'Full-Stack Developer', 'Backend Developer',
        'Frontend Developer', 'React.js Developer', 'Angular Developer',
        'Mobile App Developer', 'Embedded Systems Engineer', 'Software Programmer',
        'Tech Lead', 'Software Architect', 'Principal Engineer'
    ],
    'AI & Machine Learning': [
        'AI Engineer', 'ML Engineer', 'GenAI Engineer', 'NLP Scientist',
        'Prompt Engineer', 'MLOps Engineer', 'Deep Learning Engineer',
        'Computer Vision Engineer', 'AI Product Manager'
    ],
    'Cybersecurity': [
        'Cybersecurity Analyst', 'Security Engineer', 'Penetration Tester',
        'SOC Analyst', 'Threat Intelligence Analyst',
        'Application Security Engineer', 'Security Architect',
        'Cloud Security Engineer', 'Compliance Security Specialist',
        'Chief Information Security Officer (CISO)'
    ],
    'Cloud & DevOps': [
        'Cloud Engineer', 'Cloud Architect', 'Site Reliability Engineer (SRE)',
        'Cloud Administrator', 'Kubernetes Administrator', 'Platform Engineer',
        'DevOps Engineer', 'Infrastructure as Code (IaC) Engineer',
        'Cloud Security Architect'
    ],
    'Data & Analytics': [
        'Data Analyst', 'Business Intelligence Analyst', 'Data Engineer',
        'Data Scientist', 'ETL Developer', 'BI Engineer',
        'Analytics Consultant', 'Statistician', 'Data Product Manager'
    ],
    'Databases': [
        'Database Administrator (DBA)', 'Database Engineer',
        'Data Warehouse Developer', 'SQL Developer',
        'Database Reliability Engineer', 'Data Governance Specialist'
    ],
    'UI/UX & Design': [
        'UX Designer', 'UI Designer', 'Product Designer', 'Visual Designer',
        'User Researcher', 'Interaction Designer', 'Design Systems Specialist'
    ],
    'Quality Assurance & Testing': [
        'QA Engineer', 'Manual Tester', 'Automation Tester',
        'SDET (Software Development Engineer in Test)', 'Test Lead',
        'Performance Tester', 'Security Tester', 'QA Lead', 'Test Architect'
    ],
    'IT Support': [
        'IT Support Specialist', 'System Administrator', 'Network Engineer',
        'IT Asset Manager', 'IT Helpdesk Specialist'
    ],
    'Sales & Marketing': [
        'Sales Executive', 'Sales Manager', 'Business Development Manager',
        'Pre-Sales Consultant', 'Account Manager', 'Content Writer',
        'Digital Marketer', 'SEO Specialist', 'Performance Marketer',
        'Growth Hacker', 'Brand Strategist', 'Technical Account Manager'
    ],
    'Finance': [
        'Accountant', 'Financial Analyst', 'Internal Auditor',
        'FinOps Specialist', 'Investment Analyst', 'Finance Manager'
    ],
    'HR & People Ops': [
        'HR Manager', 'Recruiter', 'HRBP (Business Partner)',
        'L&D Specialist', 'Talent Acquisition Specialist', 'Payroll Manager'
    ],
    'Operations': [
        'Operations Analyst', 'Logistics Coordinator', 'Process Improvement Analyst',
        'Supply Chain Analyst', 'Vendor Manager', 'Operations Manager'
    ],
    'Administration': [
        'Admin Executive', 'Front Desk Officer', 'Facility Coordinator',
        'Executive Assistant', 'Office Manager'
    ],
    'Customer Service': [
        'Support Agent', 'Customer Success Manager', 'Technical Support Engineer',
        'CRM Specialist', 'Customer Success Engineer', 'Customer Support Engineer'
    ],
    'Product & Strategy': [
        'Product Manager', 'Product Owner', 'Program Manager',
        'Business Analyst', 'Strategy Consultant', 'Associate Product Manager',
        'Product Director', 'Portfolio Manager', 'Innovation Strategist'
    ],
    # Newly added relevant departments
    'Research & Development (R&D)': [
        'R&D Engineer', 'Innovation Engineer', 'Research Scientist',
        'Prototype Developer', 'Solutions Researcher'
    ],
    'Legal & Compliance': [
        'Legal Counsel', 'Compliance Manager', 'IT Compliance Specialist',
        'Contract Manager', 'Data Privacy Officer'
    ],
    'Delivery & Client Services': [
        'Delivery Manager', 'Service Delivery Lead', 'Client Services Manager',
        'Engagement Manager', 'Account Delivery Lead'
    ]
}

# Reverse Mapping from Job to Dept
job_dept_map = {job: dept for dept, jobs in job_titles.items() for job in jobs}

# Educational qualifications per job titles
job_qualifications = {
    # --- Software Development ---
    'Software Engineer': ['Bachelor', 'Master'],
    'Full-Stack Developer': ['Bachelor', 'Master'],
    'Backend Developer': ['Bachelor', 'Master'],
    'Frontend Developer': ['Bachelor', 'Master'],
    'React.js Developer': ['Bachelor', 'Master'],
    'Angular Developer': ['Bachelor', 'Master'],
    'Mobile App Developer': ['Bachelor', 'Master'],
    'Embedded Systems Engineer': ['Bachelor', 'Master'],
    'Software Programmer': ['Bachelor'],
    'Tech Lead': ['Bachelor', 'Master'],
    'Software Architect': ['Master', 'PhD'],
    'Principal Engineer': ['Master', 'PhD'],

    # --- AI & Machine Learning ---
    'AI Engineer': ['Bachelor', 'Master', 'PhD'],
    'ML Engineer': ['Bachelor', 'Master', 'PhD'],
    'GenAI Engineer': ['Bachelor', 'Master', 'PhD'],
    'NLP Scientist': ['Bachelor', 'Master', 'PhD'],
    'Prompt Engineer': ['Bachelor', 'Master'],
    'MLOps Engineer': ['Bachelor', 'Master'],
    'Deep Learning Engineer': ['Bachelor', 'Master', 'PhD'],
    'Computer Vision Engineer': ['Bachelor', 'Master', 'PhD'],
    'AI Product Manager': ['Master', 'PhD'],

    # --- Cybersecurity ---
    'Cybersecurity Analyst': ['Bachelor', 'Master'],
    'Security Engineer': ['Bachelor', 'Master'],
    'Penetration Tester': ['Bachelor'],
    'SOC Analyst': ['Bachelor'],
    'Threat Intelligence Analyst': ['Bachelor', 'Master'],
    'Application Security Engineer': ['Bachelor', 'Master'],
    'Security Architect': ['Master', 'PhD'],
    'Cloud Security Engineer': ['Bachelor', 'Master'],
    'Compliance Security Specialist': ['Bachelor', 'Master'],
    'Chief Information Security Officer (CISO)': ['Master', 'PhD'],

    # --- Cloud & DevOps ---
    'Cloud Engineer': ['Bachelor', 'Master'],
    'Cloud Architect': ['Master', 'PhD'],
    'Site Reliability Engineer (SRE)': ['Bachelor', 'Master'],
    'Cloud Administrator': ['Diploma', 'Bachelor'],
    'Kubernetes Administrator': ['Bachelor', 'Master'],
    'Platform Engineer': ['Bachelor', 'Master'],
    'DevOps Engineer': ['Bachelor', 'Master'],
    'Infrastructure as Code (IaC) Engineer': ['Bachelor', 'Master'],
    'Cloud Security Architect': ['Master', 'PhD'],

    # --- Data & Analytics ---
    'Data Analyst': ['Bachelor', 'Master'],
    'Business Intelligence Analyst': ['Bachelor', 'Master'],
    'Data Engineer': ['Bachelor', 'Master'],
    'Data Scientist': ['Bachelor', 'Master', 'PhD'],
    'ETL Developer': ['Bachelor', 'Master'],
    'BI Engineer': ['Bachelor', 'Master'],
    'Analytics Consultant': ['Bachelor', 'Master', 'PhD'],
    'Statistician': ['Bachelor', 'Master', 'PhD'],
    'Data Product Manager': ['Bachelor', 'Master', 'PhD'],

    # --- Databases ---
    'Database Administrator (DBA)': ['Bachelor', 'Master'],
    'Database Engineer': ['Bachelor', 'Master'],
    'Data Warehouse Developer': ['Bachelor', 'Master'],
    'SQL Developer': ['Bachelor', 'Master'],
    'Database Reliability Engineer': ['Bachelor', 'Master'],
    'Data Governance Specialist': ['Bachelor', 'Master'],

    # --- UI/UX & Design ---
    'UX Designer': ['Bachelor', 'Master'],
    'UI Designer': ['Bachelor', 'Master'],
    'Product Designer': ['Bachelor', 'Master'],
    'Visual Designer': ['Bachelor', 'Master'],
    'User Researcher': ['Bachelor', 'Master'],
    'Interaction Designer': ['Bachelor', 'Master'],
    'Design Systems Specialist': ['Bachelor', 'Master'],

    # --- Quality Assurance & Testing ---
    'QA Engineer': ['Bachelor', 'Master'],
    'Manual Tester': ['Diploma', 'Bachelor'],
    'Automation Tester': ['Bachelor', 'Master'],
    'SDET (Software Development Engineer in Test)': ['Bachelor', 'Master'],
    'Test Lead': ['Bachelor', 'Master'],
    'Performance Tester': ['Bachelor', 'Master'],
    'Security Tester': ['Bachelor', 'Master'],
    'QA Lead': ['Bachelor', 'Master'],
    'Test Architect': ['Master', 'PhD'],

    # --- IT Support ---
    'IT Support Specialist': ['Diploma', 'Bachelor'],
    'System Administrator': ['Bachelor', 'Master'],
    'Network Engineer': ['Bachelor', 'Master'],
    'IT Asset Manager': ['Bachelor', 'Master'],
    'IT Helpdesk Specialist': ['Diploma', 'Bachelor'],

    # --- Sales & Marketing ---
    'Sales Executive': ['Bachelor', 'Master'],
    'Sales Manager': ['Master', 'PhD'],
    'Business Development Manager': ['Master', 'PhD'],
    'Pre-Sales Consultant': ['Bachelor', 'Master'],
    'Account Manager': ['Bachelor', 'Master'],
    'Content Writer': ['Bachelor', 'Master'],
    'Digital Marketer': ['Bachelor', 'Master'],
    'SEO Specialist': ['Diploma', 'Bachelor'],
    'Performance Marketer': ['Bachelor', 'Master'],
    'Growth Hacker': ['Bachelor', 'Master'],
    'Brand Strategist': ['Master', 'PhD'],
    'Technical Account Manager': ['Bachelor', 'Master'],

    # --- Finance ---
    'Accountant': ['Bachelor', 'Master'],
    'Financial Analyst': ['Bachelor', 'Master'],
    'Internal Auditor': ['Bachelor', 'Master'],
    'FinOps Specialist': ['Bachelor', 'Master'],
    'Investment Analyst': ['Master', 'PhD'],
    'Finance Manager': ['Master', 'PhD'],

    # --- HR & People Ops ---
    'HR Manager': ['Master', 'PhD'],
    'Recruiter': ['Bachelor', 'Master'],
    'HRBP (Business Partner)': ['Master', 'PhD'],
    'L&D Specialist': ['Bachelor', 'Master'],
    'Talent Acquisition Specialist': ['Bachelor', 'Master'],
    'Payroll Manager': ['Bachelor', 'Master'],

    # --- Operations ---
    'Operations Analyst': ['Bachelor', 'Master'],
    'Logistics Coordinator': ['Diploma', 'Bachelor'],
    'Process Improvement Analyst': ['Bachelor', 'Master'],
    'Supply Chain Analyst': ['Bachelor', 'Master'],
    'Vendor Manager': ['Bachelor', 'Master'],
    'Operations Manager': ['Master', 'PhD'],

    # --- Administration ---
    'Admin Executive': ['Diploma', 'Bachelor'],
    'Front Desk Officer': ['High School', 'Diploma'],
    'Facility Coordinator': ['Diploma', 'Bachelor'],
    'Executive Assistant': ['Bachelor', 'Master'],
    'Office Manager': ['Bachelor', 'Master'],

    # --- Customer Service ---
    'Support Agent': ['Diploma', 'Bachelor'],
    'Customer Success Manager': ['Bachelor', 'Master'],
    'Technical Support Engineer': ['Bachelor', 'Master'],
    'CRM Specialist': ['Bachelor', 'Master'],
    'Customer Success Engineer': ['Bachelor', 'Master'],
    'Customer Support Engineer': ['Bachelor', 'Master'],

    # --- Product & Strategy ---
    'Product Manager': ['Bachelor', 'Master', 'PhD'],
    'Product Owner': ['Bachelor', 'Master', 'PhD'],
    'Program Manager': ['Bachelor', 'Master', 'PhD'],
    'Business Analyst': ['Bachelor', 'Master'],
    'Strategy Consultant': ['Master', 'PhD'],
    'Associate Product Manager': ['Bachelor', 'Master'],
    'Product Director': ['Master', 'PhD'],
    'Portfolio Manager': ['Master', 'PhD'],
    'Innovation Strategist': ['Master', 'PhD'],

    # --- Research & Development (R&D) ---
    'R&D Engineer': ['Bachelor', 'Master', 'PhD'],
    'Innovation Engineer': ['Bachelor', 'Master', 'PhD'],
    'Research Scientist': ['Bachelor', 'Master', 'PhD'],
    'Prototype Developer': ['Bachelor', 'Master'],
    'Solutions Researcher': ['Bachelor', 'Master', 'PhD'],

    # --- Legal & Compliance ---
    'Legal Counsel': ['Bachelor', 'Master'],
    'Compliance Manager': ['Bachelor', 'Master'],
    'IT Compliance Specialist': ['Bachelor', 'Master'],
    'Contract Manager': ['Bachelor', 'Master'],
    'Data Privacy Officer': ['Bachelor', 'Master', 'PhD'],

    # --- Delivery & Client Services ---
    'Delivery Manager': ['Bachelor', 'Master', 'PhD'],
    'Service Delivery Lead': ['Bachelor', 'Master', 'PhD'],
    'Client Services Manager': ['Bachelor', 'Master', 'PhD'],
    'Engagement Manager': ['Bachelor', 'Master', 'PhD'],
    'Account Delivery Lead': ['Bachelor', 'Master', 'PhD']
}

# Salary ranges as per dept
salary_ranges = {
    'Software Development': (400000, 3000000),
    'AI & Machine Learning': (600000, 4000000),
    'Cybersecurity': (500000, 3500000),
    'Cloud & DevOps': (500000, 3500000),
    'Data & Analytics': (400000, 3000000),
    'Databases': (400000, 2800000),
    'UI/UX & Design': (350000, 2000000),
    'Quality Assurance & Testing': (350000, 1800000),
    'IT Support': (250000, 1200000),
    'Sales & Marketing': (300000, 2500000),
    'Finance': (350000, 2500000),
    'HR & People Ops': (300000, 1500000),
    'Operations': (300000, 1500000),
    'Administration': (250000, 1000000),
    'Customer Service': (200000, 800000),
    'Product & Strategy': (500000, 3500000),
    'Research & Development (R&D)': (500000, 4000000),
    'Legal & Compliance': (400000, 3000000),
    'Delivery & Client Services': (400000, 2500000)
}

# Department → Employee ID Prefix mapping
empId_prefixes = {
    'Software Development': 'SD',
    'AI & Machine Learning': 'AI',
    'Cybersecurity': 'CS',
    'Cloud & DevOps': 'CD',
    'Data & Analytics': 'DA',
    'Databases': 'DB',
    'UI/UX & Design': 'UX',
    'Quality Assurance & Testing': 'QA',
    'IT Support': 'IT',
    'Sales & Marketing': 'SM',
    'Finance': 'FN',
    'HR & People Ops': 'HR',
    'Operations': 'OP',
    'Administration': 'AD',
    'Customer Service': 'CSRV',
    'Product & Strategy': 'PS',
    'Research & Development (R&D)': 'RD',
    'Legal & Compliance': 'LC',
    'Delivery & Client Services': 'DC'
}
