import cv2
from vision import compare_images

size = 0
templateSurvs = []

while True:
    templateSurvOut = cv2.imread("../data/templates/Survivors/identifySurv" + str(size) + ".png")
    if templateSurvOut is not None:
        templateSurvs.append(templateSurvOut)
        size += 1
    else:
        break

vors = cv2.imread("../data/templates/Survivors/identifySurv32.png")
print("Compared against Surv 32")
# Cheryl
size = 0
for template in templateSurvs:
    thresh = compare_images(vors, template)
    if thresh > .8:
        print("Match")
    print("Surv" + str(size) + ":" + str(thresh))
    size += 1

