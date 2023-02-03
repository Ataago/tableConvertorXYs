import pandas as pd
from pathlib import Path
import os
import pyreadstat

# USER INPUTS
INPUT_FILE_PATH = Path(os.getenv("INPUT_FILE_PATH", "../input/dataset.sav"))
OUTPUT_FILE_PATH = Path(os.getenv("OUTPUT_FILE_PATH", "../output/data_out.sav"))
COLUMN_KEYWORD_TO_CONCATENATE = str(os.getenv("COLUMN_KEYWORD_TO_CONCATENATE", "Author."))
NEW_COLUMN_NAME = str(os.getenv("NEW_COLUMN_NAME", "New Column"))
CONCATENATOR = str(os.getenv("CONCATENATOR", ', '))


def save_output(df, out_file_path):
    if out_file_path.suffix == '.xlxs':
        writer = pd.ExcelWriter(out_file_path, engine="xlsxwriter")
        df.to_excel(writer)
        writer.save()

    elif out_file_path.suffix == '.sav':
        pyreadstat.write_sav(df, out_file_path)

    else:
        raise Exception(f"OUTPUT_FILE_PATH extension is not supported to save : {out_file_path.suffix}")


def read_input(in_file_path):
    if in_file_path.suffix == '.xlxs':
        return pd.read_excel(in_file_path, engine='openpyxl')

    elif in_file_path.suffix == '.sav':
        return pd.read_spss(in_file_path)

    else:
        raise Exception(f"INPUT_FILE_PATH extension is not supported to read : {in_file_path.suffix}")


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

    df = read_input(in_file_path=INPUT_FILE_PATH).fillna('')
    df = concatenator(df=df)
    save_output(df=df, out_file_path=OUTPUT_FILE_PATH)


# USER INPUTS
INPUT_FILE_PATH = Path("C:/Users/Principal/Google Drive/PhD - VTU/#My PhD Work/SPSS/ExtractedData/dataset.xlsx")
OUTPUT_FILE_PATH = Path("C:/Users/Principal/Google Drive/PhD - VTU/#My PhD Work/SPSS/ExtractedData/data_out.xlsx")
COLUMN_KEYWORD_TO_CONCATENATE = str("Author.")
NEW_COLUMN_NAME = str("AuthorConcatenated")
CONCATENATOR = str(', ')
