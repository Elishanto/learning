from PIL import Image

image = Image.new("RGB", (4726, 4726))

with open('M74207281.txt') as f:
    for i in range(4725):
        for j in range(4725):
            try:
                c = int(f.read(1))
                if c is 0:
                    color = (0, 0, 255)
                elif c is 1:
                    color = (255, 0, 0)
                elif c is 2:
                    color = (0, 128, 0)
                elif c is 3:
                    color = (128, 0, 128)
                elif c is 4:
                    color = (0, 0, 0)
                elif c is 5:
                    color = (255, 165, 0)
                elif c is 6:
                    color = (255, 255, 0)
                elif c is 7:
                    color = (255, 215, 0)
                elif c is 8:
                    color = (255, 255, 255)
                elif c is 9:
                    color = (255, 192, 203)
                else:
                    color = (0, 0, 0)
                image.putpixel((i, j), color)
            except ValueError:
                pass
        if i % 100 is 0:
            print(i * 4725)
            image.save("images/{}.jpg".format(i // 100), "JPEG")
