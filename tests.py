# 06/25/2018
#
# Tests for IdeaGenerator
# By James Kuny - james.kuny@yahoo.com

import unittest
import ideas

class TestIdeaGenerator(unittest.TestCase):

	def setUp(self):
		self.test_generator = ideas.IdeaGenerator(3)
		
	def test_initialized_array(self):
		self.assertEqual(len(self.test_generator.results), 0)

	def test_parameter(self):
		self.assertEqual(self.test_generator.number_of_ideas, 3)

	def test_output(self):
		self.test_generator.generate_ideas()
		self.assertTrue(len(self.test_generator.results) > 0)
		
	def test_file_found(self):
		self.assertIsNotNone(self.test_generator.is_file_found("nouns"))
		self.assertIsNotNone(self.test_generator.is_file_found("adjectives"))
	
	def test_file_read(self):
		self.assertIsNotNone(self.test_generator.retrieve_file_info("nouns"))
		self.assertIsNotNone(self.test_generator.retrieve_file_info("adjectives"))
		
	def test_sentence_made(self):
		self.assertIsNotNone(self.test_generator.generate_sentence())
		
if __name__ == "__main__":
	global x
	unittest.main()
