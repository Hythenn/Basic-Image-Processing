#CS124P Module 1-B Laboratory Exercise
#   1. Allow user to select 10 points in given image.
#      Program shall display/print RGB value of specific pixel of selected points.
#
#   2. Write Program that will dynamically fill a 180x180 RGB image with following details.
#
#   3. Select a digital image and perform 4 gray transforms using default values.
#      Allow each image to undergo Histogram and compare the results accordingly through a short discussion


# GRAY TRANSFORM AND HISTOGRAM
from PIL import Image
from numpy import *
from pylab import *

# Load and convert image to grayscale array
img = array(Image.open('popcat.png').convert('L'))

# Define Image Transformations
imgOriginal = img
imgInverted = 50 - img
imgSqueezed = (100.0/255) * img + 100
imgSquared = 255.0 * (img/255.0)**2

images = [imgOriginal, imgInverted, imgSqueezed, imgSquared]
titles = ['Original', 'Inversion (50 - im)', 'Squeezed (100-200)', 'Squared Intensity']


figure(figsize=(12, 10))

for i in range(4):
    # Transformed Images
    subplot(4, 2, 2*i + 1)
    imshow(images[i])
    title(titles[i])
    gray()
    axis('off')

    # HISTOGRAM
    subplot(4, 2, 2*i + 2)
    hist(images[i].flatten(), 128)
    title(f'Histogram: {titles[i]}')

tight_layout()
show()