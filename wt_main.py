import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wt_functions as wt_func


def prep_df():

    # get DF from csv file
    df = wt_func.get_file('./data/wt_data.csv')
    df = wt_func.set_index_col(df, 'year')
    # get the name of the city
    city_name = df.iloc[0][1]
    # modified column 'temp_city' to add the city
    col_name_updated = f'temp_city {city_name }'
    # modified the column in the DF
    df = wt_func.rename_col(df, 'temp_ciy', col_name_updated)
    # remove column year, city not needed anymore
    wt_func.trim_df(df, 'year', 'city')

    return (df, col_name_updated)


def group_moving_average(df, col_name_updated, col_world_name):

    # Create list index, data, and column to be inserted at the end in new dataFrame
    # each list be happened with value
    index_list = list()
    data_list = list()
    columns_list = ['year_range', col_name_updated, col_world_name]

    # get min data and max data to control loop
    year_min, year_max = (df.index.min(), df.index.max())

    # create list of decade date
    decade_list = list(range(year_min, year_max, 10))

    # for each date:
    # - group row corresponding + 9 below to get mean()
    # - extract: the mean for the city and wold
    # - create data range for better understanding

    [wt_func.insert_data(
        wt_func.get_row_val(
            df, i, year_max, col_name_updated, col_world_name),
        index_list,
        data_list)
     for i in decade_list]

    # create new dataFrame

    return pd.DataFrame(
        data=data_list, columns=columns_list, index=index_list)


def insert_delta_col(df, col_city_name_updated, col_world_name):
    # create and insert col delta with difference between temperature
    # city and temperature world
    df['delta'] = df[col_city_name_updated]-df[col_world_name]
    return df


def df_to_plot(df, col_city_name_updated, col_world_name):
    # print plot from col temperatur city and temperature world
    df = df.loc[:, [col_city_name_updated, col_world_name]]
    plt.close("all")
    plt.figure()
    df.plot()
    plt.show()


def main():
    print('main file')

    prep_df()

    df,  col_city_name_updated = prep_df()
    col_world_name = 'temp_world'

    df = group_moving_average(df, col_city_name_updated, col_world_name)

    df = insert_delta_col(df, col_city_name_updated, col_world_name)

    wt_func.convert_to_html(df, 'html/index.html')

    df_to_plot(df, col_city_name_updated, col_world_name)


if(__name__ == '__main__'):
    main()
