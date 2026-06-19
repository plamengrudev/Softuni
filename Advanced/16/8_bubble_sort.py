def bubble_sort(numbers):
	length = len(numbers)

	for end_index in range(length):
		swapped = False

		for current_index in range(0, length - 1 - end_index):
			next_index = current_index + 1

			if numbers[current_index] > numbers[next_index]:
				numbers[current_index], numbers[next_index] = numbers[next_index], numbers[current_index]
				swapped = True

		if not swapped:
			break


array = [int(value) for value in input().split()]
bubble_sort(array)
print(*array)
