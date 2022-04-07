from tabulate import tabulate
import json

class DataFrame:

    def __init__(self, data={}):
        if DataFrame.is_valid(data):
            self.data = data
        else:
            raise ValueError("DataFrame Creation Error : Data is not valid")

    @property
    def columns(self):
        return list(self.data.keys())

    @columns.setter
    def columns(self, new_columns):
        result = {}
        for (old_col, new_col) in list(zip(self.columns, new_columns)):
            result[new_col] = self.data[old_col]
        self.data = result

    def get_column(self, col_name):
        return self.data[col_name]

    def get_row(self, i):
        result = {}
        for col in self.columns:
            result[col] = self.data[col][i]
        return result

    def copy(self):
        return DataFrame(self.data)

    def to_json(self, filepath):
        try:
            with open(filepath, 'w') as f:
                f.write(json.dumps(self.data))
        except Exception as e:
            print(f"Error: {e}")

    def __str__(self):
        return tabulate(self.data, self.columns, 'pretty')

    def __repr__(self):
        return tabulate(self.data, self.columns, 'pretty')

    def __len__(self):
        return len(self.data[self.columns[0]]) if len(self.data) else 0

    def __getitem__(self, col_name):
        return self.data[col_name]

    def __setitem__(self, col_name, values):
        self.data[col_name] = values
        self.columns = list(self.data.keys())

    def __iter__(self):
        return iter(self.columns)

    def __add__(self, df):
        result = {}
        for key in self.data.keys():
            type_key_df1 = type(self.data[key][0])
            type_key_df2 = type(df[key][0])
            if type_key_df1 is type_key_df2:
                result[key] = self.data[key] + df[key]
            else:
                raise ValueError("Error : DF1 has not the same type as DF2")
        return DataFrame(result)

    @classmethod
    def read_json(cls, filepath):
        try:
            with open(filepath, 'r') as f:
                data = json.loads(f.read())
            return DataFrame(data)
        except Exception as e:
            print(f"Error : {e}")

    @staticmethod
    def is_valid(data_dict):
        if not isinstance(data_dict, dict):
            return False
        cols = list(data_dict.keys())
        if not len(cols):
            return False
        for col in cols:
            values = data_dict[col]
            if not isinstance(values, list):
                return False
            if len(values) != len(data_dict[cols[0]]):
                return False
            for value in values:
                if type(value) is not type(values[0]):
                    return False
        return True