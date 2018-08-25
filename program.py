import datetime

def get_user_date_input():

    while True:
        try:
            year = int(input('Enter your birth year: '))
            month = int(input('Enter your birth month: '))
            day = int(input('Enter yout birth day: '))
            break
        except:
            print('Invalid input')

    birthday = datetime.date(year, month, day)
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