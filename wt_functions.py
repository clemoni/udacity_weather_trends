import pandas as pd
import numpy as np


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
