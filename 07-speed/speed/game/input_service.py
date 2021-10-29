import sys

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if event == 27:
                sys.exit()
            elif event == 10: 
                result = "*"
            elif event >= 97 and event <= 122: 
                result = chr(event)
        return result

#Snake Game 

import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is
    to detect player keypresses and translate them into a point representing
    a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _current (Point): The last direction that was pressed.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._current = Point(1, 0)
        
    def get_direction(self):
        """Gets the selected direction. If one hasn't been selected the last 
        one is returned.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        if self.is_left_pressed():
            self._current = Point(-1, 0)
        elif self.is_right_pressed():
            self._current = Point(1, 0)
        elif self.is_up_pressed():
            self._current = Point(0, -1)
        elif self.is_down_pressed():
            self._current = Point(0, 1)

        return self._current

    def is_left_pressed(self):
        """
        Determines if the left key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        """
        Determines if the right key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        """
        Determines if the up key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        """
        Determines if the down key is currently being pushed
        """
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def window_should_close(self):
        """
        Determines if the user is trying to close the window
        """
        return raylibpy.window_should_close()