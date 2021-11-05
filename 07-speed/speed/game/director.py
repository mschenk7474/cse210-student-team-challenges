from time import sleep
import random

import raylibpy
from game import constants
from game.score_board import ScoreBoard
from game.words import Word
from game.buffer import Buffer
#from speed.game import buffer

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
        self._buffer_2 = None
        self._buffer = Buffer(self._bufferstring)
        #self._word_string_list = [""]
        self._word = Word()
        self._ifending_x = 50
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

        self._word._prepare_words()
        self._word.get_words()
        print(self._word._word_list)

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
        self._buffer_2 = Buffer(self._bufferstring)

        
        #self._ifending_x = self._word.move_next()
        self._word.move_word()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means seeing if the word is a match, if the word hits
        the wall, removing the words from the list, and then adding and subtracting
        the points.

        Args:
            self (Director): An instance of Director.
        """
        # if self._ifending_x == 0:
        #     self._score_board.sub_points(50)

        self._bufferstring += self._input_service.get_letter()
        
        bufferbool, x = self._buffer_2.match(self._word._word_list)
        counting_score = 0
        if bufferbool:
            word = self._word._word_list[x]
            for let in word:
                counting_score += 1
            self._score_board.add_points(counting_score)

            remove_actor = self._word._words[x]
            self._word._words.remove(remove_actor)
            
            self._bufferstring = ""
        
        random_range = random.randint(1,1500)
        if random_range <= 10:
            self._word._add_word()
            self._word.get_words()
        print(self._word._word_list)
        # #Variable declarations
        # words_to_remove = []
        # add_points_num = 0
        # sub_points_num = 0
        # #If word is match and add points
        # for word in self._word_list:
        #     #Word match here
        #     if word == self._buffer.match(self._word_list):
        #         #Figure out how the addition per letter (1 per letter)
        #         for let in word:
        #             let = 1
        #             let += 1
        #             add_points_num = let
        #         self._score_board.add_points(add_points_num)

        #         #Append the word to the remove list
        #         words_to_remove.append(word)

        # #If word hits wall and sub points
        #     if word == self._word.hit_wall(): #New Function
        #         #Figure out subtraction per letter (-1 per letter)
        #         for let in word:
        #             let = 1
        #             let += 1
        #             let = -(let)
        #             sub_points_num = let
        #         self._score_board.sub_points(sub_points_num)
        #         #Append the word to the remove list
        #         words_to_remove.append(word)


        # #Remove words
        # for word in range(len(self._word_list)):
        #     for words in range(len(words_to_remove)):
        #         if word == words:
        #             self._word_list.pop(word)


        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means outputting the scoreboard, words, and buffer.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        #self._output_service.draw_actors(self._word.display_all()) #New function that needs to be added
        self._output_service.draw_actors(self._word.get_all())
        self._output_service.draw_actor(self._score_board)
        #self._output_service.draw_actor(self._word)
        self._output_service.draw_actor(self._buffer_2)
        self._output_service.flush_buffer()

