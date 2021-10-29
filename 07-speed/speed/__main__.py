import os
os.environ['RAYLIB_BIN_PATH'] = r'../07-speed'

from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService

def main():
    input_service = InputService()
    output_service = OutputService()
    director = Director(input_service, output_service)
    director.start_game()
