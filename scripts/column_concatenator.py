import pandas as pd
from pathlib import Path


# USER INPUTS
INPUT_FILE_PATH = Path("../input/dataset.xlsx")
OUTPUT_FILE_PATH = Path("../output/data_out.xlsx")
COLUMN_KEYWORD_TO_CONCATENATE = str("utho")
NEW_COLUMN_NAME = str("NEW_COLUMN_NAME")
CONCATENATOR = str(' | ')


def save_excel(df, out_file_path):
    writer = pd.ExcelWriter(out_file_path, engine="xlsxwriter")
    df.to_excel(writer)
    writer.save()


def read_excel(in_file_path):
    return pd.read_excel(in_file_path, engine='openpyxl')


def concatenator(df):
    cols_to_concat = [col for col in df.columns if COLUMN_KEYWORD_TO_CONCATENATE in col]
    if len(cols_to_concat) == 0:
        raise Exception(f"No columns to concatenate, which has '{COLUMN_KEYWORD_TO_CONCATENATE}' in its name.")
    else:
        print(f"Following columns will be merged with '{CONCATENATOR}' and dropped : {cols_to_concat}")

    df[NEW_COLUMN_NAME] = df[cols_to_concat].apply(lambda row: CONCATENATOR.join(filter(None, row)), axis=1)
    df = df.drop(columns=cols_to_concat)
    return df


if __name__ == '__main__':

    df = read_excel(in_file_path=INPUT_FILE_PATH).fillna('')
    df = concatenator(df=df)
    save_excel(df=df, out_file_path=OUTPUT_FILE_PATH)
