
import pandas as pd
from pathlib import Path

class Sheet:
    def __init__(self,sheet_name, df):
        self.sheet_name = sheet_name
        self.sheet_df = df
        self.X = None
        self.Y = None
        self.V = None
        self.values_list = None
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

    def get_values(self):
        self.values_list = sorted(list(set(self.sheet_df[self.V])))

    def agg_1(self, x):
        values = {}
        for value in self.values_list:
            values[value] = 0
        for item in x:
            values[item] += 1
        values = {k: v for k, v in sorted(values.items(), key=lambda item: item[1], reverse=True)}

        out_dic = {}
        for value in values.items():
            if value[1] != 0:
                out_dic[value[0]] = value[1]
        out = str(out_dic)[1:-1].replace("'", "").replace(": ", "(").replace(",", ")") + ")"

        return out

    def agg_2(self, x):
        values = {}
        for value in self.values_list:
            values[value] = 0
        for item in x:
            values[item] += 1
        my_list = []
        for item in values.values():
            my_list.append(item)

        return tuple(my_list)

    def convertor3(self):
        self.get_values()
        new_df = self.sheet_df.pivot_table(values=self.V, index=self.X, columns=self.Y, aggfunc=self.agg_1)
        return new_df

    def convertor4(self):
        self.get_values()
        print(f"Values order: {self.values_list}")
        new_df = self.sheet_df.pivot_table(values=self.V, index=self.X, columns=self.Y, aggfunc=self.agg_2)
        return new_df

    def save_csv(self, df, file_name):
        out_dir = Path("output")
        df.to_csv(out_dir / str(file_name + ".csv"))

    def save_excel(self, df, file_name):
        out_dir = Path("output")
        writer = pd.ExcelWriter(out_dir / str(file_name + ".xlsx"),  engine="xlsxwriter")
        df.to_excel(writer, sheet_name=str(file_name), index=False)
        writer.save()



