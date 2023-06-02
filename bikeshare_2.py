import time
import pandas as pd
import numpy as np


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
        user_input_city = input('Select a city (chicago, new york city or washington): ')
        if user_input_city in ["chicago", "new york city", "washington"]:
            break
        else:
            print("Invalid input. Please enter a valdi city")
    print("You have selected: ", user_input_city)
    city = user_input_city

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        user_input_month = input('Select a month (all, january, february, march, april, may, june) :')
        if user_input_month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid input. Please enter a valid month")
    print("You have selected: ", user_input_month)
    month = user_input_month


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        user_input_day_of_the_week = input('Select a day of the week (all, monday, thuesday, wednesday, thursday, friday, saturday, sunday):')
        if user_input_day_of_the_week in ['all', 'monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
         break
        else:
          print("Invalid input. Please enter a valid day of the week: ")
    print("You have selected: ", user_input_day_of_the_week)
    day = user_input_day_of_the_week

    return city, month, day
#print(city)
print('-'*40)
print("test")

def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

"""
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    popular_day = df['day'].mode()[0]
    print('Most Popular day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    # convert the Start Time column to datetime


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('most used start station:', most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('most used end station:', most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_sec = df['Trip Duration'].sum()
    print('Total travel Time in sec: ', total_travel_time_sec)
    print('Total travel Time in min: ', (total_travel_time_sec / 60))
    print('Total travel Time in hour: ', (total_travel_time_sec / 3600))
    print(' ')
    # TO DO: display mean travel time
    mean_travel_time_sec = df['Trip Duration'].sum()
    mean_travel_time_len = len(df['Trip Duration'])
    mean_travel_time_sec = mean_travel_time_sec / mean_travel_time_len
    print('mean travel time in sec: ', mean_travel_time_sec)
    print('mean travel time in min: ', (mean_travel_time_sec / 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ', user_types)
    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('Counts of user gender: ', counts_of_gender)
    except KeyError:
        print('Counts of user gender have no data. ')


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].dt.year.min()
    print('earliest year of birth: ', earliest_year_of_birth)

    most_recent_year_of_birth = df['Birth Year'].dt.year.max()
    print('most recent year of birth: ', most_recent_year_of_birth)

    most_common_year_of_birth = df['Birth Year'].mode()[0]
    print('most common year of birth: ', most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
