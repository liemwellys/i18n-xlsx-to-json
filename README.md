# i18n Excel File into JSON Converter

Convert Excel file (`.xlsx` format) containing internationalization (i18n) data into JSON format.

## Key highlights

**Input:** `.xlsx` file with the following format:

- sheet names representing parent keys in `camelCase` format (e.g., `commonButton`).
- columns containing child keys, language codes, and values. Example:

  | key    | zh-TW | en-US  |
  | ------ | ----- | ------ |
  | apply  | 套用  | Apply  |
  | export | 道出  | Export |
  | send   | 送出  | Send   |

**Output:**

- Individual JSON files named with the date time and language code (e.g., `2024-05-30-11-30-en-US.json`).

- `zh-TW` json file sample output:

  ```json
  {
    "commonButton": {
      "apply": "套用",
      "export": "道出",
      "send": "送出"
    }
  }
  ```

- `en-US` json file sample output:

  ```json
  {
    "commonButton": {
      "apply": "Apply",
      "export": "Export",
      "send": "Send"
    }
  }
  ```

**Functionality:**

- Reads each sheet of the `.xlsx` file.
- Extracts parent key (sheet name) and child keys (first column).
- Iterates through each language code column.
- Constructs a nested JSON dictionary with child keys as keys and corresponding values.

**Benefits:**

- Improved efficiency and accuracy.
- Reduced manual effort and error-proneness.
- Enhanced data management and localization.

## Required Package

- `pandas`
- `json`
- `os`
- `datetime`
