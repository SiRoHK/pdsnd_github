import time
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("Please Select one From the list [chicago, new york city, washington]:").lower()
        if city in CITY_DATA:
          break
        else:
            print("Wrong input!")

        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Which month? all,January, February, March, April, May,or June? Please type out the full month name.\n").lower()
        if month =='january' or month =='all' or month =='february'or month =='march'or month=='april'or month=='may'or month=='june':
            break
        else:
            print("Wrong input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Which day? type one of the week day  (e.g. all, Sunday,Monday...).\n").lower()
        if day=='sunday' or day=='monday' or day== 'tuesday ' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day =='saturday' or day =='all':
            break
        else:
          print("Wrong input!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month_name()
    df['day_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
      df = df[ df['month'] == month.title()];

    if day != 'all':
        df = df[ df['day_name'] == day.title()];

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is :",df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("The most common day of week is :",df['day_name'].value_counts().idxmax())


    # TO DO: display the most common start hour
    print("The most common start hour is :",df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is :",df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print("The most common end station is :",df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    print("The most common start station and end station :",pd.DataFrame(df.groupby(['Start Station','End Station']).size().sort_values(ascending = False)).iloc[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time :",df["Trip Duration"].sum()," seconds")

    # TO DO: display mean travel time
    print("mean travel time :",df["Trip Duration"].mean()," seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types : \n",df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if 'Gender'in df:
        print("counts of gender :\n",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("The most earliest birth year : ",df['Birth Year'].min())
        print("The most recent birth year : ",df['Birth Year'].max())
        print("The most common year of birth : ",df['Birth Year'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data."""
    start_loc=0
    while True:
        view_data  = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data.lower() != 'yes':
            break
        print(df.iloc[start_loc:start_loc+5,:])
        start_loc += 5

        
    return" ";
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
