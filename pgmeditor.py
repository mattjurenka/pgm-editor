import math

inputstring = "HRLVH"
file = "earth.pgm"

transformations = {'R': 0, 'L': 0, 'V': 0, 'H': 0, 'N': 0, 'B': 0, 'D': 0, 'W': 0, 'C': 0, 'E': 0, 'S': 0}

for i in inputstring:
    transformations[i] = transformations[i] + 1

dupes = ["V", "H", "N"]

for i in dupes:
    if transformations[i] > 1:
        transformations[i] = transformations[i] % 2

pairs = ["ES", "RL", "BD", "WC"]

for i in pairs:
    while (transformations[i[0]] > 0) and (transformations[i[1]] > 0):
        transformations[i[0]] = transformations[i[0]] - 1
        transformations[i[1]] = transformations[i[1]] - 1
quads = ["RVH", "LVH"]

for i in quads:
    while (transformations[i[0]] > 1) and (transformations[i[1]] > 0) and (transformations[i[2]] > 0):
        transformations[i[0]] = transformations[i[0]] - 2
        transformations[i[1]] = transformations[i[1]] - 1
        transformations[i[2]] = transformations[i[2]] - 1

ftransformations = ""

for i in inputstring:
    if transformations[i] > 0:
        ftransformations = ftransformations + i
        transformations[i] = transformations[i] - 1

image = []

i_f = open(file, 'r')

firstline = i_f.readline()
metadata = firstline.split()
width = int(metadata[1])
height = int(metadata[2])

for i in range(0,height):
    h_list = []
    for j in range(0,width):
        h_list.append(int(i_f.readline().strip("\\n")))
    image.append(h_list)

for i in ftransformations:
    trans_image = []
    if i == 'R':
        t = width
        width = height
        height = t
        for j in range(0,height):
            h_list = []
            for k in range(0, width):
                h_list.append(image[width - k - 1][j])
            trans_image.append(h_list)
    elif i == "L":
        t = width
        width = height
        height = t
        for j in range(0,height):
            h_list = []
            for k in range(0, width):
                h_list.append(image[k][height - j - 1])
            trans_image.append(h_list)
    elif i == "V":
        for j in range(0, height):
            trans_image.append(image[height - j - 1])
    elif i == "H":
        for j in range(0, height):
            h_list = []
            for k in range(0, width):
                h_list.append(image[j][width - k - 1])
            trans_image.append(h_list)
    elif i == "N":
        for j in range(0, height):
            for k in range(0, width):
                image[j][k] = 100 - image[j][k]
        trans_image = image
    elif i == "B":
        for j in range(0, height):
            for k in range(0, width):
                image[j][k] = image[j][k] + 10
                if image[j][k] > 100: image[j][k] = 100
        trans_image = image
    elif i == "D":
        for j in range(0, height):
            for k in range(0, width):
                image[j][k] = image[j][k] - 10
                if image[j][k] < 0: image[j][k] = 0
        trans_image = image
    elif i == "W":
        for j in range(0, height):
            for k in range(0, width):
                x = image[j][k]
                if x < 50:
                    x = int(round(8.814*math.log(x+1, 2)))
                elif x > 50:
                    x = int(round(-8.814*math.log(101-x, 2)+100))
                if x < 0:
                    x = 0
                elif x > 100:
                    x = 100
                image[j][k] = x
        trans_image = image
    elif i == "C":
        for j in range(0, height):
            for k in range(0, width):
                x = image[j][k]
                if x < 50:
                    x = int(round(pow(2, (x / 8.814)) - 1))
                elif x > 50:
                    x = int(round(101 - pow(2, ((-x + 100)/8.814))))
                if x < 0:
                    x = 0
                elif x > 100:
                    x = 100
                image[j][k] = x
        trans_image = image
    elif i == "E":
        for j in range(0, height):
            h_list = []
            for k in range(0, width):
                h_list.append(image[j][k])
                h_list.append(image[j][k])
            trans_image.append(h_list)
            trans_image.append(h_list)
        height = height * 2
        width = width * 2
    elif i == "S":
        for j in range(0, int(height / 2)):
            h_list = []
            for k in range(0, int(width / 2)):
                h_list.append(image[2 * j][2 * k])
            trans_image.append(h_list)
        height = int(height / 2)
        width = int(width / 2)
    image = trans_image
    

o_f = open("t" + file, "w")
o_f.write("P2 " + str(width) + " " + str(height) + " 100\n")

for i in range(0, height):
    for j in range(0, width):
        o_f.write(str(image[i][j]) + "\n")

o_f.close()
