import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
	def setUp(self):
		self.hero = Hero("Peter", 2, 100, 10)
		self.enemy = Hero("John", 1, 100, 10)

	def test_initialization_sets_attributes(self):
		self.assertEqual("Peter", self.hero.username)
		self.assertEqual(2, self.hero.level)
		self.assertEqual(100, self.hero.health)
		self.assertEqual(10, self.hero.damage)

	def test_battle_with_self_raises_exception(self):
		with self.assertRaises(Exception) as context:
			self.hero.battle(Hero("Peter", 1, 100, 10))

		self.assertEqual("You cannot fight yourself", str(context.exception))

	def test_battle_when_hero_needs_rest_raises_value_error(self):
		self.hero.health = 0

		with self.assertRaises(ValueError) as context:
			self.hero.battle(self.enemy)

		self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

	def test_battle_when_enemy_needs_rest_raises_value_error(self):
		self.enemy.health = 0

		with self.assertRaises(ValueError) as context:
			self.hero.battle(self.enemy)

		self.assertEqual("You cannot fight John. He needs to rest", str(context.exception))

	def test_battle_returns_draw_when_both_heroes_die(self):
		self.hero.health = 10
		self.enemy.health = 20

		self.assertEqual("Draw", self.hero.battle(self.enemy))
		self.assertLessEqual(self.hero.health, 0)
		self.assertLessEqual(self.enemy.health, 0)

	def test_battle_returns_win_and_increases_winner_stats(self):
		self.enemy.health = 10

		self.assertEqual("You win", self.hero.battle(self.enemy))
		self.assertEqual(3, self.hero.level)
		self.assertEqual(95, self.hero.health)
		self.assertEqual(15, self.hero.damage)

	def test_battle_returns_loss_and_increases_enemy_stats(self):
		self.hero.health = 10

		self.assertEqual("You lose", self.hero.battle(self.enemy))
		self.assertEqual(2, self.enemy.level)
		self.assertEqual(85, self.enemy.health)
		self.assertEqual(15, self.enemy.damage)

	def test_string_representation(self):
		expected = "Hero Peter: 2 lvl\nHealth: 100\nDamage: 10\n"
		self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
	unittest.main()
