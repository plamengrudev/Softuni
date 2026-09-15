from project.computer_types.computer import Computer


class Laptop(Computer):
	AVAILABLE_PROCESSORS = {
		"AMD Ryzen 9 5950X": 900,
		"Intel Core i9-11900H": 1050,
		"Apple M1 Pro": 1200,
	}
	MAX_RAM = 64

	def configure_computer(self, processor: str, ram: int):
		if processor not in self.AVAILABLE_PROCESSORS:
			raise ValueError(
				f"{processor} is not compatible with laptop "
				f"{self.manufacturer} {self.model}!"
			)
		if not self._is_valid_ram(ram):
			raise ValueError(
				f"{ram}GB RAM is not compatible with laptop "
				f"{self.manufacturer} {self.model}!"
			)

		self.processor = processor
		self.ram = ram
		self.price = self.AVAILABLE_PROCESSORS[processor] + (ram.bit_length() - 1) * 100
		return (
			f"Created {self.manufacturer} {self.model} with {self.processor} "
			f"and {self.ram}GB RAM for {self.price}$."
		)

	def _is_valid_ram(self, ram: int):
		return isinstance(ram, int) and 2 <= ram <= self.MAX_RAM and ram & (ram - 1) == 0
