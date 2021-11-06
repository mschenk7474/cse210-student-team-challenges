from time import sleep
import random

import raylibpy
from game import constants
from game.score_board import ScoreBoard
from game.words import Word
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._bufferstring = ""
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._buffer = None
        self._word = Word()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

        self._word._prepare_words()

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the five words that will be displayed on the screen.

        Args:
            self (Director): An instance of Director.
        """
        self._buffer = Buffer(self._bufferstring)
        self._word.move_word()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means seeing if the word is a match, if the word hits
        the wall, removing the words from the list, and then adding and subtracting
        the points.

        Args:
            self (Director): An instance of Director.
        """

        self._bufferstring += self._input_service.get_letter()

        # add point for right answer
        bufferbool, x = self._buffer.match(self._word.word_list)
        counting_score = 0
        if bufferbool:
            word = self._word.word_list[x]
            for let in word:
                counting_score += 1
            self._score_board.add_points(counting_score)

            remove_actor = self._word._words[x]
            self._word.word_list.remove(word)
            self._word._words.remove(remove_actor)
            self._bufferstring = ""


        position_list = []
        for i in range(len(self._word.word_list) - 1):
            temp_word_actor = self._word._words[i]
            if temp_word_actor._x < -7:
                word_string = self._word.word_list[i]
                counting_score = 0
                for let in word_string:
                    counting_score += 1    
                self._score_board.sub_points(counting_score)
                position_list.append(i)
        
        forloopint = 0
        for val in position_list:
            remove_actor = self._word._words[val + forloopint]
            temp_word = self._word.word_list[val + forloopint]
            self._word.word_list.remove(temp_word)
            self._word._words.remove(remove_actor)
            forloopint -= 1
    
        #add more words the the program
        random_range = random.randint(1,1500)
        if random_range <= 10:
            self._word._add_word()
        elif len(self._word.word_list) < 1:
            self._word._add_word()
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means outputting the scoreboard, words, and buffer.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._word.get_all())
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()

