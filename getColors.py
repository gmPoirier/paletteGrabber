import os
import sys
from PIL import Image, ImageDraw

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
OUTPUT_FILE = "output.png"

OUTPUT_FILE_WIDTH = 100
OUTPUT_FILE_HEIGHT = 100

def generatePaletteImage(colorDict):
    newImage = Image.new("RGBA",(OUTPUT_FILE_WIDTH,\
                                OUTPUT_FILE_HEIGHT),\
                                (0,0,0,0))

    d = ImageDraw.Draw(newImage)
    x = 0
    y = 0

    for color in colorDict.keys():
        d.point((x,y), color)
        ++x
        if x > OUTPUT_FILE_WIDTH - 1:
            ++y
            x = 0
            if y > OUTPUT_FILE_HEIGHT - 1:
                break
    
    newImage.save(OUTPUT_DIR + "/" + OUTPUT_FILE)

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

    # numColors = len(allImageColors)
    generatePaletteImage(allImageColors)


if __name__ == "__main__":
    main()
