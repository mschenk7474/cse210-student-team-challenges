from game.board import Board


class Director:
    def __init__(self):
        self._board = None

    def start_game(self):
        self._board = Board("Jack", "Steven")
        self._board.update_guess("Jack", "0440", "*oo*")
        self._board.update_guess("Steven", "0490", "**o*")
        self._board.print()

        #text = self._board.get_display_text()
        #print(text)