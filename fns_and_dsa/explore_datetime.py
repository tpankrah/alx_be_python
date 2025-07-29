from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current_date

#display_current_datetime()

print(f'Current date and time: {display_current_datetime()}')


number_of_days = int(input("Enter the number of days to add to the current date:"))

//future_date =""

def calculate_future_date(number_of_days):
    return (datetime.datetime.now() + datetime.timedelta(days=number_of_days))

future_date =calculate_future_date(number_of_days)

print(f' Future date: {future_date.strftime('%Y-%m-%d')}')