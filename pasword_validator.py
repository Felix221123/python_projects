#password generator
#the password generator should only have at teh start a capitalized
#letter and then small letters afterwards and then a special character
#create an authentication first and then do a generator
import string
import secrets
import random
import re

mylower_char = string.ascii_lowercase
mycap_char = string.ascii_uppercase

#compare password setters
my_password_regex = '^[A-Z]+[a-z]*[!@#$%^&*()-+?_=,<>/]+[0-9]+$'

is_valid = True
print('')

while is_valid:
    user_input = input('enter a new password..')
    if(re.match(my_password_regex, user_input)):
        print('new password has been set successfully')
        is_valid = False
    else:
        print('Your password must starts with at least one uppercase and some lowercases..\nYour password must have some special characters in them..\nYour password must end with some digits..')




