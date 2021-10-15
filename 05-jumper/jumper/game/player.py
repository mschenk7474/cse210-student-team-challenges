class Player:
    def __init__(self):
        pass

    def ask_letter():
        guess = input("Guess a letter [a-z]: ")
        return guess
    
    def guess_letter():
        """
        Add the letter to the library
        """
        lib = []
        letter = (Player.ask_letter())
        while letter in lib:
            print("That letter was already chosen:")
            letter = (Player.ask_letter())
        lib.append(letter)
        return lib