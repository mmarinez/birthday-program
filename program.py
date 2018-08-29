import datetime

def get_year_input():

    while True:
        try:
            year = int(input('Enter your birth year: '))
            break
        except:
            print('Invalid year')

    return year

def get_month_input():

    while True:
        try:
            month = int(input('Enter your birth month: '))
            break
        except:
            print('Invalid month')

    return month

def get_day_input():

    while True:
        try:
            day = int(input('Enter your birth day: '))
            break
        except:
            print('Invalid day')

    return day

def get_user_date_input():
   
    birthday = datetime.date(get_year_input(), get_month_input(), get_day_input())
    return birthday

def difference_between_dates(birthday,currentday):

    this_year_birthday = datetime.date(currentday.year, birthday.month, birthday.day)

    days_left = this_year_birthday - currentday
    return days_left.days

def print_birthday_info(days):
    
    if days < 0:
        print('Your birthday was {} days ago this year'.format(-days))
    elif days > 0:
        print('Your birthday will be in {} days'.format(days))
    else:
        print('Today is your birthday!!!')

def main():
    user_birthday = get_user_date_input()
    today = datetime.date.today()
    birthday = difference_between_dates(user_birthday, today)
    print_birthday_info(birthday)

main()