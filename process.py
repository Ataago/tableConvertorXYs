
import pandas as pd
from main import main as tableConvertor


df = pd.read_csv("input/mappings.csv")

for idx, row in df.iterrows():
    try:
        if row['exec'] == 1:
            tableConvertor(
                file_path=row['file_path'],
                X=row['x'],
                Y=row['y'],
                V=row['v'],
                saveAs=row['save_as'],
                convertor=row['convertor']
            )
            print(f"Generated {row['save_as']} for {row['file_path']} using {row['convertor']}.")
    except Exception as e:
        print(e)
