import random

class Guess:
    def __init__(self):
        self.answer_key = ["*","*","*","*"]
        self.user_guess = ""
        self.end_game = False
        self._random_string = ""

    #get's the answer number
    def get_random_number(self):
        randomnum = random.randint(10000, 19999)
        random_string = str(randomnum)
        random_string = random_string[1:]
        self._random_string = random_string
        return random_string

    #get user guess
    def get_user_guess(self):
        user_guess = input("What is your guess? ")
        userint = int(user_guess)
        while(userint > 9999 or userint < 0):
            user_guess = input("Invalid input!\nWhat is your guess? ")
            userint = int(user_guess)
        self.user_guess = user_guess
        return (user_guess)

    #set the answer key code
    def set_user_key(self, key_num_string):
        answer_key_list = ["*","*","*","*"]
        #change key number and user guess number into string lists
        user_guess_string = self.user_guess
        key_num_list = []
        user_guess_list = []
        for let in key_num_string:
            key_num_list.append(let)
        for let in user_guess_string:
            user_guess_list.append(let)
        
        #make comparision to find answer symbol key
        for i in range(len(key_num_string)):

            #count number of times one of user's numbers is in answer
            is_in_number = key_num_string.count(user_guess_list[i])

            #If user number is same as the answer number position
            if key_num_list[i] == user_guess_list[i]:
                answer_key_list[i] = "X"

            #if user number is in the answer
            elif is_in_number > 0:
                answer_key_list[i] = "O"

            #if number is not in the answer
            else:
                answer_key_list[i] = "*"
        self.answer_key = answer_key_list
        return (answer_key_list)

    #if player is right return true
    def player_wins(self, answer_key):
        if answer_key == ["X","X","X","X"]:
            return True
'''       
guess = Guess()
randomnum = guess.get_random_number()
print(randomnum)
guess.get_user_guess()
print(guess.user_guess)
guess.set_user_key(randomnum)
print(guess.answer_key)'''