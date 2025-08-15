# Employee Dataset Generator

## Project Overview
This project is a **modular, Python-based system** designed to generate a large, realistic HR dataset that reflects the Indian IT industry workforce. The dataset includes detailed employee information such as demographics, job roles, salary modelling, and multiple location fields.

This dataset generator is the largest I have created, built over three to four days, emphasising depth, accuracy, and configurability.

## Key Features
- Generates **20,000+ employee records** with realistic distributions  
- Gender-aware name and state generation linked to Indian demographic data  
- Weighted selection of departments and job titles mimicking industry trends  
- Birthdates, hire dates, and termination dates modelled realistically  
- Salary calculations include education multipliers and age-related increments  
- Dual location fields: *home city* and *base location* (work location) with configurable probabilities reflecting company HQ and core offices  
- Stylish and informative **progress bar** showing generation status  
- Fully modular design separating config, data mapping, logic, and generation  

## Project Structure
```
project_root/
├── config.py         # Configuration: probabilities, constants, base location probabilities
├── mappings.py       # Static mappings: job titles, salary ranges, state/city lists, ID prefixes
├── logic.py          # Helper functions: weighted picks, date generation, age calculations, etc.
├── generator.py      # Core record generation (includes progress bar)
├── main.py           # Entry point: calls generator and saves dataset to CSV
└── data/
    └── names_dataset.csv # Input: gendered names & states
    └── HumanResources.csv # Output: final generated dataset
```

## Workflow
<img width="1564" height="1984" alt="image" src="https://github.com/user-attachments/assets/42db0271-c268-402b-a9f6-e5c306289125" />

## ⚙️ Configurability
All probabilities, distributions, and mappings are stored in config.py and mappings.py, making it easy to customise:
- Gender and state probabilities
- Department and job title distributions
- Hiring year and age group weights
- Salary ranges and increments
- Base work locations and their probabilities

## Potential Use Cases
- Data Analytics Practice — Build dashboards and KPIs in tools like Tableau or Power BI.
- Machine Learning — Train HR analytics models (attrition prediction, salary forecasting, etc.).
- Testing — Populate HRMS/ERP systems with realistic data.
- Education — Teach SQL, Python, or data science with hands-on datasets.

## Future Improvements
- Add international location support.
- Introduce employee promotion history.
- Implement parallel processing for faster generation on large datasets.
- Add JSON and Parquet output formats.

## Acknowledgments
This project reflects multiple days of effort, focusing on building a realistic and rich HR dataset for analytics, testing, and educational purposes.

## License
This project is licensed under the MIT License — feel free to use and modify it.

## Contact
**Author**: Abhisekh Nayak <br>
**Email**: abhinayak.gita2016@gmail.com <br>
**GitHub**: [Abhisekh Nayak's Github](https://github.com/abhayvikramnayak98)
