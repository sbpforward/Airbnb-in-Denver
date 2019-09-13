import numpy as np
import pandas as pd

def select_cols(df, cols):
    '''
    Returns pandas DataFrame with desired columns.
    
    Parameters
    ----------
    df: pandas.DataFrame
        DataFrame produced by the calendar.csv file.
    cols: list
        List of columns to keep
        =============
        listing_id
        date
        available
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
    
def to_datetime(df, cols):
    '''
    Converts specifified column to datetime type as YEAR-MONTH-DATE.

    Parameters
    ----------
    df: pandas.DataFrame
        The DataFrame that was recently passed through and updated to have
        the necessary columns.

    cols: list
        List of the column name that needs to be converted to datetime.
        =============
        date
        =============
    Returns
    ----------
    df: pandas.DataFrame
        Updated DataFrame that updates the 'date' column datatype from a
        string to a datetime datatype.
    ''' 
    for c in cols:
        df[c] =  pd.to_datetime(df['date'])
    return df

def update_col_name(df,cols):
    '''
    Updates column names to ensure smooth merging and consistency across
    DataFrames within the /data folder. For example: in the calendar.csv
    the listing ID variable is referred to as "listing_id". However in the 
    listing.csv, it is referred to as simply "id". 

    Parameters
    ----------
    df: pandas.DataFrame
        Passes in the DataFrame that has the designated columns and updated
        'date' datatype.  
    new_col: list
        A list of strings with the desired new column variables.
        =============
        id
        date
        available
        =============

    Returns
    ----------
    df: pandas.DataFrame
        A ready-to-save DataFrame after completing all the requirements to get
        it ready for digging into!

    ''' 
    df.columns = cols
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
    df = update_col_name(df, new_col)

    save(df)