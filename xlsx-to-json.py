import pandas as pd
import json
import os
from datetime import datetime


def load_existing_data(filename):
    """
    Load existing data from a JSON file.

    Args:
      filename (str): The path to the JSON file.

    Returns:
      dict: The loaded data as a dictionary. If the file doesn't exist, an empty dictionary is returned.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return {}


def write_data_to_file(filename, data):
    """
    Write data to a file in JSON format.

    Args:
      filename (str): The name of the file to write the data to.
      data (dict): The data to be written to the file.

    Returns:
      None
    """
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def process_sheet(sheet_name, dataframe, current_date):
    """
    Process a sheet in an Excel file and convert it to a JSON file.

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
        lang_dict = {sheet_name: dataframe[lang].dropna().to_dict()}
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
current_date = datetime.now().strftime('%Y-%m-%d-%H-%M')

# Load the Excel file
xlsx = pd.read_excel('i18n.xlsx', sheet_name=None)

# Call the function to start the process
process_xlsx(xlsx, current_date)
