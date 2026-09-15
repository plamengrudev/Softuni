import unittest

from car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Corolla", 6.5, 50)

    def test_constructor_initializes_all_attributes(self):
        self.assertEqual("Toyota", self.car.make)
        self.assertEqual("Corolla", self.car.model)
        self.assertEqual(6.5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_raises_for_empty_value(self):
        with self.assertRaisesRegex(Exception, "Make cannot be null or empty!"):
            self.car.make = ""

    def test_model_raises_for_empty_value(self):
        with self.assertRaisesRegex(Exception, "Model cannot be null or empty!"):
            self.car.model = ""

    def test_fuel_consumption_raises_for_zero_or_negative_value(self):
        for invalid_value in (0, -1):
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaisesRegex(
                    Exception, "Fuel consumption cannot be zero or negative!"
                ):
                    self.car.fuel_consumption = invalid_value

    def test_fuel_capacity_raises_for_zero_or_negative_value(self):
        for invalid_value in (0, -1):
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaisesRegex(
                    Exception, "Fuel capacity cannot be zero or negative!"
                ):
                    self.car.fuel_capacity = invalid_value

    def test_fuel_amount_raises_for_negative_value(self):
        with self.assertRaisesRegex(Exception, "Fuel amount cannot be negative!"):
            self.car.fuel_amount = -1

    def test_refuel_raises_for_zero_or_negative_fuel(self):
        for invalid_value in (0, -1):
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaisesRegex(
                    Exception, "Fuel amount cannot be zero or negative!"
                ):
                    self.car.refuel(invalid_value)

    def test_refuel_increases_fuel_amount(self):
        self.car.refuel(20)

        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_caps_fuel_at_capacity(self):
        self.car.refuel(60)

        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_raises_when_fuel_is_insufficient(self):
        with self.assertRaisesRegex(Exception, "You don't have enough fuel to drive!"):
            self.car.drive(100)

    def test_drive_decreases_fuel_by_required_amount(self):
        self.car.refuel(20)

        self.car.drive(200)

        self.assertEqual(7, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()