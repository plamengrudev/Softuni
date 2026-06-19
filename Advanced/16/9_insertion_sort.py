def insertion_sort(numbers):
	for index in range(1, len(numbers)):
		current_value = numbers[index]
		previous_index = index - 1

		while previous_index >= 0 and numbers[previous_index] > current_value:
			numbers[previous_index + 1] = numbers[previous_index]
			previous_index -= 1

		numbers[previous_index + 1] = current_value

	return numbers


numbers = [int(value) for value in input().split()]
sorted_numbers = insertion_sort(numbers)

print(*sorted_numbers)
