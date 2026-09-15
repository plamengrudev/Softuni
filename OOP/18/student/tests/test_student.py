import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
	def test_initialization_with_default_courses(self):
		student = Student("Peter")

		self.assertEqual("Peter", student.name)
		self.assertEqual({}, student.courses)

	def test_initialization_with_courses(self):
		courses = {"Python": ["variables"]}
		student = Student("Peter", courses)

		self.assertEqual(courses, student.courses)

	def test_enroll_existing_course_appends_notes(self):
		student = Student("Peter", {"Python": ["variables"]})

		result = student.enroll("Python", ["functions"])

		self.assertEqual("Course already added. Notes have been updated.", result)
		self.assertEqual(["variables", "functions"], student.courses["Python"])

	def test_enroll_new_course_with_default_option_adds_notes(self):
		student = Student("Peter")

		result = student.enroll("Python", ["variables"])

		self.assertEqual("Course and course notes have been added.", result)
		self.assertEqual(["variables"], student.courses["Python"])

	def test_enroll_new_course_with_yes_option_adds_notes(self):
		student = Student("Peter")

		result = student.enroll("Python", ["variables"], "Y")

		self.assertEqual("Course and course notes have been added.", result)
		self.assertEqual(["variables"], student.courses["Python"])

	def test_enroll_new_course_without_notes(self):
		student = Student("Peter")

		result = student.enroll("Python", ["variables"], "N")

		self.assertEqual("Course has been added.", result)
		self.assertEqual([], student.courses["Python"])

	def test_add_notes_to_existing_course(self):
		student = Student("Peter", {"Python": []})

		result = student.add_notes("Python", "variables")

		self.assertEqual("Notes have been updated", result)
		self.assertEqual(["variables"], student.courses["Python"])

	def test_add_notes_to_missing_course_raises_exception(self):
		student = Student("Peter")

		with self.assertRaises(Exception) as context:
			student.add_notes("Python", "variables")

		self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

	def test_leave_existing_course_removes_it(self):
		student = Student("Peter", {"Python": ["variables"]})

		result = student.leave_course("Python")

		self.assertEqual("Course has been removed", result)
		self.assertNotIn("Python", student.courses)

	def test_leave_missing_course_raises_exception(self):
		student = Student("Peter")

		with self.assertRaises(Exception) as context:
			student.leave_course("Python")

		self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == "__main__":
	unittest.main()
