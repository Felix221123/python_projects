#this is another way of implementing binary search in a recursive form


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if target > list[midpoint]:
                return recursive_binary_search(list[midpoint +1 :] , target)
            else:
                return recursive_binary_search(list[:midpoint] , target)
            

def verify(result):
    if result == True:
        print(f'the target was found...  : ) : {result}')
    else:
        print(f'the target was not found... : ( : {result}')

random_numbers = [12, 45, 67, 23, 56, 78, 34, 89, 10, 42]
sorted_list = sorted(random_numbers)

first_target = 56
second_target = 80

result = recursive_binary_search(sorted_list, first_target)
verify(result)

result = recursive_binary_search(sorted_list, second_target)
verify(result)