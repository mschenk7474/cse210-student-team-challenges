
class Board:
    def __init__(self, p1, p2):
        self._player1 = p1
        self._player2 = p2
        self._guess1 = "----"
        self._guess2 = "----"
        self._hint1 = "****"
        self._hint2 = "****"

    def update_guess(self, player, guess, hint):
        if player == self._player1:
            self._guess1 = guess
            self._player1 = player
            self._hint1 = hint
            #print(self._player1, self._guess1, self._hint1)

        else:
            self._guess2 = guess
            self._hint2 = hint
            #print(self._player2, self._guess2, self._hint2)


    def print(self):
        print("--------------------")
        print("Player {0}: {1}, {2}".format(self._player1, self._guess1, self._hint1))
        print("Player {0}: {1}, {2}".format(self._player2, self._guess2, self._hint2))
        print("--------------------")
        pass
