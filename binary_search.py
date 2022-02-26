def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None


def verify(index):
    if index is not None:
        print('Number found at index', index)
    else:
        print('Number not found')


numbers = input('Enter the numbers: ')
value = input('Enter the target value: ')
result = binary_search(numbers, value)
verify(result)
