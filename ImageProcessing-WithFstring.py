from PIL import Image
from os.path import isfile, join
from os import listdir
import sys
import numpy as np

di={}
with open("simbolitotalicolori.txt", encoding="utf-8") as f:
    for line in f:
        t = line.rstrip().split()
        di[t[1]]=t[0]

for s in range(500):  # ciclo per ogni immagine

    filepathgialli = 'C:\\Users\\david\\Desktop\\ProvaImmagini\\resizeHeatmap\\'  # percorso immagini Heatmap (dove sono presenti i pixel gialli)
    yellowfile = [
        f for f in listdir(filepathgialli)
    ]

    filepathgray = 'C:\\Users\\david\\Desktop\\ProvaImmagini\\CROPP1\\'  # percorso immagini Originali del Ransomware(dove sono presenti i pixel grigi)
    grayfile = [
        f for f in listdir(filepathgray)
    ]

    if yellowfile[s] != grayfile[s]:  # controllo se le immagini hanno lo stesso nome
        print(str(grayfile))
        print(str(yellowfile))
        sys.exit('Le immagini hanno nomi diversi')

    result = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\Trovati\\'+(str(yellowfile[s]))+'.txt','w',encoding="utf-8")
    result = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\Trovati\\'+(str(yellowfile[s]))+'.txt','a',encoding="utf-8")

    result1 = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\NonTrovati\\' + (str(yellowfile[s])) + '.txt', 'w')
    result1 = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\NonTrovati\\' + (str(yellowfile[s])) + '.txt', 'a')

    im = Image.open(filepathgialli + yellowfile[s])  # apro l'immagine Heatmap

    print(str(yellowfile[s]))
    pix = im.load()
    coordinate = []
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if (pix[x, y][0] >= 51 and pix[x, y][0] <= 255) and (pix[x, y][1] >= 51 and pix[x, y][1] <= 255) and (
                    pix[x, y][2] >= 0 and pix[x, y][2] <= 125):
                pixelG = f"{pix[x, y][0]},{pix[x, y][1]},{pix[x, y][2]}"
                coordinate.append(f"{x},{y}")

    im1 = Image.open(filepathgray + grayfile[s])  # apro l'immagine originale ransomware
    print(str(grayfile[s]))
    pix1 = im1.load()
    pixelGrey = []
    for x1 in range(im1.size[0]):
        for y1 in range(im1.size[1]):
            coordinate1 = f"{x1},{y1}"
            # coo1.append(coordinate1)
            if coordinate1 in coordinate:
                pixGrey = f"{pix1[x1, y1][0]},{pix1[x1, y1][1]},{pix1[x1, y1][2]}"
                if pixGrey in di.keys():
                    print('si')
                    print(di[pixGrey])
                    result.write(str(di[pixGrey]))
                    if pixGrey not in di.keys():
                        result1.write('[' + str(coordinate1) + ']')
                        print('no')

        result.write('\n')
        result1.write('\n')


result.close()
result1.close()





#print("k={} v={}".format(k, v))
                    #else:
                        #result1.write('[' + str(coordinate1) + ']')
                            #print('no')
