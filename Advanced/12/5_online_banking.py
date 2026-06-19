class MoneyNotEnoughError(Exception):
	pass


class PINCodeError(Exception):
	pass


class UnderageTransactionError(Exception):
	pass


class MoneyIsNegativeError(Exception):
	pass


pin_code, balance, age = input().split(", ")
balance = float(balance)
age = int(age)


while True:
	command = input()

	if command == "End":
		break

	command_parts = command.split("#")
	action = command_parts[0]

	if action == "Send Money":
		money_to_send = float(command_parts[1])
		current_pin_code = command_parts[2]

		if money_to_send > balance:
			raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

		if current_pin_code != pin_code:
			raise PINCodeError("Invalid PIN code")

		if age < 18:
			raise UnderageTransactionError(
				"You must be 18 years or older to perform online transactions"
			)

		balance -= money_to_send
		print(f"Successfully sent {money_to_send:.2f} money to a friend")
		print(f"There is {balance:.2f} money left in the bank account")

	elif action == "Receive Money":
		money_to_receive = float(command_parts[1])

		if money_to_receive < 0:
			raise MoneyIsNegativeError(
				"The amount of money cannot be a negative number"
			)

		balance += money_to_receive / 2
		print(f"{money_to_receive / 2:.2f} money went straight into the bank account")
