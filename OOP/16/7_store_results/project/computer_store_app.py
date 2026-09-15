from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
	COMPUTER_TYPES = {
		"Desktop Computer": DesktopComputer,
		"Laptop": Laptop,
	}

	def __init__(self):
		self.warehouse = []
		self.profits = 0

	def build_computer(
		self,
		type_computer: str,
		manufacturer: str,
		model: str,
		processor: str,
		ram: int,
	):
		computer_class = self.COMPUTER_TYPES.get(type_computer)
		if computer_class is None:
			raise ValueError(f"{type_computer} is not a valid type computer!")

		computer = computer_class(manufacturer, model)
		result = computer.configure_computer(processor, ram)
		self.warehouse.append(computer)
		return result

	def sell_computer(
		self, client_budget: int, wanted_processor: str, wanted_ram: int
	):
		for computer in self.warehouse:
			if (
				computer.price <= client_budget
				and computer.processor == wanted_processor
				and computer.ram >= wanted_ram
			):
				self.warehouse.remove(computer)
				self.profits += client_budget - computer.price
				return f"{computer} sold for {client_budget}$."

		raise Exception("Sorry, we don't have a computer for you.")
