import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\SchenkKids\Documents\CSE-210-Repos\cse210-student-team-challenges\07-speed\speed\game\raylib-2.0.0-Win64-mingw\lib'

from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService

def main():
    input_service = InputService()
    output_service = OutputService()
    director = Director(input_service, output_service)
    director.start_game()
