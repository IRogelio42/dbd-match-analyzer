import cv2
from vision import compare_images, get_screen
from detect_generators import detect_generators, Generators

#image = cv2.imread("../data/screenshots/test_gen2.png")
#image2 = cv2.imread("../data/screenshots/test_gen_out.png")
#imagegen = detect_generators(image)
#cv2.imwrite("../data/screenshots/test_gen_out2.png", imagegen)

#print(compare_images(image, image))

#collection system
Gens = Generators()
while True:
    input("Continue..")

    image = get_screen()
    Gens.add_new(detect_generators(image))

