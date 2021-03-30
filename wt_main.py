import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wt_functions as wt_func


def prep_df():

    # get DF from csv file
    df = wt_func.get_file('./data/wt_data.csv')
    df = wt_func.set_index_col(df, 'year')

    # get the name of the city
    col_1_name = df.iloc[0][1]
    col_2_name = 'World'
    # modified column 'temp_city' to add the city

    # modified the column in the DF
    df = wt_func.rename_col(df, 'temp_ciy', col_1_name)
    df = wt_func.rename_col(df, 'temp_world', col_2_name)
    # remove column year, city not needed anymore
    wt_func.trim_df(df, 'year', 'city')

    return (df, col_1_name, col_2_name)


def get_sma_20(df, col_name):
    """Compute Simple Moving Average 
    by using function rolling

    Args:
        df ([dataFame]): 
        col_name ([str]): 

    Returns:
        [serie]: 
    """
    return df[col_name].rolling(20, min_periods=1).mean()


def insert_delta_col(df, col_name_1, col_name_2):
    # create and insert col delta with difference between temperature
    # city and temperature world
    return df[col_name_1]-df[col_name_2]


def get_describe(df, col_name, year_1, year_2):
    """Compute statistics by using describe() function
    between year range

    Args:
        df ([dataFame]): 
        col_name ([str]): 
        year_1 ([int]): 
        year_2 ([int]): 

    Returns:
        [serie]: 
    """
    return df.loc[year_1:year_2, col_name].describe()


def feed_index_data(index_list, data_list, index, data):
    index_list.append(index)
    data_list.append(data)


def describe_year_perdiod(df, year_period, col_name):
    # create list data and list inde
    # to be insert in dataFrmae
    data_list = list()
    index_list = list()

    # for each couple year_1 and year_2 of the list
    # get statistics data with Describe
    # append data and year range to data_list and index_list
    for year_range in year_period:
        s = get_describe(df, col_name, year_range[0], year_range[1])
        feed_index_data(index_list, data_list,
                        f'{year_range[0]}-{year_range[1]}', s.to_dict())

    df = pd.DataFrame(data=data_list, index=index_list)
    df.index.name = col_name

    # return new dataFrame
    return df


def df_to_plot(df, xaxis, title_plot, *cols):
    """Render line chart from a given dataFame

    Args:
        df ([dataFrame]): 
        xaxis ([list]): 
        title_plot ([str]): 
    """
    cols_list = [col for col in cols]
    plt.close("all")
    # colors for the line plot
    colors = ['blue', 'red']

    df[cols_list].plot(
        color=colors, figsize=(12, 4), use_index=True, grid=True, alpha=0.8)
    plt.xticks(xaxis)

    # modify ticks size
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(labels=cols_list, fontsize=14)

    # title and labels
    plt.title(title_plot, fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Temperature [°C]', fontsize=14)

    plt.show()


def main():
    print('main file')

    prep_df()

    df, city_name, world_name = prep_df()
    sma_city = f'SMA_20 {city_name}'
    sma_world = f'SMA_20 {world_name}'

    # Compute the moving average by using the rolling function
    # Round result to decimal ten
    df[sma_city] = round(get_sma_20(df, city_name), 2)
    df[sma_world] = round(get_sma_20(df, world_name), 2)
    df['delta'] = insert_delta_col(
        df, sma_city, sma_world)

    # Devided year range between 3 time period
    # for each get statistic for the sma of city and world
    # and the delta
    year_period = [(1752, 1900), (1900, 1975), (1975, 2013)]
    df_sma_city = describe_year_perdiod(df, year_period, sma_city)
    df_sma_world = describe_year_perdiod(df, year_period, sma_world)
    df_delta = describe_year_perdiod(df, year_period, 'delta')

    # convert data to html
    # wt_func.convert_to_html(df_delta, 'html/index.html')

    # render plot
    # create axis by year range with a step of 15
    xaxis = get_year_range(df, 15)
    title_plot = f'Evolution temperature between {city_name} and {world_name}'
    df_to_plot(df, xaxis, title_plot, 'SMA_20 Dublin', 'SMA_20 World')


if(__name__ == '__main__'):
    main()
