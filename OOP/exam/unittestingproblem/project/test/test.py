import unittest

from project.legendary_item import LegendaryItem


class LegendaryItemTests(unittest.TestCase):
	def setUp(self):
		self.item = LegendaryItem("Excalibur-1", 50, 80, 100)

	def test_constructor_assigns_all_attributes(self):
		self.assertEqual("Excalibur-1", self.item.identifier)
		self.assertEqual(50, self.item.power)
		self.assertEqual(80, self.item.durability)
		self.assertEqual(100, self.item.price)

	def test_identifier_setter_accepts_letters_digits_and_hyphens(self):
		self.item.identifier = "Item-42"

		self.assertEqual("Item-42", self.item.identifier)

	def test_identifier_setter_raises_for_invalid_characters(self):
		with self.assertRaisesRegex(
			ValueError, "Identifier can only contain letters, digits, or hyphens!"
		):
			self.item.identifier = "bad item!"

	def test_identifier_setter_raises_when_shorter_than_four_characters(self):
		with self.assertRaisesRegex(
			ValueError, "Identifier must be at least 4 characters long!"
		):
			self.item.identifier = "abc"

	def test_power_setter_accepts_zero(self):
		self.item.power = 0

		self.assertEqual(0, self.item.power)

	def test_power_setter_raises_for_negative_value(self):
		with self.assertRaisesRegex(
			ValueError, "Power must be a non-negative integer!"
		):
			self.item.power = -1

	def test_durability_setter_accepts_boundary_values(self):
		self.item.durability = 1
		self.assertEqual(1, self.item.durability)

		self.item.durability = 100
		self.assertEqual(100, self.item.durability)

	def test_durability_setter_raises_outside_allowed_range(self):
		for durability in (0, 101):
			with self.subTest(durability=durability):
				with self.assertRaisesRegex(
					ValueError, "Durability must be between 1 and 100 inclusive!"
				):
					self.item.durability = durability

	def test_price_setter_accepts_nonzero_multiple_of_ten(self):
		self.item.price = -20

		self.assertEqual(-20, self.item.price)

	def test_price_setter_raises_for_zero_or_non_multiple_of_ten(self):
		for price in (0, 15):
			with self.subTest(price=price):
				with self.assertRaisesRegex(
					ValueError, "Price must be a multiple of 10 and not 0!"
				):
					self.item.price = price

	def test_is_precious_returns_true_for_power_of_fifty_or_more(self):
		self.assertTrue(self.item.is_precious)

	def test_is_precious_returns_false_for_power_below_fifty(self):
		self.item.power = 49

		self.assertFalse(self.item.is_precious)

	def test_enhance_doubles_power_increases_price_and_durability(self):
		self.item.enhance()

		self.assertEqual(100, self.item.power)
		self.assertEqual(110, self.item.price)
		self.assertEqual(90, self.item.durability)

	def test_enhance_caps_durability_at_one_hundred(self):
		self.item.durability = 95

		self.item.enhance()

		self.assertEqual(100, self.item.durability)

	def test_evaluate_returns_eligible_message_when_conditions_are_met(self):
		result = self.item.evaluate(80)

		self.assertEqual("Excalibur-1 is eligible.", result)

	def test_evaluate_returns_not_eligible_when_durability_is_insufficient(self):
		result = self.item.evaluate(81)

		self.assertEqual("Item not eligible.", result)

	def test_evaluate_returns_not_eligible_when_item_is_not_precious(self):
		self.item.power = 49

		result = self.item.evaluate(80)

		self.assertEqual("Item not eligible.", result)


if __name__ == "__main__":
	unittest.main()


