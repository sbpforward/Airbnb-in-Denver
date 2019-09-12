import numpy as np
import pandas as pd

def select_cols(df, cols):
    '''
    Returns df with specified columns
    
    ARGS
        df - pd.dataFrame
        cols - list of columns
    '''
    columns_to_drop = []
    for x in df.columns:
        if x not in columns_to_keep:
            columns_to_drop.append(x)
    df.drop(columns_to_drop, inplace=True, axis=1)
    return df
    
def to_datetime(df, cols):
    '''
    Converts specifified column to datetime type as YEAR-MONTH-DATE

    ARGS
        df = DataFrame
        cols = list of column names

    RETURN
        df
    ''' 
    for c in cols:
        df[c] =  pd.to_datetime(df['date'])
    return df

def update_col_name(df):
    '''
    Updates specifified column name(s) to ensure consistency across DataFrames

    ARGS
        df = DataFrame

    RETURN
        df
    ''' 
    df.columns = new_col
    return df

def save(df):
     df.to_pickle('../data/pickled_cal_df')

if __name__ == '__main__':
    df = pd.read_csv('../data/calendar.csv')

    columns_to_keep = ['listing_id','date','available']
    date_cols = ['date']
    new_col = ['id','date','available']

    df = select_cols(df, columns_to_keep)
    df = to_datetime(df, date_cols)
    df = update_col_name(df)

    save(df)