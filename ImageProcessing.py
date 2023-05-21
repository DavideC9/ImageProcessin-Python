from PIL import Image
from os.path import isfile, join
from os import listdir
import sys
import numpy as np

name = []
colour = []

for s in range(1):  # ciclo per ogni immagine

    filepathgialli = 'C:\\Users\\david\\Desktop\\ProvaImmagini\\resizeHeatmap\\'  # percorso immagini Heatmap (dove sono presenti i pixel gialli)
    yellowfile = [
        f for f in listdir(filepathgialli)
    ]

    filepathgray = 'C:\\Users\\david\\Desktop\\ProvaImmagini\\CROPP1\\'  # percorso immagini Originali del Ransomware(dove sono presenti i pixel grigi)
    grayfile = [
        f for f in listdir(filepathgray)
    ]

    if yellowfile[s] != grayfile[s]:  # controllo se le immagini hanno lo stesso nome
        result.write('Le immagini hanno nomi diversi')
        result.close()
        sys.exit('Le immagini hanno nomi diversi')

    result = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\' + (str(yellowfile[s])) + '.txt', 'w')

    img = Image.open(filepathgialli + yellowfile[s])  # apro l'immagine Heatmap
    size = w, h = img.size
    data = img.load()
    pieces = []

    for x in range(w):
        for y in range(h):
            rgb_color = img.getpixel((x, y))
            if ((rgb_color[0] >= 51 and rgb_color[0] <= 255) and (rgb_color[1] >= 51 and rgb_color[1] <= 255) and (
                    rgb_color[2] >= 0 and rgb_color[2] <= 125)):
                pieces.append((x, y, rgb_color))


    img2 = Image.open(filepathgray + grayfile[s])  # apro l'immagine originale ransomware(dove sono i grigi)

    size = w, h = img2.size
    data = img2.load()

    pieces1 = []  # qui salvo solo colori grigi
    greycoo = []  # qui salvo cooordinate + colori grigi

    # ---------------------------------- ciclo l' immagine Originale e salvo in pieces1 tutti i pixel grigi con le coordinate
    for coordinates_giallo in pieces:
        rgb_color = img2.getpixel((coordinates_giallo[0], coordinates_giallo[1]))
        print(rgb_color)
        pieces1.append(rgb_color)  # qui salvo solo colori grigi

        greycoo.append((coordinates_giallo[0], coordinates_giallo[1], rgb_color))  # qui salvo cooordinate + colori grigi
    # ----------------------------------
    # print(pieces1) io qua ho gia il match con i ggialli e salvo i grigi equivalenti in pieces1

    # qui inizia il controllo con il file legend, prima salvo i nomi e i colori
    data = np.loadtxt("legend.txt", skiprows=1, dtype='str')
    nome_mw = []
    colore_mw = []
    for each in data:
        nome_mw.append(each[0])
        colore_mw.append(each[1])
    print(yellowfile[s])  # stampo a schermo il nome dell'immagine heatmap che sto processando
    print(grayfile[s])  # stampo a schermo il nome dell'immagine originale che sto processando
    print('Immagine ' + str(s) + ':')
    result.write(str(yellowfile[s]) + '\n')  # scrivo i nomi nel file
    result.write(str(grayfile[s]) + '\n')
    result.write('Immagine ' + str(s) + ':\n')



    mylistcolorlegend = [tuple(map(int, i.split(','))) for i in colore_mw]  # salvo i colori in mylist come tuple
    indice = 0

    # ciclo controllo colori con il file legend
    for i in mylistcolorlegend:  # scorro i colori del file legend
        for piece in pieces1:  # scorro i grigi
            if i == piece:  # se i colori sono uguali li salvo
                print(nome_mw[indice], i, piece)
                result.write('            ' + nome_mw[indice] + str(i) + '\n')
                nome_trovati = nome_mw[indice]  # nome opcode trovato
                name.append(nome_trovati)  # appendo gli opcode trovati
                colore_trovati = i  # salvo il colore dell'Opcode trovato
                colour.append(colore_trovati)  # appendo il colore dell'Opcode trovato
        indice = indice + 1

    print('\n')
    print('*******************************************************************************')
    print('\n')

    # qui stampo sopra l'immagine nera solo il pezzo giallo d'interesse
    imY = Image.open(
        "C:\\Users\\david\\Desktop\\ProvaImmagini\\black\\black.jpg")  # apro un'immigine nera e ci salvo la zona di pixel gialli
    newsize = (w, h)
    imY = imY.resize(newsize)
    for i in pieces:
        imY.putpixel((i[0], i[1]), i[2])  # sovrappongo i pixel in pieces e li metto al loro posto ma sull'immagine nera
    imY = imY.convert("RGB")

    imY.save("C:\\Users\\david\\Desktop\\ProvaImmagini\\zonegialle\\" + (str(yellowfile[s])) + ".png")

    # qui stampo sopra l'immagine nera solo il pezzo grigio d'interesse
    imG = Image.open(
        "C:\\Users\\david\\Desktop\\ProvaImmagini\\black\\black.jpg")  # apro un'immigine nera e ci salvo la zona di pixel grigi
    newsize = (w, h)
    imG = imG.resize(newsize)
    for i in greycoo:
        imG.putpixel((i[0], i[1]), i[2])  # sovrappongo i pixel di pos e li metto al loro posto ma sull'immagine nera
    imG = imG.convert("RGB")

    imG.save("C:\\Users\\david\\Desktop\\ProvaImmagini\\zonegrigie\\" + (str(grayfile[s])) + ".png")
    result.write('\n\n')
result.close()

nomiTrovati = []
coloriTrovati = []
coloriNONtrovati = mylistcolorlegend
nomiNONtrovati = nome_mw

for i in nome_mw:  # ciclo per tutti i nomi del file legend
    for j in name:  # ciclo per tutti i nomi trovati
        if i == j:  # se i nomi sono uguli li metto in nomiTrovati, e li rimuovo da nomiNONtrovati
            nomiTrovati.append(i)
            nomiNONtrovati.remove(i)
            break

for i in mylistcolorlegend:  # ciclo per tutti i colori del file legend
    for j in colour:  # ciclo per tutti i colori trovati
        if i == j:  # se i colori sono uguli li metto in coloriTrovati, e li rimuovo da coloriNONtrovati
            coloriTrovati.append(j)
            coloriNONtrovati.remove(j)
            break

listaTrovati = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\listaTrovati.txt', 'w')
listaTrovati.write('Lista Trovati: ' + '\n')
listaTrovati = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\listaTrovati.txt', 'a')
print('lista trovati')
for i in range(len(nomiTrovati)):  # ciclo i nomi trovati
    print(str(nomiTrovati[i]) + str(coloriTrovati[i]))
    listaTrovati.write(str(nomiTrovati[i]) + '  ' + str(coloriTrovati[i]) + '\n')

listaTrovati.close()

listaNONtrovati = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\listaNONtrovati.txt', 'w')
listaNONtrovati.write('Lista Non Trovati: ' + '\n')
listaNONtrovati = open('C:\\Users\\david\\Desktop\\ProvaImmagini\\legend\\listaNONtrovati.txt', 'a')

print('lista non trovati')
for i in range(len(nomiNONtrovati)):  # ciclo i nominon trovati
    print(str(nomiNONtrovati[i]) + str(coloriNONtrovati[i]))
    listaNONtrovati.write(str(nomiNONtrovati[i]) + '  ' + str(coloriNONtrovati[i]) + '\n')

listaNONtrovati.close()
