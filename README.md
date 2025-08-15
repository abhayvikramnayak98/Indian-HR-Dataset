# Employee Dataset Generator

## Project Overview
This project is a **modular Python-based system** designed to generate a large, realistic HR dataset reflecting the Indian IT industry workforce. The dataset includes detailed employee information such as demographics, job roles, salary modeling, and multiple location fields.

This dataset generator is the largest I have created, built over 3-4 days, emphasizing depth, accuracy, and configurability.

## Key Features
- Generates **20,000+ employee records** with realistic distributions  
- Gender-aware name and state generation linked to Indian demographic data  
- Weighted selection of departments and job titles mimicking industry trends  
- Birthdates, hire dates, and termination dates modeled realistically  
- Salary calculations include education multipliers and age-related increments  
- Dual location fields: *home city* and *base location* (work location) with configurable probabilities reflecting company HQ and core offices  
- Stylish and informative **progress bar** showing generation status  
- Fully modular design separating config, data mapping, logic, and generation  

## Project Structure
project_root/
├── config.py # Configurations: probabilities, constants, base location probabilities
├── mappings.py # Static mappings: employee ID prefixes, job titles, salaries, state/city dictionaries
├── logic.py # Helper functions: weighted picks, date generation, age calculations, base location picker
├── generator.py # Core record generation with built-in stylish progress bar
├── main.py # Minimal entry point for dataset generation and CSV output
│
├── names_dataset.csv # Gender-aware name and state dataset (input)
│
└── data/
└── HumanResources.csv # Final generated dataset output


## Workflow

            ┌───────────────────┐
            │  names_dataset.csv │
            │  (gendered names & │
            │   states data)     │
            └────────┬───────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │       generator.py               │
    │ Loads: config.py, mappings.py,  │
    │ logic.py + names_dataset.csv    │
    │ Generates employee records with:│
    │  -  Gender-aware name/state/city │
    │  -  Weighted department/job titles│
    │  -  Hire date, birthdate, termination date│
    │  -  Salary with adjustments       │
    │  -  Home city + base work location│
    └────────┬─────────────────────────┘
             │
             ▼
      ┌─────────────────┐
      │     main.py      │
      │ Calls generate   │
      │ dataset()        │
      │ Saves CSV       │
      └────────┬────────┘
               │
               ▼
   ┌─────────────────────────────┐
   │  Generated HumanResources.csv│
   └─────────────────────────────┘


## Configurability
All probabilities, distributions, and mappings are driven by `config.py`, making it easy to tweak:
- Gender and state probabilities  
- Department and job title distributions  
- Hiring year and age group weights  
- Salary ranges and increments  
- Base work locations and their probabilities  

## Acknowledgments
This dataset generation project reflects a substantial effort across multiple days, focusing on creating a realistic and rich HR dataset for analytics, testing, and learning purposes.

---

*Feel free to customize this README further by adding sections such as:*

- **Installation Instructions**  
- **Examples of Dataset Usage**  
- **Future Improvements**  
- **Contributing Guidelines**  
- **License**  
- **Contact / Author Information**

---

