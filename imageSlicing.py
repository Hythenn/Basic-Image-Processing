#CS124P Module 1-B Laboratory Exercise
#   1. Allow user to select 10 points in given image.
#      Program shall display/print RGB value of specific pixel of selected points.
#
#   2. Write Program that will dynamically fill a 180x180 RGB image with following details.
#
#   3. Select a digital image and perform 4 gray transforms using default values.
#      Allow each image to undergo Histogram and compare the results accordingly through a short discussion


# RGB IMAGE SLICING
from PIL import Image
from numpy import *
from pylab import *

# COLORS
Red = {
    "color1": [240, 40, 40],
    "color2": [255, 100, 100]
}
Orange = {
    "color1": [240, 140, 40],
    "color2": [255, 180, 80]
}
Yellow = {
    "color1": [240, 240, 40],
    "color2": [255, 255, 100]
}
Green = {
    "color1": [40, 240, 40],
    "color2": [100, 255, 100]
}
Blue = {
    "color1": [40, 40, 240],
    "color2": [100, 100, 255]
}
Violet = {
    "color1": [180, 80, 200],
    "color2": [220, 120, 240]
}
White = {
    "color1": [240, 240, 240],
    "color2": [255, 255, 255]
}
Black = {
    "color1": [40, 40, 40],
    "color2": [80, 80, 80]
}

# Color mapping dictionary
colorMap = {
    "1": Red, "red": Red,
    "2": Orange, "orange": Orange,
    "3": Yellow, "yellow": Yellow,
    "4": Green, "green": Green,
    "5": Blue, "blue": Blue,
    "6": Violet, "violet": Violet,
    "7": White, "white": White,
    "8": Black, "black": Black
}

def generateBoard(imgSize, cellNum, color1, color2):
    #create blank board
    array = zeros([imgSize, imgSize, 3], dtype = uint8)

    cellSize = imgSize/cellNum
    print(f"Size: {cellSize}")
    for i in range(cellNum):
        for j in range(cellNum):

            yStart  = int(i * cellSize)
            yEnd    = int((i + 1) * cellSize)
            xStart  = int(j * cellSize)
            xEnd    = int((j + 1) * cellSize)

            #array[height,width] = [RGB Value]
            if (i+j) % 2 == 0:  array[yStart:yEnd, xStart:xEnd] = color1
            else:               array[yStart:yEnd, xStart:xEnd] = color2
    img = Image.fromarray(array)
    img.save("imageSlice.png")
    img.show()

def main():
    print('''==========================================
        1 - Generate Default Board
        2 - Create Custom Board

        Any Other Input will exit the Program.
        ''')

    userChoice = input("[Choice]: ")

    if userChoice == "1":
        color1 = [255, 206, 158]
        color2 = [209, 139, 71 ]
        generateBoard(180, 8, color1, color2)
    elif userChoice == "2":
        imgSize = int(input("Enter Size of Image: "))
        cellNum = int(input("Number of Blocks/Cells: "))
        

        print('''
    Colors:
        1 - Red
        2 - Orange
        3 - Yellow
        4 - Green
        5 - Blue
        6 - Violet
        7 - White
        8 - Black
''')    
        userColorTheme = input("Enter Color Theme: ").strip().lower()
        
        if userColorTheme in colorMap:
            selectedColor = colorMap[userColorTheme]
            color1 = selectedColor["color1"]
            color2 = selectedColor["color2"]
        else:
            print("Invalid color choice. Using default (Red).")
            color1 = Red["color1"]
            color2 = Red["color2"]
        
        generateBoard(imgSize, cellNum, color1, color2)
    else:
        print("\n        Good bye!")


main()


