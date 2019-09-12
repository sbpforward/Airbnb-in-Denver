import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_top_10_neighborhoods(df):
    '''
    Groups neighborhoods and room types, then counts the number 
    of room types and adds it to a new column called "count".
    Returns the sum of the number of room types for each neighborhood 
    and puts them in descending order.

    ARGS
        df - pd.dataFrame

    RETURN
        df - pd.dataFrame
    '''
    df_top_10_neighborhoods = pd.DataFrame()

    temp = df.groupby(['neighbourhood_cleansed','room_type']).size().to_frame('count').reset_index()
    temp = temp.groupby(['neighbourhood_cleansed'])['count'].sum().sort_values(ascending=False)
    df_top_10_neighborhoods = temp.iloc[0:10].reset_index()

    return df_top_10_neighborhoods

def get_top_10_neighborhoods_list(df_top_10_neighborhoods):
    '''
    Creates a list of strings of the top 10 neighborhoods

    ARGS
        df - pd.dataFrame

    RETURN
        list
    '''
    top_10_neighborhood_lst = df_top_10_neighborhoods['neighbourhood_cleansed'].tolist()

    return top_10_neighborhood_lst

def plot_top_10_neighborhoods(df_top_10_neighborhoods, city):
    '''
    Saves bar chart image of the city's top 10 neighborhoods with the most Airbnb listings

    ARGS
        df - pd.dataFrame
        city - str 

    RETURN
        plot - jpeg
    '''
    ax = df_top_10_neighborhoods.plot.bar(x='neighbourhood_cleansed', y='count', rot=45, figsize=(10, 6), legend=False)
    ax.set_xlabel("Neighborhood", fontsize=14)
    ax.set_ylabel("# of Total Listings", fontsize=14)
    plt.title(f'Top 10 {city} Neighborhoods with Most Available Airbnb Listings', fontsize=20)
    plt.tight_layout()
    # plt.savefig(f'top-10-neighborhoods-in-{city}-with-most-airbnb-listings.jpeg')
    # plt.show()

def get_top_10_neighborhoods_and_room_type(df, top_10_neighborhood_lst):
    '''
    Groups neighborhoods and room types, then counts the number of 
    room types and adds it to a new column called "count"
    
    ARGS
        df - pd.dataFrame
        list - list of strings

    RETURN
        df - pd.dataFrame
    '''
    df_top_10_neighborhoods_and_room_type = pd.DataFrame()
    
    df = df.groupby(['neighbourhood_cleansed','room_type']).size().to_frame('count').reset_index()

    for neighborhood in top_10_neighborhood_lst:
        temp = df[df.neighbourhood_cleansed == neighborhood]
        df_top_10_neighborhoods_and_room_type = df_top_10_neighborhoods_and_room_type.append(temp)

    return df_top_10_neighborhoods_and_room_type

def plot_top_10_neighborhoods_and_room_type(df_top_10_neighborhoods_and_room_type, city):
    '''
    Saves bar chart image featuring top 10 neighborhoods by room type

    ARGS
        df - pd.dataFrame
        city - string

    RETURN
        plot - jpeg
    '''
    plt.figure(figsize=(12, 6))

    ax = sns.barplot(x="neighbourhood_cleansed", y="count", hue="room_type", palette='YlOrRd', data=df_top_10_neighborhoods_and_room_type)
    ax.set_xlabel("Neighborhood", fontsize=14)
    ax.set_ylabel("Number of Listings", fontsize=14)
    ax.set_title(f'Most Available Neighborhoods on Airbnb in {city} by Room Type', fontsize=20)
    plt.gca().legend().set_title('Room Type')
    plt.legend(loc=1, prop={'size': 14})

    plt.tight_layout()
    # plt.savefig('most-available-airbnb-listings-in-{city}-by-room-type.jpeg')
    # plt.show()


    
if __name__ == '__main__':
    df = pd.read_pickle('../data/pickled_listings_df')

    get_top_10_neighborhoods(df)
    
    # Counts and pulls the top 10 neighborhoods with the most total Airbnb listings
    df_top_10_neighborhoods = get_top_10_neighborhoods(df)

    # Creates list of top 10 neighborhoods
    top_10_neighborhood_lst = get_top_10_neighborhoods_list(df_top_10_neighborhoods)

    # Plots the top 10 neighborhoods
    plot_top_10_neighborhoods(df_top_10_neighborhoods, 'Denver')


    df_top_10_neighborhoods_and_room_type = get_top_10_neighborhoods_and_room_type(df, top_10_neighborhood_lst)

    plot_top_10_neighborhoods_and_room_type(df_top_10_neighborhoods_and_room_type, 'Denver')