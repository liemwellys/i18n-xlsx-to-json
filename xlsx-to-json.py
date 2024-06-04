import pandas as pd
import json
import os
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d-%H-%M')

# Load the Excel file
xlsx = pd.read_excel('i18n.xlsx', sheet_name=None)

# Iterate over the sheets
for sheet_name, df in xlsx.items():
    # Skip the process if the sheet name is "template"
    if sheet_name == "template":
        continue

    # Set the first column as the index (child key)
    df.set_index(df.columns[0], inplace=True)

    # Iterate over the columns (languages)
    for lang in df.columns:
        # Create a dictionary for this language
        lang_dict = {sheet_name: df[lang].dropna().to_dict()}

        # Create the filename with the current date and language code
        filename = f'{current_date}-{lang}.json'

        # Check if the JSON file already exists
        if os.path.exists(filename):
            # If it does, load the existing data
            with open(filename, 'r') as f:
                existing_data = json.load(f)
        else:
            # If it doesn't, create an empty dictionary
            existing_data = {}

        # Update the existing data with the new data
        existing_data.update(lang_dict)

        # Write the updated data to the JSON file
        with open(filename, 'w') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
