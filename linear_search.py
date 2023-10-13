#linear search algorithm
#Loops through a lsit until the target is found , else it returns 
#none

def linear_search(list , target):
    '''
    returns the target if found else returns none
    '''
    for i in range(0 , len(list)):
        #compare the numbers in the list parameter to the target
        if list[i] == target:
            #if found, return the index
            return i
    return None


#function to verify if the 
def verify(index):
    if index is not None:
        print('Target was found at index: ', index)
    else:
        print('Target not found in list')

numbers = [23,43,2,5,83,73,0,4]
mytarget = 83

result = linear_search(numbers , mytarget)
verify(result)