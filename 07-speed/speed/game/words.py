"""
This class keeps track of everything with the words: how the words fly,
how many words fly, etc.
"""


import random
from game.actor import Actor
from game.point import Point

class Word():
    def __init__(self):

        super().__init__()
        self._word = None
        self._words = []
        self._prepare_words()
        self._word_list = []

    def get_all(self):
        return self._words

    def get_word(self):
        with open("speed\game\words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
        
        word = (random.choice(words))

        return((word))

    def move_word(self):
        """Moves the head in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        for word in self._words:
            word.move_next()
        #word.set_velocity(direction)

    def _add_word(self):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        velocity = Point(-1, 0)
        y = random.randint(30, 340)
        position = Point(500, y)
        self._word = Actor()
        word = self.get_word()
        self._word.set_text(word)
        self._word.set_position(position)
        self._word.set_velocity(velocity)
        self._words.append(self._word)

    def get_words(self):
        for word in self._words:
            string_word = word.get_text()
            self._word_list.append(string_word)
        #return self._word_list

    def hit_wall():
        """
        This determines if the word hits the "wall" meaning that it hit 
        0 on the X-axis.

        Needs to return true or false.
        """
        pass

    def _prepare_words(self):
        for i in range(0, 5):
            self._add_word()