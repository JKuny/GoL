# 06/25/2018
#
# IdeaGenerator - Creates a random scene to visualize
# By James Kuny - james.kuny@yahoo.com

import sys
import os
import random


class IdeaGenerator(object):

    def __init__(self, number_of_ideas):
        """ Main constructor. """
        os.chdir(r'.')  # Change directory to where the file is
        self.results = []
        self.number_of_ideas = number_of_ideas

    def generate_ideas(self):
        """
        Creates populate's the generator's result array with
        the object's specied number of ideas.
        """
        ideaArray = []
        for x in range(0, self.number_of_ideas):
            ideaArray.append(self.generate_sentence())

        self.results = ideaArray

    def generate_sentence(self):
        """ Creates a basic sentence with random nouns and adjectives. """
        sentence = "An image of a "
        sentence = sentence + self.retrieve_file_info("nouns")
        sentence = sentence + " that is "
        sentence = sentence + self.retrieve_file_info("adjectives")
        sentence = sentence + "."
        return sentence

    def is_file_found(self, file_name):
        """ Checks to see if the specified file exists. """
        file = open(file_name + ".txt", 'r')
        file.close()
        return file

    def retrieve_file_info(self, file_name):
        """ Return a random value from the specified file. """
        file = open(file_name + ".txt", 'r')

        array = []
        for line in file:
            array.append(line.rstrip())

        file.close()

        index = random.randint(0, len(array) - 1)
        return array[index]


if __name__ == '__main__':
    x = IdeaGenerator(1)
    x.generate_ideas()
    print(x.results[0])
