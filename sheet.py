
import pandas as pd
from pathlib import Path
from ast import literal_eval

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

    def validate_cols(self, col_names):
        try:
            col_names = literal_eval(col_names)
        except Exception as err:
            print(f"Please check the mappings CSV for '{col_names}' syntax, should be ['something1', 'something2']")

        for col_name in col_names:
            if col_name not in self.col_names:
                print(f"'{col_name}' does not exist in '{self.sheet_name}'")
                raise Exception
        return col_names

    def validate_col(self, col_name):
        if col_name not in self.col_names:
            print(f"'{col_name}' does not exist in '{self.sheet_name}'")
            raise Exception
        return col_name

    def save_cols(self, X, Y, V):
        self.X = self.validate_cols(X)
        self.Y = self.validate_cols(Y)
        self.V = self.validate_col(V)

    def convertor1(self):
        Xs = []
        for col in self.col_names:
            if col not in self.Y and col != self.V:
                Xs.append(col)

        new_df = self.sheet_df.pivot_table(values=self.V, index=Xs, columns=self.Y, aggfunc="sum")
        return new_df

    def convertor2(self):
        new_df = self.sheet_df.pivot_table(values=self.V, index=self.X, columns=self.Y, aggfunc="sum")
        return new_df

    def get_values(self):
        self.values_list = sorted(list(set(self.sheet_df[self.V])))

    @staticmethod
    def get_super(x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)

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

        out = ""
        for key, val in out_dic.items():
            out += key
            if val > 1:
                out += self.get_super(x=str(val))

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
        df.to_excel(writer, sheet_name=str(file_name))
        writer.save()



