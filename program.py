import datetime

def get_user_date_input():
    year = int(input('Enter your birth year: '))
    month = int(input('Enter your birth month: '))
    day = int(input('Enter yout birth day: '))

    birthday = datetime.date(year, month, day)
    return birthday

def main():
    user_birthday = get_user_date_input()
    print(user_birthday)

main()