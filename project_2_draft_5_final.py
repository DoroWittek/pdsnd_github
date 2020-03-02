import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# start of added code
months = ('january', 'february', 'march', 'april', 'may', 'june')

weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday', 'sunday')

def choice(prompt, choices=('y', 'n')):

    while True:
        choice = input(prompt).lower().strip()
        # typing end will terminate the program
        if choice == 'end':
            raise SystemExit
        # for input with only one name
        elif ',' not in choice:
            if choice in choices:
                break
        # for input with more than one name
        elif ',' in choice:
            choice = [i.strip().lower() for i in choice.split(',')]
            if list(filter(lambda x: x in choices, choice)) == choice:
                break

        prompt = ("\nPython cannot process your input correctly. Please enter "
                  "correctly spelled input in lower letters:\n>")

    return choice
# end of added code

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
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # start of added code for the first tasks:

    while True:
        city = choice("\nWould you like to see data for Chicago, New York City, "
                     "or Washington? Use commas to list the names.\n>",
                     CITY_DATA.keys())
        month = choice("\nWould you like to see data from January, February, "
                      "March, April, May, or June? Feel free to list several "
                      "months. Use commas to list the names.\n>", months)
        day = choice("\nWould you like to see data from Monday, Tuesday, "
                    "Wednesday, Thursday, Friday, Saturday or Sunday? "
                    "Feel free to list several weekdays."
                    "Use commas to list the names.\n>", weekdays)

        # ask the user to confirm his/her input
        confirmation = choice("\nAre you sure that you would like to apply "
                              "the following filter(s) to the data:"
                              "\n\n City/Cities: {}\n Month(s): {}\n Weekday(s)"
                              ": {}\n\n [y] Yes\n [n] No\n\n>"
                              .format(city, month, day))
        if confirmation == 'y':
            break
        else:
            print("\nPlease enter your desired filters for city, month and day once again!")

# end of added code

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
# start of added code

    print("\nPythong is loading the data considering your desired filters.")
    start_time = time.time()

    # filter data concerning the entered city filters
    if isinstance(city, list):
        df = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),
                       sort=True)
        # reorganize data frame
        try:
            df = df.reindex(columns=['Unnamed: 0', 'Start Time', 'End Time',
                                     'Trip Duration', 'Start Station',
                                     'End Station', 'User Type', 'Gender',
                                     'Birth Year'])
        except:
            pass
    else:
        df = pd.read_csv(CITY_DATA[city])

    # create columns for time statistics
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    # filter data concerning the desired month and weekday into new data frames
    if isinstance(month, list):
        df = pd.concat(map(lambda month: df[df['Month'] ==
                           (months.index(month)+1)], month))
    else:
        df = df[df['Month'] == (months.index(month)+1)]

    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]

    print("\nThanks to the power of panda, this only took {} seconds.".format((time.time() - start_time)))
    print('-'*40)

# end of added code

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour

# start of added code

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print('The most common month in your filtered data is: ' +
          str(months[most_common_month-1]).title() + '.')

    # display the most common day of week
    most_common_day = df['Weekday'].mode()[0]
    print('The most common day of the week in your filtered data is: ' +
          str(most_common_day) + '.')

    # display the most common start hour
    most_common_hour = df['Start Hour'].mode()[0]
    print('The most common start hour in your filtered data is: ' +
          str(most_common_hour) + '.')

# end of added code

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip

# start of added code

    # display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("The most common start station in your filtered data is: " +
          most_common_start_station)

    # display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0])
    print("The most common end station in your filtered data is: " +
          most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("The most common combination of start station and end sation "
          " in your filtered data is: " + most_common_start_end_combination)

# end of added code

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # TO DO: display mean travel time

    # start of added code

# display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print("The total travel time for your filtered data is : " +
          total_travel_time + ".")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print("The mean travel time for your filtered data is : " +
          mean_travel_time + ".")

    # end of added code

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

# start of added code

# Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Frequency of user types:")
    print(user_types)

    # Display counts of gender
    try:
        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nFrequency of gender:")
        print(gender_distribution)
    except KeyError:
        print("Sorry! Unfortunately, there are no counts of gender")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nThe earliest year of birth in your filtered data is "
              + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("The most recent year of birth in your filtered data is "
              + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("The most common year of birth in your filtered data is "
              + most_common_birth_year)
    except:
        print("Sorry! Unfortunately, there are no counts of birth years")

# end of added code

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# start of added code
# display raw data
# cretaed with the help of github: https://github.com/finish06/PDSND-Project-3 

def raw_data(df):

    display_raw_input = input("\nDo you want Python to display raw data? Enter 'yes' or 'no'\n").strip().lower()
    if display_raw_input in ("yes", "y"):
        i = 0

        while True:
            if (i + 5 > len(df.index) - 1):
                print(df.iloc[i:len(df.index), :])
                print("End of raw data was reached.")
                break

            print(df.iloc[i:i+5, :])
            i += 5

            show_next_five_input = input("\nWould you like to see the next 5 rows? Enter 'yes' or 'no'\n").strip().lower()
            if show_next_five_input not in ("yes", "y"):
                break

# end of added code

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


if __name__ == "__main__":
	main()
