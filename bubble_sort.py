def bubble_sort(nums):
	nums = list(nums)
	if len(nums) == 1:
		return nums
	else:
		for _ in range(len(nums)-1):
			for i in range (len(nums)-1):
				if nums[i] > nums[i+1]:
					nums[i], nums[i+1] = nums[i+1], nums[i]
		return nums

numbers = input('>')
print(bubble_sort(numbers))