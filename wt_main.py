import pandas as pd
import numpy as np
import wt_functions as wt_func


def prep_df():

    # get DF from csv file
    df = wt_func.prep_index('./data/wt_data.csv', 'year')
    # get the name of the city
    city_name = df.iloc[0][0]
    # modified column 'temp_city' to add the city
    col_name_updated = f'temp_city {city_name }'
    # modified the column in the DF
    df = wt_func.rename_col(df, 'temp_ciy', col_name_updated)
    # remove column year, city not needed anymore
    wt_func.trim_df(df, 'year', 'city')

    return df


def main():
    print('main file')
    df = prep_df()

    print(df)


if(__name__ == '__main__'):
    main()
