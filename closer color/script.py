from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_conversions import convert_color


def average_colour(image):
    colour_tuple = [None, None, None]
    for channel in range(3):
        pixels = image.getdata(band=channel)

        values = []
        for pixel in pixels:
            values.append(pixel)

        colour_tuple[channel] = sum(values) / len(values)

    return tuple(colour_tuple)


main = average_colour(Image.open('main.jpg'))
main = convert_color(sRGBColor(main[0], main[1], main[2]), LabColor)

to1 = average_colour(Image.open('1.jpg'))
to1 = convert_color(sRGBColor(to1[0], to1[1], to1[2]), LabColor)

to2 = average_colour(Image.open('2.jpg'))
to2 = convert_color(sRGBColor(to2[0], to2[1], to2[2]), LabColor)

print(delta_e_cie1976(main, to1))
print(delta_e_cie1976(main, to2))

