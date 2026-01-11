#CS124P Module 1-B Laboratory Exercise
#   1. Allow user to select 10 points in given image.
#      Program shall display/print RGB value of specific pixel of selected points.
#
#   2. Write Program that will dynamically fill a 180x180 RGB image with following details.
#
#   3. Select a digital image and perform 4 gray transforms using default values.
#      Allow each image to undergo Histogram and compare the results accordingly through a short discussion


# ANNOTATION AND PIXEL MANIPULATION
import matplotlib.pyplot
from PIL import Image
from PIL import ImageEnhance
from numpy import *
from pylab import *

img = array(Image.open("popcat.png"))


imshow(img)

