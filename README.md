# i18n Excel File into JSON Converter

Convert Excel file (`.xlsx` format) containing internationalization (i18n) data into JSON format.

## Key highlights

**Input:** `.xlsx` file with the following format:

- Sheet names:
  - Representing main grouped component (e.g., UI component).
  - The grouped component can be written in any case, following the developer convention.
  - Example: `COMMONBUTTON`
- Content:
  - `key` columns representing unique identifier of each translation string for each supported language code and region.
  - Each `key` can be written in any case, following the developwer convention.
    - Example: `Apply`
  - If there are any keys used for managing sub group, the child key corresponding to the parent key should be separated with `.` (dot) notation.
    - Example:
      - `Confirm.Yes`
      - `Confirm.No`
- Example:

  A sheet named `COMMONBUTTON` has the following data:

  | key         | zh-TW | en-US  |
  | ----------- | ----- | ------ |
  | Apply       | 套用  | Apply  |
  | Export      | 道出  | Export |
  | Send        | 送出  | Send   |
  | Confirm.Yes | 是    | Yes    |
  | Confirm.No  | 否    | No     |

**Output:**

- Individual JSON files, named according to their language code and region (e.g., `en-US.json`, `zh-TW.json`, etc.), are stored within a directory named with the date and time of generation inside the `i18n-output` directory. The date-time format for the directory name is `YYYYMMDD-HHmm`.

  Example:

  ```bash
  i18n-xlsx-to-json/
  ├── i18n-output/
  │   └── 20250212-1500/
  │       ├── en-US.json
  │       └── zh-TW.json
  ```

- `zh-TW` JSON file sample output:

  ```json
  {
    "COMMONBUTTON": {
      "Apply": "套用",
      "Export": "道出",
      "Send": "送出",
      "Confirm": {
        "Yes": "是",
        "No": "否"
      }
    }
  }
  ```

- `en-US` JSON file sample output:

  ```json
  {
    "COMMONBUTTON": {
      "Apply": "Apply",
      "Export": "Export",
      "Send": "Send",
      "Confirm": {
        "Yes": "Yes",
        "No": "No"
      }
    }
  }
  ```

## Running The Program

Change your directory into this workspace directory, then install the requirements.

```bash
pip install -r requirements.txt
```

Place the multi-language Excel file (e.g., `i18n.xlsx`) under the workspace directory as described on the following example:

```bash
i18n-xlsx-to-json/
└── i18n.xlsx
```

Make sure the i18n Excel file name on the [`xlsx-to-json.py`](/xlsx-to-json.py#L83-L84) script is matched to the file placed under the workspace directory.

```python
# Load the Excel file
xlsx = pd.read_excel('i18n.xlsx', sheet_name=None)
```

Execute the Python script using the following command:

```bash
python xlsx-to-json.py
```

Each JSON files output, named according to their language code and region (e.g., `en-US.json`, `zh-TW.json`, etc.), are stored within a directory named with the date and time of generation inside the `i18n-output` directory. The date-time format for the directory name is `YYYYMMDD-HHmm`.

```bash
i18n-xlsx-to-json/
├── i18n-output/
│   └── 20250212-1500/
│       ├── en-US.json
│       └── zh-TW.json
```
