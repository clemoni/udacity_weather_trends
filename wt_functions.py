import pandas as pd
import numpy as np


def get_file(path_name):
    """return a dataFrame from cvs file

    Args:
        path_name ([str]): path to the file

    Returns:
        [dataFrame]
    """
    return pd.read_csv(path_name)


def set_index_col(df, col):
    """set a given column to index

    Args:
        df ([dataFrame]):
        col ([obj]): 

    Returns:
        [dataFrame]:
    """
    df = df.set_index(df[col])
    return df


def trim_df(df, *cols):
    """Removed unwanted column to a DataFrame
    Args:
        df ([DataFrame]): a dataFrame
    Returns:
        [list]: list of columns name 
    """
    len_col_origin = len(df.columns)
    for col in cols:
        del df[col]
    len_col_trimed = len(df.columns)

    if len_col_origin > len_col_trimed:
        return '{del_col} column(s) deleted'.format(del_col=len_col_origin - len_col_trimed)


def rename_col(df, origin_col_name, new_col_name):
    """Rename a column name

    Args:
        df ([datFrame]): the dataFrame that included the column
        origin_col_name ([str]): the name of the original column
        new_col_name ([str]):the new name

    Returns:
        [dataFrame]: the dataFrame with the newly named column
    """
    return df.rename({origin_col_name: new_col_name}, axis='columns')


def get_temperature(i, col):
    return round(df.loc[i:i+9, col].mean(axis=0), 2)


def get_row_val(i, year_max):
    i_plus = year_max if year_max < i+9 else i+9
    year_range = f'{i}-{i_plus}'
    return [i, year_range, get_temperature(i, 'dublin'), get_temperature(i, 'world')]


def insert_data(data):
    index_list.append(data[0])
    data_list.append(data[1:5])


def main():
    print('active functions module')


if(__name__ == '__main__'):
    main()
