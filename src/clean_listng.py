import numpy as np
import pandas as pd

def select_cols(df, cols):
    '''
    Returns df with specified columns
    
    ARGS:
        df - pd.dataFrame
        cols - list of columns
    '''
    columns_to_drop = []
    for x in df.columns:
        if x not in columns_to_keep:
            columns_to_drop.append(x)
    df.drop(columns_to_drop, inplace=True, axis=1)
    return df


def to_float(df, cols):
    '''
    Converts specified columns to float type

    ARGS
        df = DataFrame
        cols = list of column names

    RETURN
        df
    '''
    for c in cols:
        df[c] = df[c].replace({'\$':'', ',':''}, regex = True).astype(float)
    return df

def save(df):
     df.to_pickle('../data/pickled_listings_df')

if __name__ == '__main__':
    df = pd.read_csv('../data/listings.csv')

    columns_to_keep = ['id','host_id','host_listings_count','neighbourhood','neighbourhood_cleansed',
                        'property_type','room_type','price','weekly_price','monthly_price','latitude',
                        'longitude','minimum_nights','maximum_nights','minimum_nights_avg_ntm',
                        'maximum_nights_avg_ntm','requires_license','license','name','summary','space',
                        'description','transit','access','interaction','host_url','listing_url']
    numeric_cols = ['price','weekly_price','monthly_price']

    df = select_cols(df, columns_to_keep)
    df = to_float(df, numeric_cols)
    
    save(df)