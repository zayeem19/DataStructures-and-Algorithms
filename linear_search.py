def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
            
def verify(index):
    if index is not None:
        print('Number found at', index)
    else:
        print('Number not found on the list')

numbers = input('>')
value= input('>')
result = linear_search(numbers, value)
verify(result)


