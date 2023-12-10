# AGE CALCULATOR PROJECT

import datetime
from datetime import datetime
import sys
monthsWithDaysTest = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

print('')
print('\n ******** AGE CALCULAOTR ********\n')
print('You are going to enter your date of birth in order....')
print('')

while True:
    try:
        birthYear = int(input('enter your birth-year(YYYY)?....'))
        birthMonth = int(input('enter your birth-month(MM)?....'))
        birthDay = int(input('enter your birth-day(DD)?....'))

        if (birthYear == '' or birthMonth == "" or birthDay == ''):
            print('Invalid Input..read instructions and try again....')
            print('')
            continue
        elif birthMonth > 12 or birthDay > 31:
            print('Invalid Input..read instructions and try again....')
            print('')
            continue
        else:
            ageInyears = datetime.now().year - birthYear
            ageInMonth = datetime.now().month - birthMonth
            ageInDays = datetime.now().day - birthDay


            # cases where teh birthday hanst appeared yet
            if (datetime.now().month < birthMonth or (datetime.now().month == birthMonth and datetime.now().day < birthDay)):
                ageInyears -=1
                ageInMonth += 12

            if datetime.now().day < birthDay:
                ageInMonth -= 1
                lastmonth = monthsWithDaysTest[(datetime.now().month + 11) % 12]
                ageInDays += lastmonth

            if ageInDays == 1:
                word =  'day'
            else:
                word = 'days'

            print(f"you are {ageInyears} years , {ageInMonth} months and {ageInDays} {word}")

            user_option = input('do you want to try again(Y for YES | N for NO)...').lower()
            if user_option == 'y':
                continue
            elif user_option == 'n':
                print('See ya.....')
                sys.exit(0)
            else:
                print('invalid Option....EXIITNG')
                sys.exit(0)
    except Exception as e:
        print(f'Invalid Input.....Error : {e}')






