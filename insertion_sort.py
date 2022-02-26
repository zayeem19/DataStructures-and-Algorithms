def insertion_sort(nums):
	nums = list(nums)
	for i in range(len(nums)):
		current = nums.pop(i)
		j = i-1
		while j >= 0 and nums[j] > current:
			j -= 1
		nums.insert(j+1, current)
	return nums

numbers = input('>')
print(insertion_sort(numbers))
