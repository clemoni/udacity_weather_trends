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


def get_temperature(df, i, col):
    """group year by range of 9
    and return average temperature for a given column

    Args:
        df ([dataFrame]): 
        i ([int]): the starting year of the decade
        col ([str]): name of the column

    Returns:
        [float]: average of temperature for year range
    """
    return round(df.loc[i:i+9, col].mean(axis=0), 2)


def get_row_val(df, i, year_max, col_city, col_world):
    """return value for average temperature for 
    range of year. 

    Args:
        df ([datFrame]): 
        i ([int]): teh first year of the decade
        year_max ([int]): the max year use a test to stop
        col_city ([str]): name of column city
        col_world ([str]): name of column world_temp

    Returns:
        [list]: return list of essentail value for each row
        year (index), year range, temperature for city picked, temperature for world
    """
    # text if i_plus if bigger means that needs to take value of
    # year_max instead. Since behond of last range.
    i_plus = year_max if year_max < i+9 else i+9
    year_range = f'{i}-{i_plus}'
    return [i, year_range, get_temperature(df, i, col_city), get_temperature(df, i, col_world)]


def insert_data(data, index_list, data_list):
    """insert values to index_list and data_list
       in order to be added to new dataFrae

    Args:
        data ([list]): list of value
        index_list ([list]):
        data_list ([list]): 
    """
    index_list.append(data[0])
    data_list.append(data[1:5])


def convert_to_html(df, path_to_file):
    # render dataframe as html
    html = df.to_html()
    # write html to file
    text_file = open(path_to_file, 'w')
    text_file.write(html)
    text_file.close()


def main():
    print('active functions module')


if(__name__ == '__main__'):
    main()
