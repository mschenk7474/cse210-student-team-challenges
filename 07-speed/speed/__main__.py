import os
os.environ['RAYLIB_BIN_PATH'] = r'cse210-student-team-challenges\07-speed\speed\raylib-2.0.0-Win64-mingw'

from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService

def main():
    input_service = InputService()
    output_service = OutputService()
    director = Director(input_service, output_service)
    director.start_game()
