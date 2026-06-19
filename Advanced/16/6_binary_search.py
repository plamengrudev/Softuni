def binary_search(numbers, target):
	left = 0
	right = len(numbers) - 1

	while left <= right:
		middle = (left + right) // 2
		current_number = numbers[middle]

		if current_number == target:
			return middle

		if current_number < target:
			left = middle + 1
		else:
			right = middle - 1

	return -1


numbers = [int(value) for value in input().split()]
target = int(input())

print(binary_search(numbers, target))
