import unittest
import ideas

class TestIdeaGenerator(unittest.TestCase):

	def setUp(self):
		self.x = ideas.IdeaGenerator(1)

	def test_parameter(self):
		self.assertEqual(self.x.numberOfIdeas, 1)

	def test_output(self):
		self.assertEqual(self.x.generate_ideas(), "idea")

	def test_file_read(self):
		self.assertEqual("", "")

if __name__ == "__main__":
	global x
	unittest.main()
