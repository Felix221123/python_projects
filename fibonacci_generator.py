#this is a project that features the generation of a fibonacci sequence
#based on the users request

def fibonacci_generator():
    start_value = 0 
    print(' ')
    num2 = 1
    next_number = start_value
    count = 1
    user_end_value = int(input('how many sequence would you like your fibonacci?.... '))
    
    while user_end_value >= count:
        print(next_number , end=' ')
        count += 1
        start_value , num2 = num2 , next_number
        next_number = start_value + num2
    print()
        
fibonacci_generator()
