# 06/25/2018
#
# IdeaGenerator - Creates a random scene to visualize
# By James Kuny - james.kuny@yahoo.com

import sys
import os
import random

class IdeaGenerator(object):
	
	def __init__(self, numberOfIdeas):
		os.chdir(r'D:\Downloads') # Change directory to where file is
		self.results = []
		self.numberOfIdeas = numberOfIdeas

	def generate_ideas(self):
		ideaArray = []
		for x in range(0, self.numberOfIdeas):
			ideaArray.append(self.new_idea())
			
		self.results = ideaArray

	def new_idea(self):
		return "ideas"
	
	def is_file_found(self):
		file = open("nouns.txt", 'r')
		file.close()
		return file
		
	def retrieve_noun(self):
		file = open("nouns.txt", 'r') # Open file
		
		# Loop through file
		array = []
		for line in file:
			array.append(line)
			
		file.close() # Close file
		return array[random.randint(0, len(array)]

if __name__ == '__main__':
	x = IdeaGenerator(5)
	x.generate_ideas()
	print(x.retrieve_noun())
