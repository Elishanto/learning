from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie2000 as delta
from colormath.color_conversions import convert_color


def average_color(image):
    colour_tuple = [None, None, None]
    for channel in range(3):
        pixels = image.getdata(band=channel)
        values = []
        for pixel in pixels:
            values.append(pixel)
        colour_tuple[channel] = sum(values) / len(values)
    return tuple(colour_tuple)


main = convert_color(sRGBColor(*average_color(Image.open('main.jpg'))), LabColor)
to1 = convert_color(sRGBColor(*average_color(Image.open('1.jpg'))), LabColor)
to2 = convert_color(sRGBColor(*average_color(Image.open('2.jpg'))), LabColor)

res1 = delta(main, to1)
res2 = delta(main, to2)

print(res1)
print(res2)
if res1 == res2:
    print('=')
elif res1 < res2:
    print(1)
else:
    print(2)
