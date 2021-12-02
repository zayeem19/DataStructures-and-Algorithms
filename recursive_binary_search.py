def recursive_binary_search(list, target):
    if len(list)==0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[ : midpoint], target)

numbers = input('>')
value = input('>')
result = recursive_binary_search(numbers, value)

def verify(result):
    print('Target found at index: ', result)

verify(result)