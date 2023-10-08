#interest rate calculator
#option to calculate interets payments or compound interest
import time


def interets_calculator():
    is_valid = True
    print('\nHello Welcome')
    print('')
    print('******    Customer Area    *******')
    user_name = input('\nEnter your name....')
    print('\n')
    while is_valid:
        print(f'{user_name.capitalize()}, which interest calculator would you like..\nS for Simple Interest\nC for Compound Interest')
        user_choice = input('enter your choice..S or C..').lower()
        if user_choice == 's':
            return simple_interest()
        elif user_choice == 'c':
            return compound_interest()
        else:
            print(f"{user_name}, seriously, read intrustions and try again..\n")
            is_valid = True
        
    

def currency():
    print('\n')
    print('Before we start\nIs your money in dollars or pounds?')
    print('Choose D for dollars and P for Pound Sterling..')
    currency = input('Is your money in dollars or pounds?..').lower()
    if currency == 'd':
        return '$'
    elif currency == 'p':
        return '£'

def simple_interest():
    user_currency = currency()
    print('\n')
    print('***********   OPERATION  ***********')
    print('\n')
    intial_Amount = int(input('Enter your initial amount of deposit..'))
    print('\nYou are going to enter your interest rate given to you by commercial bank\nPLEASE TYPE THIS IN PERCENTAGE WITHOUT ADDING THE PERCENTAGE SIGN(%)')
    time.sleep(4)
    print('\n')
    rate = input('enter your interest rate..')
    integer_convert_rate = int(rate) / 100
    year = int(input('enter the amount of years you would like to keep your money for...'))
    interest = (intial_Amount * integer_convert_rate * year)
    end_balance = intial_Amount + interest
    time.sleep(1)
    print('')
    print(f'Your total interest would amount to {user_currency}{interest:.2f} in {year} years')
    print(f'Your End Balance would amount to {end_balance:.2f} in {year} years')

def compound_years():
    is_valid = True
    while is_valid:
        print('\n')
        print('You are going to be asked how often your interest would be compounded per year..\nYou ready....👍')
        time.sleep(1)
        print('\n')
        print('Enter \nF for Whole annual year..\nH for Half a year..\nQ for Quarterly\nM for Monthly\nD for Daily..')
        time.sleep(1)
        print('\n')
        
        user_compound = input('enter how often, your compound-periods is going to be...').lower()
        if user_compound == "f":
            return 1
        elif user_compound == 'h':
            return 2
        elif user_compound == 'm':
            return 12
        elif user_compound == 'd':
            return 365
        elif user_compound == 'q':
            return 4
        else:
            print('your option was invalid, try again..')
            is_valid = True



def compound_interest():
    user_currency = currency()
    print('***********   OPERATION  ***********')
    print('\n')
    intial_Amount = int(input('Enter your initial amount of deposit..'))
    print('\nYou are going to enter your interest rate given to you by commercial bank\nPLEASE TYPE THIS IN PERCENTAGE WITHOUT ADDING THE PERCENTAGE SIGN(%)')
    time.sleep(4)
    print('\n')
    rate = input('enter your interest rate..')
    integer_convert_rate = int(rate) / 100
    year = int(input('enter the amount of years you would like to keep your money for...'))

    user_compound_periods = compound_years()

    compound_interest = intial_Amount * (1 + (integer_convert_rate / user_compound_periods)) ** (user_compound_periods * year) - intial_Amount
    full_amount = intial_Amount + compound_interest
    print(f'Your total compound interest would amount to {user_currency}{compound_interest:.2f} in {year} years')
    print(f'Your End Balance would amount to {full_amount:.2f} in {year} years')
    


