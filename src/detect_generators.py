##like detect survivors, extract region from image,
## decision: text id or image id, 6 states, 5 gens, 4 gens, 3 gens, 2 gens, 1 gens, 0 gens
## image may be easier
import cv2
from vision import get_region


def detect_generators(image):
    generator_region = get_region(
        image,
        140,
        1071,
        119,
        62
    )
    cv2.imwrite("./temp/preidentify_gen.png", generator_region) #get image
    return generator_region # currently: return region, may be return state