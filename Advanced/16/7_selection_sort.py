def selection_sort(numbers):
	for index in range(len(numbers)):
		min_index = index

		for current_index in range(index + 1, len(numbers)):
			if numbers[current_index] < numbers[min_index]:
				min_index = current_index

		numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

	return numbers


array = [int(value) for value in input().split()]
print(*selection_sort(array))
