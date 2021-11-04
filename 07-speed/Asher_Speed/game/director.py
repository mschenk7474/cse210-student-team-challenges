from time import sleep

import raylibpy
from game import constants
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
        pass

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.
        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.
        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        for i in range(len(self.word)):
            self._output_service.draw_text(self.word[i],raylibpy.BLACK)
        self._output_service.flush_buffer()

