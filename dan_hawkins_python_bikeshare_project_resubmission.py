import time
import pandas as pd
import numpy as np
import sys

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
    # Get user input for city (chicago, new york city, washington). Use a while loop to repeat process until the enter a valid input.
    city = ''
    while city != 'quit':
        print('Please select which city you would like to explore. You can enter Chicago, New York City, or Washington. \nTo quit this program enter quit for any of the first three questions.\n')
        city = input('\nPlease enter your city here: ')
        #enure the user response is lowercase
        city = city.lower()
        #Respond to the user's city choice
        #Please note that city, month, and day selection idea on formating came from this website: http://introtopython.org/while_input.html
        if city == 'chicago':
            print('\nGreat you selected Chicago./n') # Let the user know they've chosen chicago
            break
        elif city == 'new york city':
            print('\nGreat you selected New York City.\n') # Let the user know they've chosen New York City
            break
        elif city == 'washington':
            print('\nGreat you selected Washington./n') # Let the user know they've chosen Washington
            break
        elif city == 'quit':
            print('\nOkay. Goodbye.') # Let the user know they've quit the program
            sys.exit() #How to exit a program came from this website: https://stackoverflow.com/questions/179369/how-do-i-abort-the-execution-of-a-python-script
            break
        else:
            print('\nI do not understand, please try again.\n') # Let the user know their answer is incomplete and they need to try again



    # Get user input for month selection (all, january, february, ... , june)
    month = ''
    while month != 'quit':
        print('Please select which month you would like to analyze. You can select All, January, February, March, April, May or June. \nTo quit this program enter quit for any of the first three questions.\n')
        month = input('\nPlease enter your month selection here: ')
        month = month.lower()

        #Respond to the user's month choice
        if month == 'all':
            print('\nGreat you selected All Months.\n') # Let the user know they've selected all months
            break
        elif month == 'january':
            print('\nGreat you selected the month of January.\n') # Let the user know they've selected January
            break
        elif month == 'february':
            print('\nGreat you selected the month of February.\n') # Let the user know they've selected February
            break
        elif month == 'march':
            print('\nGreat you selected the month of March.\n') # Let the user know they've selected March
            break
        elif month == 'april':
            print('\nGreat you selected the month of April.\n') # Let the user know they've selected April
            break
        elif month == 'may':
            print('\nGreat you selected the month of May.\n') # Let the user know they've selected May
            break
        elif month == 'june':
            print('\nGreat you selected the month of June.\n') # Let the user know they've selected June
        elif month == 'quit':
            print('\nOkay. Goodbye.\n') # Let the user know they've quit the program
            sys.exit()
        else:
            print('\nI do not understand, please try again.\n') # Let the user know their answer is incomplete and they need to try again

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day != 'quit':
        print('Please select which day you would like to analyze. You can select All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday. \nTo quit this program enter quit for any of the first three questions.\n')
        day = input('\nPlease enter your day selection here: ')
        day = day.lower()

        #Respond to the user's month choice
        if day == 'all':
            print('\nGreat you selected All Days.\n') # Let the user know they've selected all days
            break
        elif day == 'monday':
            print('\nGreat you selected the day Monday.\n') # Let the user know they've selected Monday
            break
        elif day == 'tuesday':
            print('\nGreat you selected the day Tuesday.\n') # Let the user know they've selected Tuesday
            break
        elif day == 'wednesday':
            print('\nGreat you selected the day Wednesday.\n') # Let the user know they've selected Wednesday
            break
        elif day == 'thursday':
            print('\nGreat you selected the day Thursday.\n') # Let the user know they've selected Thursday
            break
        elif day == 'friday':
            print('\nGreat you selected the day Friday.\n') # Let the user know they've selected Friday
            break
        elif day == 'saturday':
            print('\nGreat you selected the day Saturday.\n') # Let the user know they've selected Saturday
            break
        elif day == 'sunday':
            print('\nGreat you selected the day Sunday.\n') # Let the user know they've selected Sunday
            break
        elif day == 'quit':
            print('\nOkay. Goodbye.\n') # Let the user know they've quit the program
            sys.exit()
        else:
            print('\nI do not understand, please try again.\n') # Let the user know their answer is incomplete and they need to try again


    print('-'*40)
    return city, month, day


def load_data(city, month, day): # I copied this code directly from the third practice problem
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # Pre loaded data provided by Udacity
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nThe most common month (Please note a result of 1 = January, 2 = February, etc.): ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nThe most common day: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\nThe most common start hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    # Pre loaded data provided by Udacity
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common start station is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['best_station_combo'] = df['Start Station'] + ' ' + df['End Station']
    print('\nThe most frequent start and end station combination is: {0} '.format(df.best_station_combo.mode()[0])) # An engineer at my company helped me through this one. I'm not sure if that counts as "citing your work" but thought I'd call that out to ensure I'm adhering to the Udacity Honor Code.

    # Pre loaded data provided by Udacity
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    # Pre loaded data provided by Udacity
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print('\nThe total travel time is: ', total_travel_time, 'minutes')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('\nThe mean travel time is: ', mean_travel_time, 'minutes')

    # Pre loaded data provided by Udacity
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    # Pre loaded data provided by Udacity
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe user stats are: ')
    print(user_types)

    # TO DO: Display counts of gender
    try: #Run this code when we have gender data
        gender_counts = df['Gender'].value_counts()
        print('\nThe gender stats are: ')
        print(gender_counts)
    except KeyError: # Call out washington doesn't have any of this data and therefore cannot report on it
        print('\nWashington does not have any gender data to report.')


    # TO DO: Display earliest, most recent, and most common year of birth
    try: #Run this code when we have birth year data
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year of a user is: ', earliest)
        print('\nThe most recent birth year of a user is: ', most_recent)
        print('\nThe most common birth year amongst users is: ', most_common_year)
    except KeyError: # Call out that washington does not have any of this data and therefore cannot report on it
        print('\nWashington does not have any birth year data to report.')

    # Pre loaded data provided by Udacity
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Shows the user the first 5 lines of data, and continuously asks if they'd like to until told to stop by the user"""
    print('\nRaw Data')
    # Get user input for if they want to see the raw data. Use a while loop to repeat process until they user ends the program.
    answer = ''
    i = 0
    n = 5
    while answer != 'no':
        answer = input('\nWould you like to see five lines of raw data? ')
        #enure the user response is lowercase
        answer = answer.lower()
        #Respond to the user's choice


        if answer == 'yes':
            print('\nOkay here are five lines of raw data') # Let the user know they've chosen to see the raw data
            print(df.iloc[i:n]) #Format for this line came from https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
            i = i + 5
            n = n + 5
        else:
            print('Okay. The program is over.')

# Pre loaded data provided by Udacity
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

# Pre loaded data provided by Udacity
if __name__ == "__main__":
	main()
