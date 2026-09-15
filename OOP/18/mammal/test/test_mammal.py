import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
	def setUp(self):
		self.mammal = Mammal("Bobby", "dog", "woof")

	def test_initialization_sets_attributes(self):
		self.assertEqual("Bobby", self.mammal.name)
		self.assertEqual("dog", self.mammal.type)
		self.assertEqual("woof", self.mammal.sound)

	def test_make_sound_returns_expected_message(self):
		self.assertEqual("Bobby makes woof", self.mammal.make_sound())

	def test_get_kingdom_returns_animals(self):
		self.assertEqual("animals", self.mammal.get_kingdom())

	def test_info_returns_expected_message(self):
		self.assertEqual("Bobby is of type dog", self.mammal.info())


if __name__ == "__main__":
	unittest.main()
