from configs import __X__, __Y__, __VALUE__

import pandas as pd
from pathlib import Path

class Sheet:
    def __init__(self,sheet_name, df):
        self.sheet_name = sheet_name
        self.sheet_df = df
        self.X = None
        self.Y = None
        self.V = None
        self.col_names = []

        self.get_col_names()

    def get_col_names(self):
        self.col_names = list(self.sheet_df.columns)

    def save_col(self, col_name):
        if col_name not in self.col_names:
            print(f"{col_name} not exists in {self.sheet_name}")
            raise Exception
        return True

    def save_cols(self, X, Y, V):
        if self.save_col(X):
            self.X = X
        if self.save_col(Y):
            self.Y = Y
        if self.save_col(V):
            self.V = V


    def convertor1(self):
        Xs = []
        for col in self.col_names:
            if col != self.Y and col != self.V:
                Xs.append(col)

        new_df = self.sheet_df.pivot_table(values=self.V, index=Xs, columns=self.Y, aggfunc="sum")
        return new_df

    def convertor2(self):
        new_df = self.sheet_df.pivot_table(values=self.V, index=self.X, columns=self.Y, aggfunc="sum")
        return new_df

    def save_csv(self, df, file_name):
        out_dir = Path("output")
        df.to_csv(out_dir / file_name)



