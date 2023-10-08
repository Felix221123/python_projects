#basic calculator in python
import sys
def addtion():
    a = int(input('enter your first number..'))
    b = int(input('enter your second nummber..'))
    sum = a + b
    print(f'the sum of {a} and {b} is {sum}')
    
    
def subtraction():
    a = int(input('enter your first number..'))
    b = int(input('enter your second nummber..'))
    sub = a - b
    print(f'the subtraction of {a} and {b} is {sub}')


def multiply():
    a = int(input('enter your first number..'))
    b = int(input('enter your second nummber..'))
    mul = a * b
    print(f'the multiplication of {a} and {b} is {mul}')
    
def division():
    is_valid = True
    while is_valid:
        a = int(input('enter your first number as the numerator..'))
        b = int(input('enter your second nummber as the demominator..'))
        if not(a or b ) == 0:
            div = (a / b)
            print(f'the result of the division was {div:.2f}')
            is_valid = False
        elif (a or b) == 0:
            sys.exit('we can\'t do division by zero')  
        else:
            print('your numbers are just not valid')
            continue
            

is_valid = True


while is_valid == True:
    print('\nwhat operation would you like to perform...\nA for Addition\nS for Subtraction\nM for Multiplicaiton\nD for Division\nX for Exit')
    user_choice = input('enter A or S or M or D or X for opertion..').lower()
    print('\n******** operation *********')
    if user_choice == 'a':
        addtion()
        break
    elif user_choice == 's':
        subtraction()
        break
    elif user_choice == 'm':
        multiply()
        break
    elif user_choice == 'd':
        division()
        break
    elif user_choice == 'x':
        sys.exit('Thanks for playing...🙃')
    else:
        print('Your option is invalid, try again..')
        is_valid = True
    