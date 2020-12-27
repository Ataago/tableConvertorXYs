
import pandas as pd
from pathlib import Path

from main import main as tableConvertor



df = pd.read_csv("input/mappings.csv")

for idx, row in df.iterrows():
    try:
        if row['exec'] == 1:
            print(f"{idx + 1}. Generating {row['save_as']} for {Path(row['file_path']).name} using {row['convertor']}.")
            tableConvertor(
                file_path=row['file_path'],
                X=row['x'],
                Y=row['y'],
                V=row['v'],
                saveAs=row['save_as'],
                convertor=row['convertor']
            )
        else:
            print(f"{idx + 1}. Skipping.. ")
    except Exception as e:
        print(f"Error in input {idx + 1} of {df.shape[0]}: {e}")
    print()
