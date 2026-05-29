def spread_bunnies(matrix, rows, cols):
	current_bunnies = []

	for row in range(rows):
		for col in range(cols):
			if matrix[row][col] == "B":
				current_bunnies.append((row, col))

	for row, col in current_bunnies:
		for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			next_row = row + delta_row
			next_col = col + delta_col

			if 0 <= next_row < rows and 0 <= next_col < cols:
				matrix[next_row][next_col] = "B"


def main():
	rows, cols = map(int, input().split())
	lair = [list(input()) for _ in range(rows)]
	commands = input()

	player_row = 0
	player_col = 0

	for row in range(rows):
		for col in range(cols):
			if lair[row][col] == "P":
				player_row, player_col = row, col
				break
		else:
			continue
		break

	directions = {
		"U": lambda row, col: (row - 1, col),
		"D": lambda row, col: (row + 1, col),
		"L": lambda row, col: (row, col - 1),
		"R": lambda row, col: (row, col + 1),
	}

	outcome = ""
	final_row = player_row
	final_col = player_col

	for command in commands:
		next_row, next_col = directions[command](player_row, player_col)

		lair[player_row][player_col] = "."

		if not (0 <= next_row < rows and 0 <= next_col < cols):
			outcome = "won"
			final_row = player_row
			final_col = player_col
		elif lair[next_row][next_col] == "B":
			player_row = next_row
			player_col = next_col
			outcome = "dead"
			final_row = player_row
			final_col = player_col
		else:
			player_row = next_row
			player_col = next_col
			lair[player_row][player_col] = "P"

		spread_bunnies(lair, rows, cols)

		if outcome == "won":
			break

		if lair[player_row][player_col] == "B":
			outcome = "dead"
			final_row = player_row
			final_col = player_col
			break

	for row in lair:
		print("".join(row))

	print(f"{outcome}: {final_row} {final_col}")


if __name__ == "__main__":
	main()
