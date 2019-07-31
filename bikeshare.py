import time
import datetime
import pandas as pd
import numpy as np
import calendar


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
        city = input('Please choose Chicago, New York City or Washington: ')
        if city.lower() not in CITY_DATA.keys():
            print("Sorry, the city you've entered is invalid.")
            continue
        else:
            break



    # TO DO: get user input for month (all, january, february, ... , june)
    #Invalid inputs handled in a While loop
    while True:
        month= input('Which month you want to see the data for?(all, january, february, ... , june): ')
        if month.lower() not in('all', 'january', 'february', 'march','april', 'may', 'june'):
            print("Sorry, the month you've entered is invalid.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Invalid inputs handled in a While loop
    while True:
        day= input('Which day you want to see the data for?(all, saturday, sunday, ... , friday): ')
        if day.lower() not in('all', 'saturday', 'sunday','monday', 'tuesday', 'wednesday','thursday','friday'):
            print("Sorry, the day you've entered is invalid.")
            continue
        else:
            break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month of travel is {}".format(calendar.month_name[common_month]))
    
    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    print("The most common day of the week is {}".format(common_dow))

    # TO DO: display the most common start hour
    df['Start hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start hour'].mode()[0]
    print("The most common start hour is {}".format(common_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #Concatenation of start and end of stattions into a new column
    df['Trip Direction']= 'From ' + df['Start Station'] +' '+'To '+df['End Station'] 
    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(common_start))
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination= df['Trip Direction'].mode()[0]
    print("The most common combination of start and end station trip is: {}".format(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = datetime.timedelta(seconds = int(df['Trip Duration'].sum()))
    print("Total travel time is {}".format(total_travel_time))

    # TO DO: display mean travel time
    average_trip_duration = datetime.timedelta(seconds = int(df['Trip Duration'].mean()))
    print("Average trip duration is {}".format(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count =df['User Type'].value_counts()
    print("Count for each type of user is:\n{}".format(user_types_count))
    while True:
        try:  
    # TO DO: Display counts of gender
     # TO DO: Display earliest, most recent, and most common year of birth
            gender_count =df['Gender'].value_counts()
            print("Gender count is:\n{}".format(gender_count))
            break
        except KeyError:
            print("Sorry, gender calculations are not available for the city you've chosen")
            break
            
   

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            print("Earliest year of birth among our users is: {}".format(int(df['Birth Year'].min())))
            print("While the most recent one is: {}".format(int(df['Birth Year'].max())))
            print("And the most common one is: {}".format(int(df['Birth Year'].mode()[0])))
            break
        except KeyError:
            print("Sorry, birth year statistic is not available for the city you've chosen!")
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon user's request"""
    #Get input from user whether they want to see the raw data or not
    display_raw_data= input("Do you want to see raw data?yes/no\n")
    i=0 #start location to display raw data
    j=5 #end location 
    if display_raw_data.lower() !='yes':
        print("Thank you, bye")
    else:
        print(df.iloc[i:j])
        i+=5
        j+=5
        
    while True:
        display_raw_data= input("Do you want to see 5 more lines?yes/no\n")
        if display_raw_data.lower()!='yes':
            break
        else:
            print(df.iloc[i:j])
            i+=5
            j+=5
            continue
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
