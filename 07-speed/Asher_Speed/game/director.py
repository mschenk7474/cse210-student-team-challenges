from time import sleep

import raylibpy
from game import constants
from game.food import Food
from game.score_board import ScoreBoard
from game.snake import Snake
from game.words import Word

class Director:

    def __init__(self, input_service, output_service):

        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._snake = Snake()
        self._word = Word()
        self.word = []
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")
        for i in range(5):
            word = self._word.get_word()
            self.word.append(word)

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.
        Args:
            self (Director): An instance of Director.
        """
        direction = self._input_service.get_direction()
        self._snake.turn_head(direction)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.
        Args:
            self (Director): An instance of Director.
        """
        self._snake.move()
        self._handle_body_collision()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.
        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._snake.get_all())
        for i in range(len(self.word)):
            self._output_service.draw_text(self.word[i],raylibpy.BLACK)
        self._output_service.flush_buffer()

    def _handle_body_collision(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.
        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        body = self._snake.get_collidable_segments()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _is_collision(self, first, second):
        x1 = first.get_position().get_x()
        y1 = first.get_position().get_y()
        width1 = first.get_width()
        height1 = first.get_height()

        rectangle1 = raylibpy.Rectangle(x1, y1, width1, height1)

        x2 = second.get_position().get_x()
        y2 = second.get_position().get_y()
        width2 = first.get_width()
        height2 = first.get_height()

        rectangle2 = raylibpy.Rectangle(x2, y2, width2, height2)

        return raylibpy.check_collision_recs(rectangle1, rectangle2)
