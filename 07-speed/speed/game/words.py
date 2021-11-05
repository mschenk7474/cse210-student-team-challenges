"""
This class keeps track of everything with the words: how the words fly,
how many words fly, etc.
"""


import random
from game.actor import Actor
from game.point import Point

class Word(Actor):
    def __init__(self):

        super().__init__()
        self._word = "George"
        y = random.randint(30, 340)
        position = Point(500, y)
        self.set_position(position)
        velocity = Point(-1,0)
        self.set_velocity(velocity)
        self.set_text(f"Word: {self._word}")


    def get_word(self):
        with open("speed\game\words.txt", "r") as file:
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
    def hit_wall():
        """
        This determines if the word hits the "wall" meaning that it hit 
        0 on the X-axis.

        Needs to return true or false.
        """
        pass
  