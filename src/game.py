from player_type import detect_player_type
from detect_survivors import detect_survivors


class Game:
    def __init__(self):
        self.state = "PRE_GAME"
        self.player_type = ""
        self.survivors = []
        self.generators = ""
        self.perks = ""
        self.events = ""

    def start(self, image):
        self.player_type = detect_player_type(image)

    def state_pregame(self, image):
        return detect_survivors(image)

    def detect_game_state(self, image):
        #function to search for survivors, so need to input image,
        #in function find surv[0]-surv[3], if true then change state
        if self.state == "":
            self.start(image)
            self.state = "PRE_GAME"
        if self.state == "PRE_GAME":
            if self.state_pregame(image):
                self.state = "IN_GAME"

        return self.state

