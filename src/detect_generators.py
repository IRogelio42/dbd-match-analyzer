##like detect survivors, extract region from image,
## decision: text id or image id, 6 states, 5 gens, 4 gens, 3 gens, 2 gens, 1 gens, 0 gens
## image may be easier
import cv2
from vision import get_region


class Generators:

    def __init__(self):
        self.current = 5
        self.size = 0
        self.update()

    def add_new(self, generator):
        if generator is not None:
            cv2.imwrite("../data/templates/Generators/GenState" + str(self.size) + ".png", generator)
            self.size += 1

    def update(self):
        while True:
            generator = cv2.imread("../data/templates/Generators/GenState" + str(self.size) + ".png")
            if generator is not None:
                self.size += 1
            else:
                break


def detect_generators(image):
    generator_region = get_region(
        image,
        140,
        1071,
        119,
        62
    )
    return generator_region # currently: return region, may be return state