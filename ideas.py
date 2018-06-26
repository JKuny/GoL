# 06/25/2018
#
# IdeaGenerator - Creates a random scene to visualize
# By James Kuny - james.kuny@yahoo.com

import sys

class IdeaGenerator(object):
	
	def __init__(self, numberOfIdeas):
		self.numberOfIdeas = numberOfIdeas

	def generate_ideas(self):
		ideaArray = []
		for x in range(0, self.numberOfIdeas):
			ideaArray.append(self.new_idea())
			print(ideaArray)
			print(self.new_idea())

	def new_idea(self):
		return "ideas"

if __name__ == '__main__':
	x = IdeaGenerator(1)