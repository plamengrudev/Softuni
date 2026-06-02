def move(position, direction):
	row, col = position

	if direction == "up":
		return row - 1, col
	if direction == "down":
		return row + 1, col
	if direction == "left":
		return row, col - 1
	return row, col + 1


def in_bounds(row, col, size):
	return 0 <= row < size and 0 <= col < size


def give_present(matrix, row, col, presents):
	if presents == 0:
		return presents

	if matrix[row][col] in {"V", "X"}:
		presents -= 1
		matrix[row][col] = "-"

	return presents


def main():
	presents = int(input())
	size = int(input())

	neighborhood = []
	santa_position = (0, 0)
	total_nice_kids = 0

	for row in range(size):
		current_row = input().split()
		neighborhood.append(current_row)

		for col in range(size):
			if current_row[col] == "S":
				santa_position = (row, col)
			elif current_row[col] == "V":
				total_nice_kids += 1

	happy_nice_kids = 0

	while presents > 0:
		command = input()
		if command == "Christmas morning":
			break

		current_row, current_col = santa_position
		neighborhood[current_row][current_col] = "-"

		next_row, next_col = move(santa_position, command)
		current_cell = neighborhood[next_row][next_col]

		if current_cell == "V":
			presents -= 1
			happy_nice_kids += 1
			neighborhood[next_row][next_col] = "-"
		elif current_cell == "C":
			neighborhood[next_row][next_col] = "-"

			for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
				adjacent_row = next_row + delta_row
				adjacent_col = next_col + delta_col

				if not in_bounds(adjacent_row, adjacent_col, size):
					continue

				adjacent_cell = neighborhood[adjacent_row][adjacent_col]

				if adjacent_cell == "V" and presents > 0:
					happy_nice_kids += 1

				presents = give_present(
					neighborhood,
					adjacent_row,
					adjacent_col,
					presents,
				)

		santa_position = (next_row, next_col)
		neighborhood[next_row][next_col] = "S"

		if presents == 0:
			break

	remaining_nice_kids = total_nice_kids - happy_nice_kids

	if presents == 0 and remaining_nice_kids > 0:
		print("Santa ran out of presents!")

	for row in neighborhood:
		print(*row)

	if remaining_nice_kids == 0:
		print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
	else:
		print(f"No presents for {remaining_nice_kids} nice kid/s.")


if __name__ == "__main__":
	main()
