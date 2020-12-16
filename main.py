
import configs as conf
from sheet import Sheet

import pandas as pd
from pathlib import Path

cwd = Path.cwd()
file_path = cwd / Path("data/DriversWithImpacts.xlsx")



def main(file_path, X, Y, V, saveAs, convertor):
    file_path = Path(file_path)
    sheets = pd.read_excel(file_path, sheet_name=None)

    sheet_names = []
    for sheet in sheets.keys():
        sheet_names.append(sheet)

    sheet_name = sheet_names[conf.__SHEET_NO__]

    df = sheets[sheet_name]
    sheet = Sheet(sheet_name=sheet_name, df=df)
    sheet.save_cols(X=X, Y=Y, V=V)

    if convertor == "convertor_1":
        sheet1 = sheet.convertor1()
        sheet.save_csv(sheet1, f"{saveAs}.csv")
    if convertor == "convertor_2":
        sheet2 = sheet.convertor2()
        sheet.save_csv(sheet2, f"{saveAs}.csv")

main(
    file_path=file_path,
    X=conf.__X__,
    Y=conf.__Y__,
    V=conf.__VALUE__,
    convertor="convertor_2",
    saveAs="sheet_demo"
)
