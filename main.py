from PIL import Image


img_name = input("Enter full path to image: ")
img = Image.open(img_name)
pixels = img.load()

width, height = img.size

LETTERS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
s = ""

for i in range(height):
    for j in range(width):
        r, g, b, A = pixels[j, i]
        mid = (r + g + b) // 3
        s += LETTERS[mid // 25]
    s += "\n"

f = open("output.txt", mode="wt")
f.write(s)
f.close()
