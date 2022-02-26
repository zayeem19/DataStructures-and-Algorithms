import random

def is_sorted(list):
	for i in range(len(list)-1):
		if list[i] > list[i+1]:
			return False
	return True

def bogo_sort(list):
	while not is_sorted(list):
		random.shuffle(list)
	return list


numbers = input('>')
result = bogo_sort(numbers)
print(result)