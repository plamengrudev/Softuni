import re


def choose_coins(coins, target_sum):
	remaining_sum = target_sum
	taken_coins = {}

	for coin in sorted(set(coins), reverse=True):
		count = remaining_sum // coin

		if count > 0:
			taken_coins[coin] = count
			remaining_sum -= coin * count

		if remaining_sum == 0:
			break

	if remaining_sum != 0:
		return None

	return taken_coins


coins = [int(value) for value in re.findall(r"\d+", input())]
target_sum = int(re.findall(r"\d+", input())[0])

result = choose_coins(coins, target_sum)

if result is None:
	print("Error")
else:
	print(f"Number of coins to take: {sum(result.values())}")
	for coin, count in result.items():
		print(f"{count} coin(s) with value {coin}")
