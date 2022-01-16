
from sheet import Sheet

import pandas as pd
from pathlib import Path


def main(file_path, X, Y, V, saveAs, convertor):
    file_path = Path(file_path)
    sheets = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')

    sheet_names = []
    for sheet in sheets.keys():
        sheet_names.append(sheet)

    # Using sheet 1 as the default sheet.
    sheet_name = sheet_names[0]

    df = sheets[sheet_name]
    sheet = Sheet(sheet_name=sheet_name, df=df)
    sheet.save_cols(X=X, Y=Y, V=V)

    if convertor == "convertor_1":
        new_sheet = sheet.convertor1()
        sheet.save_excel(new_sheet, f"{saveAs}")

    elif convertor == "convertor_2":
        new_sheet = sheet.convertor2()
        sheet.save_excel(new_sheet, f"{saveAs}")

    elif convertor == "convertor_3":
        new_sheet = sheet.convertor3()
        sheet.save_excel(new_sheet, f"{saveAs}")

    elif convertor == "convertor_4":
        new_sheet = sheet.convertor4()
        sheet.save_excel(new_sheet, f"{saveAs}")

    else:
        raise Exception(f"Invalid convertor name: '{convertor}'.")


