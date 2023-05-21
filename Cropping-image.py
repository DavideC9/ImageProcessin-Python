import os

import Image

filepath = 'C:\\Users\\david\\Desktop\\Immagini\\Ransomware1'

for filename in os.listdir(filepath):
    if "." not in filename:
        continue
    ending = filename.split(".")[1]
    if ending not in ["jpg", "gif", "png"]:
        continue

    try:
        image = Image.open(os.path.join(filepath, filename))
    except IOError as e:
        print("Problem Opening", filepath, ":", e)
        continue

    image = image.crop((400, 35, 800, 435)).thumbnail(400,400) #image = image.crop((0, 35, 400, 435))

    name, extension = os.path.splitext(filename)
    print(name + '_cropped.jpg')
    image.save(os.path.join('C:\\Users\\david\\Desktop\\Immagini\\CROPP2\\', name + '_cropped.png'))
