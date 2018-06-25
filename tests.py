import unittest
import ideas

class TestIdeaGenerator(unittest.TestCase):
	
	def test_parameter(self):
		x = ideas.IdeaGenerator(3)
		self.assertEqual(x.numberOfIdeas, 3)

	def test_file_read(self):
		x = ideas.IdeaGenerator(3)
		self.assertEqual(x., "test")

if __name__ == "__main__":
    unittest.main()