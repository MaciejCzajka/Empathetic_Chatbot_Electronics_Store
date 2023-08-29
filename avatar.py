#!/usr/bin/env python

import py_avataaars as pa
import cv2 as cv
import os

style = ['CIRCLE', 'TRANSPARENT']

skin_color = ['TANNED', 'YELLOW', 'PALE', 'LIGHT', 'BROWN', 'DARK_BROWN', 'BLACK']

hair_color = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PASTEL_PINK', 'PLATINUM', 'RED', 'SILVER_GRAY']

hat_color = ['BLACK', 'BLUE_01', 'BLUE_02', 'BLUE_03', 'GRAY_01', 'GRAY_02', 'HEATHER', 'PASTEL_BLUE', 'PASTEL_GREEN', 'PASTEL_ORANGE',
             'PASTEL_RED', 'PASTEL_YELLOW', 'PINK', 'RED', 'WHITE']

facial_hair_type = ['DEFAULT', 'BEARD_MEDIUM', 'BEARD_LIGHT', 'BEARD_MAJESTIC', 'MOUSTACHE_FANCY', 'MOUSTACHE_MAGNUM']

top_type = ['NO_HAIR', 'EYE_PATCH', 'HAT', 'HIJAB', 'TURBAN', 'WINTER_HAT1', 'WINTER_HAT2', 'WINTER_HAT3',
            'WINTER_HAT4', 'LONG_HAIR_BIG_HAIR', 'LONG_HAIR_BOB', 'LONG_HAIR_BUN', 'LONG_HAIR_CURLY', 'LONG_HAIR_CURVY',
            'LONG_HAIR_DREADS', 'LONG_HAIR_FRIDA', 'LONG_HAIR_FRO', 'LONG_HAIR_FRO_BAND', 'LONG_HAIR_NOT_TOO_LONG',
            'LONG_HAIR_SHAVED_SIDES', 'LONG_HAIR_MIA_WALLACE', 'LONG_HAIR_STRAIGHT', 'LONG_HAIR_STRAIGHT2',
            'LONG_HAIR_STRAIGHT_STRAND', 'SHORT_HAIR_DREADS_01', 'SHORT_HAIR_DREADS_02', 'SHORT_HAIR_FRIZZLE',
            'SHORT_HAIR_SHAGGY_MULLET', 'SHORT_HAIR_SHORT_CURLY', 'SHORT_HAIR_SHORT_FLAT', 'SHORT_HAIR_SHORT_ROUND',
            'SHORT_HAIR_SHORT_WAVED', 'SHORT_HAIR_SIDES', 'SHORT_HAIR_THE_CAESAR', 'SHORT_HAIR_THE_CAESAR_SIDE_PART']

mouth_type = ['DEFAULT', 'CONCERNED', 'DISBELIEF', 'EATING', 'GRIMACE', 'SAD', 'SCREAM_OPEN', 'SERIOUS', 'SMILE', 'TONGUE', 'TWINKLE', 'VOMIT']

eye_type = ['DEFAULT', 'CLOSE', 'CRY', 'DIZZY', 'EYE_ROLL', 'HAPPY', 'HEARTS', 'SIDE', 'SQUINT', 'SURPRISED', 'WINK', 'WINK_WACKY']

eyebrow_type = ['DEFAULT', 'DEFAULT_NATURAL', 'ANGRY', 'ANGRY_NATURAL', 'FLAT_NATURAL', 'RAISED_EXCITED',
                'RAISED_EXCITED_NATURAL', 'SAD_CONCERNED', 'SAD_CONCERNED_NATURAL', 'UNI_BROW_NATURAL', 'UP_DOWN',
                'UP_DOWN_NATURAL', 'FROWN_NATURAL']

accessories_type = ['DEFAULT', 'KURT', 'PRESCRIPTION_01', 'PRESCRIPTION_02', 'ROUND', 'SUNGLASSES', 'WAYFARERS']

clothe_type = ['BLAZER_SHIRT', 'BLAZER_SWEATER', 'COLLAR_SWEATER', 'GRAPHIC_SHIRT', 'HOODIE', 'OVERALL', 'SHIRT_CREW_NECK',
               'SHIRT_SCOOP_NECK', 'SHIRT_V_NECK']

clothe_color = ['BLACK', 'BLUE_01', 'BLUE_02', 'BLUE_03', 'GRAY_01', 'GRAY_02', 'HEATHER', 'PASTEL_BLUE', 'PASTEL_GREEN',
                'PASTEL_ORANGE', 'PASTEL_RED', 'PASTEL_YELLOW', 'PINK', 'RED', 'WHITE']

clothe_graphic_type = ['BAT', 'CUMBIA', 'DEER', 'DIAMOND', 'HOLA', 'PIZZA', 'RESIST', 'SELENA', 'BEAR', 'SKULL_OUTLINE', 'SKULL']

facial_hair_color = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PLATINUM', 'RED']

def modify_avatar():
    style_param = cv.getTrackbarPos('style', 'Avatar')
    skin_color_param = cv.getTrackbarPos('skin color', 'Avatar')
    hair_color_param = cv.getTrackbarPos('hair color', 'Avatar')
    hat_color_param = cv.getTrackbarPos('hat color', 'Avatar')
    facial_hair_type_param = cv.getTrackbarPos('facial hair type', 'Avatar')
    top_type_param = cv.getTrackbarPos('top type', 'Avatar')
    mouth_type_param = cv.getTrackbarPos('mouth type', 'Avatar')
    eye_type_param = cv.getTrackbarPos('eye type', 'Avatar')
    eyebrow_type_param = cv.getTrackbarPos('eyebrow type', 'Avatar')
    accessories_param = cv.getTrackbarPos('accessories', 'Avatar')
    clothe_type_param = cv.getTrackbarPos('clothe type', 'Avatar')
    clothe_color_param = cv.getTrackbarPos('clothe color', 'Avatar')
    clothe_graphic_param = cv.getTrackbarPos('clothe graphic', 'Avatar')

    param_list = [style_param, skin_color_param, top_type_param, hair_color_param, hat_color_param, facial_hair_type_param,
                  mouth_type_param, eye_type_param, eyebrow_type_param, accessories_param, clothe_type_param,
                  clothe_color_param, clothe_graphic_param]

    avatar = pa.PyAvataaar(
        style=eval('pa.AvatarStyle.%s' % style[style_param]),
        skin_color=eval('pa.SkinColor.%s' % skin_color[skin_color_param]),
        top_type=eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % top_type[top_type_param]),
        hair_color=eval('pa.HairColor.%s' % hair_color[hair_color_param]),
        hat_color=eval('pa.Color.%s' % hat_color[hat_color_param]),
        facial_hair_type=eval('pa.FacialHairType.%s' % facial_hair_type[facial_hair_type_param]),
        mouth_type=eval('pa.MouthType.%s' % mouth_type[mouth_type_param]),
        eye_type=eval('pa.EyesType.%s' % eye_type[eye_type_param]),
        eyebrow_type=eval('pa.EyebrowType.%s' % eyebrow_type[eyebrow_type_param]),
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=eval('pa.AccessoriesType.%s' % accessories_type[accessories_param]),
        clothe_type=eval('pa.ClotheType.%s' % clothe_type[clothe_type_param]),
        clothe_color=eval('pa.Color.%s' % clothe_color[clothe_color_param]),
        clothe_graphic_type=eval('pa.ClotheGraphicType.%s' % clothe_graphic_type[clothe_graphic_param])
    )
    avatar.render_png_file("AVATAR.png")
    new_avatar = cv.imread("AVATAR.png", 1)
    cv.imshow('Avatar', new_avatar)

    with open('avatar.txt', 'w') as f:
        for i in param_list:
            f.write(str(i)+'\n')

def main():
    cv.namedWindow('Avatar')
    cv.moveWindow('Avatar', 725, 100)
    param_list = []

    if os.path.isfile('avatar.txt'):
        with open('avatar.txt') as f:
            for line in f:
                param_list.append(int(line.strip()))
    else:
        for i in range(13):
            param_list.append(0)

    cv.createTrackbar('style', 'Avatar', param_list[0], 1, modify_avatar)
    cv.createTrackbar('skin color', 'Avatar', param_list[1], 6, modify_avatar)
    cv.createTrackbar('facial hair type', 'Avatar', param_list[5], 5, modify_avatar)
    cv.createTrackbar('top type', 'Avatar', param_list[2], 34, modify_avatar)
    cv.createTrackbar('hair color', 'Avatar', param_list[3], 9, modify_avatar)
    cv.createTrackbar('hat color', 'Avatar', param_list[4], 14, modify_avatar)
    cv.createTrackbar('mouth type', 'Avatar', param_list[6], 11, modify_avatar)
    cv.createTrackbar('eye type', 'Avatar', param_list[7], 11, modify_avatar)
    cv.createTrackbar('eyebrow type', 'Avatar', param_list[8], 12, modify_avatar)
    cv.createTrackbar('accessories', 'Avatar', param_list[9], 6, modify_avatar)
    cv.createTrackbar('clothe type', 'Avatar', param_list[10], 8, modify_avatar)
    cv.createTrackbar('clothe color', 'Avatar', param_list[11], 14, modify_avatar)
    cv.createTrackbar('clothe graphic', 'Avatar', param_list[12], 10, modify_avatar)

    while (True):
        modify_avatar()

        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

    cv.destroyAllWindows()
    cv.waitKey(1)


if __name__ == "__main__":
    main()