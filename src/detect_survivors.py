import cv2
from vision import compare_images, get_region
from config_table import SurvTemplate


class Survivors:
    def __init__(self):
        self.templateSurvs = []
        self.currentSurvs = []
        self.size = 0
        self.update()

    def update(self): # Currently set up for collection
        while True:
            templateSurvOut = cv2.imread("../data/templates/Survivors/identifySurv" + str(self.size) + ".png")
            if templateSurvOut is not None:
                self.templateSurvs.append(templateSurvOut)
                self.size += 1
            else:

                break

        print("Survivor Saved: " + str(self.size))

    def addNew(self, newSurv): #adds to collection
        if newSurv is not None:
            self.templateSurvs.append(newSurv)
            cv2.imwrite("../data/templates/Survivors/identifySurv" + str(self.size) + ".png", newSurv)
            self.size += 1

    def searchSurv(self, Surv): #check if in collection
        if Surv is not None:
            for vors in Surv:
                found = False
                for template in self.templateSurvs:
                    thresh = compare_images(vors, template)
                    if thresh > .8:

                        found = True
                        break

                if not found:
                    print("New Survivor Added.")
                    self.addNew(vors)

    def identifySurv(self): #later dev, identify each of 4 survivors to template
        for vor in self.currentSurvs: #currentSurvs holds images of survivors, match to template image, similar to search
            found = False
            for i, template in enumerate(self.templateSurvs): # search through file system, how to do...? hold information in file name -> then match filename to survivor in config table?
                if compare_images(vor, template) > .7:
                    self.identifiedSurvs.append(SurvTemplate[i]) #SurvTemplate defined in config table where i maps to both filename and survivor name, this index returns survivor name


def detect_survivors(image):
    survivors = []
    ##survivor_base = cv2.imread("../data/screenshots/survivor_0.png")
    for i in range(0, 4):
        survivor_region = get_region(
        image,
        156,
        570 + (118 * i),
        30,
        71
        )
        cv2.imwrite("../data/screenshots/preidentify.png", survivor_region) #get image
        survivors.append(survivor_region) #pass image to survivors
    return survivors # return to survivors -> gets sent to Survivors class
