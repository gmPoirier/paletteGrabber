import os
import sys
from PIL import Image, ImageDraw

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
OUTPUT_FILE = "output.png"

def main():
    allImageColors = {}

    for file in os.listdir(INPUT_DIR):
        if file.endswith('png'):
            image = Image.open(INPUT_DIR + "/" + file)
            image = image.convert("RGBA")
            imageColors = image.getcolors(image.size[0] * image.size[1])

            for color in imageColors:
                if color[1] in allImageColors:
                    allImageColors[color[1]] += color[0]
                else:
                    allImageColors[color[1]] = color[0]

    numColors = len(allImageColors)
    newImage = Image.new("RGBA",(100,100),(0,0,0,0))
    d = ImageDraw.Draw(newImage)

    x = 0
    y = 0
    for color in allImageColors.keys():
        d.point((x,y), color)
        x += 1
        if x > 99:
            y += 1
            x = 0

    newImage.save(OUTPUT_DIR + "/" + OUTPUT_FILE)



if __name__ == "__main__":
    main()
