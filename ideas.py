# 06/25/2018
#
# IdeaGenerator - Creates a random scene to visualize
# By James Kuny - james.kuny@yahoo.com

import sys
import os
import random

class IdeaGenerator(object):
	
	"""
	Main constructor.
	"""
	def __init__(self, number_of_ideas):
		os.chdir(r'.') # Change directory to where file is
		self.results = []
		self.number_of_ideas = number_of_ideas

	"""
	Creates populate's the generator's result array with
	the object's specied number of ideas.
	"""
	def generate_ideas(self):
		ideaArray = []
		for x in range(0, self.number_of_ideas):
			ideaArray.append(self.generate_sentence())
			
		self.results = ideaArray

	"""
	Creates a basic sentence with random nouns and adjectives.
	"""
	def generate_sentence(self):
		sentence = "An image of a "
		sentence = sentence + self.retrieve_file_info("nouns")
		sentence = sentence + " that is "
		sentence = sentence + self.retrieve_file_info("adjectives")
		sentence = sentence + "."
		return sentence

	"""
	Checks to see if the specified file exists.
	"""
	def is_file_found(self, file_name):
		file = open(file_name + ".txt", 'r')
		file.close()
		return file
		
	""" Return a random value from the specified file. """
	def retrieve_file_info(self, file_name):
		file = open(file_name + ".txt", 'r')

		array = []
		for line in file:
			array.append(line.rstrip())

		file.close()

		index = random.randint(0, len(array) - 1)
		return array[index]

if __name__ == '__main__':
	x = IdeaGenerator(3)
	x.generate_ideas()
	print(x.results)
