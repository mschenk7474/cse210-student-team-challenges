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
        self._roster = Roster()
        self._guess = Guess()
        self.guess = 0
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        print("\n")
        p1 = self._roster.players[0]
        player_1 = p1.get_name()
        p2 = self._roster.players[1]
        player_2 = p2.get_name()
        self.random_number = self._guess.get_random_number()
        self._board = Board(player_1, player_2)
        self._board.print()
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
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        self.user_guess = self._guess.get_user_guess()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        actual_player = player.get_name()
        self.secret_code = self._guess.set_user_key(self.random_number)
        self._board.update_guess(actual_player, self.user_guess, self.secret_code)
        self._board.print()
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the user has guessed the number in the
        right sequence.

        Args:
            self (Director): An instance of Director.
        """
        if self._guess.player_wins(self.secret_code):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()
