def selection_sort(list):
	sorted_list = []
	for i in range(len(list)):
		index_to_move = index_min(list)
		sorted_list.append(list.pop(index_to_move))
	return sorted_list

def index_min(list):
	min_index = 0
	for i in range(1, len(list)):
		if list[i] < list[min_index]:
			min_index = i
	return min_index

print(selection_sort([5,7,3,2,8,6]))
