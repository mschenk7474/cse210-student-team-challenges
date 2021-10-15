import re
from game.word_bank import Word_Bank
from game.player import Player

class Game_Master:

    def __init__(self):
        """
        An instance of the class Game_master 

        Attributes: 
              player: an instance of the class Player()
              guess (boolean): keeps track if the player guess correctly or not
        """

        self.player = Player()
        self.word_bank = Word_Bank()
        self.guess_check = False
        self.letters_right = 0
        self.lives = 0
        

    def check_guess(self, letter, word):
        """
        Makes sure the guess of players guess is correct. 
        """
        # get the players letter guess 
        player_guess = letter[-1]
        # make the guess a lowercase 
        player_guess.lower()
        # save the word as a variable 
        word = word
        
        # count the number of times the letter is in the word
        self.letters_right = word.count(player_guess)

        
        if self.letters_right > 0: 
          guess_check = True
        else: 
          guess_check = False
          self.lives += 1

        return guess_check, self.lives
    
    def change_underscore(self):
        word = self.word_bank.get_word
        guess = self.player.ask_letter
        guess_check = self.check_guess()
        #word_list, underscore_list = self.word_bank.make_list(word)

        #Check to make sure 
        if guess_check == True:
            #update index on underscore list with index from word list from the guess
            pass
        #Returns the underscore list for the display
        
        #return underscore_list