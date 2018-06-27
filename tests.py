# 06/25/2018
#
# Tests for IdeaGenerator
# By James Kuny - james.kuny@yahoo.com

import unittest
import ideas

class TestIdeaGenerator(unittest.TestCase):

	def setUp(self):
		self.x = ideas.IdeaGenerator(3)
		
	def test_initialized_array(self):
		self.assertEqual(len(self.x.results), 0)

	def test_parameter(self):
		self.assertEqual(self.x.numberOfIdeas, 3)

	def test_output(self):
		self.x.generate_ideas()
		self.assertTrue(len(self.x.results) > 0)
		
	def test_file_found(self):
		self.assertIsNotNone(self.x.is_file_found())
		
	def test_file_read(self):
		self.assertIsNotNone(self.x.retrieve_noun())
		
if __name__ == "__main__":
	global x
	unittest.main()
