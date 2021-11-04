"""
This class keeps track of everything with the words: how the words fly,
how many words fly, etc.
"""


import random
from game.actor import Actor

class Word(Actor):
    def __init__(self):

        super().__init__()
        self._word = ""
        self._segments = []

    def get_word(self):
        with open("/Users/asherhanson/Desktop/CSE250-projects/cse210-student-solo-checkpoints/07-snake/Ash_Snake/game/words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
        
        self.word = (random.choice(words))

        return((self.word))

    def move_word(self, direction):
        """Moves the head in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        word = self.get_word()
        #word.set_velocity(direction)
  