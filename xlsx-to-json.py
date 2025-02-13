import json
import os
from datetime import datetime

import pandas as pd


def load_existing_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def write_data_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def process_sheet(sheet_name, dataframe, output_dir):
    """
    Process the given sheet and save the data to JSON files.

    Args:
      sheet_name (str): The name of the sheet to process.
      dataframe (pandas.DataFrame): The DataFrame containing the sheet data.
      output_dir (str): The directory where the JSON files will be saved.

    Returns:
      None
    """
    if sheet_name == "template":
        return

    dataframe.set_index(dataframe.columns[0], inplace=True)

    for lang in dataframe.columns:
        lang_dict = {sheet_name: {}}
        for key, value in dataframe[lang].dropna().items():
            # Check if the key is a non-empty string
            if not isinstance(key, str) or not key:
                continue
            keys = key.split('.')
            d = lang_dict[sheet_name]
            for k in keys[:-1]:
                if k not in d:
                    d[k] = {}
                d = d[k]
            d[keys[-1]] = value

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.join(output_dir, f'{lang}.json')
        existing_data = load_existing_data(filename)
        existing_data.update(lang_dict)
        write_data_to_file(filename, existing_data)


def process_xlsx(xlsx, current_date):
    """
    Process the given Excel file and its sheets.

    Args:
      xlsx (pandas.ExcelFile): The Excel file to process.
      current_date (datetime.datetime): The current date.

    Returns:
      None
    """
    for sheet_name, dataframe in xlsx.items():
        process_sheet(sheet_name, dataframe, current_date)


# Get the current date
current_date = datetime.now().strftime('%Y%m%d-%H%M')

# Define the output directory
output_dir = os.path.join('i18n-output', current_date)

# Load the Excel file
xlsx = pd.read_excel('i18n.xlsx', sheet_name=None)

# Call the function to start the process
process_xlsx(xlsx, output_dir)
