import numpy as np
import pandas as pd

def select_cols(df, cols):
    '''
    Returns pandas DataFrame with desired columns.
    
    Parameters
    ----------
    df: pandas.DataFrame
        DataFrame produced by the listings.csv file.
    cols: array_like
        List of columns to keep
        =============
        id                          latitude                    space
        host_id                     longitude                   description
        host_listings_count         minimum_nights              transit 
        neighbourhood               maximum_nights              access
        neighbourhood_cleansed      minimum_nights_avg_ntm      interaction
        property_type               maximum_nights_avg_ntm      host_url
        room_type                   requires_license            listing_url
        price                       license
        weekly_price                name
        monthly_price               summary
        =============

    Returns
    ----------
    df: pandas.DataFrame
        DataFrame that consists only of the columns passed through.

    '''
    columns_to_drop = []
    for x in df.columns:
        if x not in columns_to_keep:
            columns_to_drop.append(x)
    df.drop(columns_to_drop, inplace=True, axis=1)
    return df


def to_float(df, cols):
    '''
    Converts specifified column to float type.

    Parameters
    ----------
    df: pandas.DataFrame
        Passes the DataFrame that was recently updated to have the
        desired columns.

    cols: array_like
        List of strings of the column names that need to be 
        converted to float.
        =============
        price
        weekly_price
        monthly_price
        =============

    Returns
    ----------
    df: pandas.DataFrame
        Updated DataFrame that updates the 'price' column datatype from a
        string to a float datatype.
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
    float_cols = ['price','weekly_price','monthly_price']

    df = select_cols(df, columns_to_keep)
    df = to_float(df, float_cols)
    
    save(df)