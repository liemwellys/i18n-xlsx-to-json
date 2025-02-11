import json
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


def process_sheet(sheet_name, dataframe, current_date):
    """
    Process the given sheet and save the data to JSON files.

    Args:
      sheet_name (str): The name of the sheet to process.
      dataframe (pandas.DataFrame): The DataFrame containing the sheet data.
      current_date (str): The current date in the format 'YYYY-MM-DD'.

    Returns:
      None
    """
    if sheet_name == "template":
        return

    dataframe.set_index(dataframe.columns[0], inplace=True)

    for lang in dataframe.columns:
        lang_dict = {sheet_name: {}}
        for key, value in dataframe[lang].dropna().items():
            keys = key.split('.')
            d = lang_dict[sheet_name]
            for k in keys[:-1]:
                if k not in d:
                    d[k] = {}
                d = d[k]
            d[keys[-1]] = value

        filename = f'{current_date}-{lang}.json'
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

# Load the Excel file
xlsx = pd.read_excel('i18n.xlsx', sheet_name=None)

# Call the function to start the process
process_xlsx(xlsx, current_date)
