from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.board import Board

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = None
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()
        self._guess = Guess()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        
        p1 = self._roster.players[0]
        player_1 = p1.get_name()
        p2 = self._roster.players[1]
        player_2 = p2.get_name()
        self._board = Board(player_1, player_2)
        # display the game board
        self._board.print()
        #self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        #I made guess a self variable so that we could use it throughout the director class.
        #self.guess = self._console.read_number("What is your guess? ")
        self.guess = self._guess.get_user_guess()
        self._console.write(" ")
        turn = Move(self.guess)
        player.set_move(turn)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        #Kept this because both of those are needed, so just add an apply method to board
        player = self._roster.get_current()
        #Get the guess and pass that into get guess
        guess = player.get_move()
        secret_code = self._guess.answer_key
        self._board.update_guess(player, guess, secret_code)
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the user has guessed the number in the
        right sequence.

        Args:
            self (Director): An instance of Director.
        """
        #Changed this to is_done for our solution
        if self._guess.player_wins():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()
