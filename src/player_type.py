import cv2
from vision import compare_images, get_region


def detect_player_type(image):
    x = 2348
    y = 1305
    width = 128
    height = 87

    player_type_region = get_region(
        image,
        x,
        y,
        width,
        height
    )
    survivor_template = cv2.imread(
        "../data/templates/player_type/player_typeA.png"
    )

    killer_template = cv2.imread(
        "../data/templates/player_type/player_typeB.png"
    )

    survivor_score = compare_images(
        player_type_region,
        survivor_template
    )

    killer_score = compare_images(
        player_type_region,
        killer_template
    )
    print(killer_score)
    print(survivor_score)
    if survivor_score > killer_score:
        player_type = "Survivor"
    elif killer_score > .7:
        player_type = "Killer"
    else:
        player_type = "Null"

    return player_type
