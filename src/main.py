import cv2
import numpy as np
from game import Game
from vision import get_screen
from detect_survivors import Survivors


Survivors = Survivors()
game = Game()

while True:
    input("Continue..")

    image = get_screen()
    Survivors.searchSurv(game.state_pregame(image))

## while True:
##    image = get_screen()
##    if game.state == "PRE_GAME":
##       game.start(image)
##        print("Player type:", game.player_type)
##        print("State:", game.state)
##    elif game.state == "IN_GAME":
##        print("Player type:", game.player_type)
##        print("State:", game.state)
##
##    game.detect_game_state(image)