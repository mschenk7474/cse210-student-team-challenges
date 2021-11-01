import random
from game.actor import Actor
from game.point import Point

"""
This class will be for input, mainly the typing of the letters to create the words.
"""
class Buffer():
   def __init__(self):
      super().__init__()
      self._string= input(" ")
      position = Point(0,0)
      self.set_position(position)
      self.set_text(f"Buffer: {self._string}")
   def get_string(self):
      return self._string
   def match(self, word_list):
      for x in word_list:
         if self._string == word_list[x]:
            return 1
         else:
            return 0