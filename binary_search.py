#binary search algorithm
#This algorithm works when the list is sorted else
#it won't be efficient as it seems to be
#It works by halving the list and if the target is greater than current number then
#it cuts the left hand side and starts lookgin at the right hand side instead
#it keeps repeating this until the target is found

def binary_search(list,target):
    first = 0  #first position in the list
    last = len(list) - 1     #last position of item in list

    while last >= first:
        midpoint = (first + last) // 2        #use the floor division to round the mid point down

        if list[midpoint] == target:           #checks if the value at the midpoint is equal to the target
            return midpoint                     #then it returns the index positon of the target
        elif target > list[midpoint]:         #checks if the target is greater the value in the midpoint 
            first = midpoint + 1               #then we add one to the midpoint, which will indicate our starting position from the list
        else:                                #else if the 
            last = midpoint - 1

    return None

#function to verify if the 
def verify(index):
    if index is not None:
        print('Target was found at index: ', index)
    else:
        print('Target not found in list')



random_numbers = [12, 45, 67, 23, 56, 78, 34, 89, 10, 42]
sorted_list = sorted(random_numbers)

target = 56

results = binary_search(sorted_list, target)
print(sorted_list)
verify(results)
