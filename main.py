import pandas as pd
from generator import *

def main():
    print(f"▶ Generating {num_records} employee records...")
    
    # Call generator.py function (progress bar handled there)
    dataset = generate_dataset(show_progress = True)

    # Column order for CSV
    columns = [
        "employee_id",
        "first_name",
        "last_name",
        "gender",
        "department",
        "job_title",
        "education_level",
        "performance_rating",
        "state",
        "home_city",
        "base_location",
        "hiredate",
        "birthdate",
        "termination_date",
        "overtime",
        "salary",
        "adjusted_salary"
    ]

    # Create Dataframe & save
    df = pd.DataFrame(dataset, columns=columns)
    output_file = 'data/HumanResources.csv'
    df.to_csv(output_file, index = False)

    print(f"✅ Dataset saved to '{output_file}' with {len(df)} records.")

if __name__ == '__main__':
    main()