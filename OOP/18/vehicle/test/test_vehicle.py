import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
	def setUp(self):
		self.vehicle = Vehicle(100, 120)

	def test_initialization_sets_default_values(self):
		self.assertEqual(100, self.vehicle.fuel)
		self.assertEqual(100, self.vehicle.capacity)
		self.assertEqual(120, self.vehicle.horse_power)
		self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

	def test_drive_decreases_fuel_by_required_amount(self):
		self.vehicle.drive(20)
		self.assertEqual(75, self.vehicle.fuel)

	def test_drive_with_insufficient_fuel_raises_exception(self):
		self.vehicle.fuel = 10

		with self.assertRaises(Exception) as context:
			self.vehicle.drive(10)

		self.assertEqual("Not enough fuel", str(context.exception))

	def test_refuel_increases_fuel(self):
		self.vehicle.fuel = 50
		self.vehicle.refuel(25)
		self.assertEqual(75, self.vehicle.fuel)

	def test_refuel_above_capacity_raises_exception(self):
		with self.assertRaises(Exception) as context:
			self.vehicle.refuel(1)

		self.assertEqual("Too much fuel", str(context.exception))

	def test_string_representation(self):
		expected = "The vehicle has 120 horse power with 100 fuel left and 1.25 fuel consumption"
		self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
	unittest.main()
