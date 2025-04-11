import os
import pandas as pd

def read_spreadsheet(filepath):
    ext = os.path.splitext(filepath)[-1].lower()

    if ext in ['.csv']:
        df = pd.read_csv(filepath)
    elif ext in ['.xlsx', '.xls', '.xlsm']:
        df = pd.read_excel(filepath, sheet_name=None)  # all sheets
    else:
        raise ValueError(f"Unsupported spreadsheet format: {ext}")

    text_chunks = []

    if isinstance(df, dict):  # multiple sheets
        for sheet, data in df.items():
            text = data.to_string(index=False)
            text_chunks.append((sheet, text))
    else:
        text_chunks.append(("Sheet1", df.to_string(index=False)))

    return text_chunks
