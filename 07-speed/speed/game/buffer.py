import random
from game.actor import Actor
from game.point import Point

"""
This class will be for input, mainly the typing of the letters to create the words.
"""
class Buffer(Actor):
   def __init__(self, bufferstring):
      super().__init__()
      self._string = bufferstring
      position = Point(1,370)
      self.set_position(position)
      self.set_text(f"Buffer: {self._string}")

   def get_string(self):
      return self._string

   def match(self, word_list):
      is_in_word = 0
      number_loop = len(word_list)
      x = 0
      while(is_in_word == 0 and x < number_loop):
         is_in_word = self._string.count(word_list[x])
         x += 1

      if is_in_word > 0:
         return True
      else:
         return False
   #if returns true, the word that's correct is word_list[x-1]
