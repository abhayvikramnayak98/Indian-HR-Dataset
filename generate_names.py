import csv
import importlib.util
import os

# Folder where your region dictionary Python files are stored
REGION_FOLDER = "./regions"  # adjust this path
OUTPUT_CSV = "data/names_dataset.csv"

def load_region_dicts(folder_path):
    """Dynamically load all *_dict dictionaries from Python files in a folder."""
    all_dicts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            file_path = os.path.join(folder_path, filename)
            module_name = filename[:-3]

            # Dynamically import the module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Collect all dict variables ending with "_dict"
            for attr_name in dir(module):
                if attr_name.endswith("_dict"):
                    d = getattr(module, attr_name)
                    if isinstance(d, dict):
                        all_dicts.update(d)
    return all_dicts

# Step 1: Load all regional name dictionaries
all_regions = load_region_dicts(REGION_FOLDER)

# Step 2: Build the rows with gender info
rows = []
for state, data in all_regions.items():
    male_first_names = data.get('male_first_names', [])
    female_first_names = data.get('female_first_names', [])
    last_names = data.get('last_names', [])

    # Male names
    for fname in male_first_names:
        for lname in last_names:
            rows.append([state, fname, lname, "male"])

    # Female names
    for fname in female_first_names:
        for lname in last_names:
            rows.append([state, fname, lname, "female"])

# Step 3: Sort results by state, then first and last name
rows.sort(key=lambda x: (x[0], x[1], x[2]))

# Step 4: Save to CSV with **lowercase** column headers
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["state", "first_name", "last_name", "gender"])  # lowercase headers
    writer.writerows(rows)

print(f"✅ Created CSV with {len(rows)} names (with gender) from {len(all_regions)} states.")
