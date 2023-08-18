# convert image to csv where each pixel is a column
# and each row is a different image

import numpy as np
import pandas as pd
from PIL import Image
import os
import sys

# get the path of the image
path = sys.argv[1]

# get the name of the image
name = os.path.basename(path)

# open the image
img = Image.open(path)

# convert the image to a numpy array
imgArray = np.array(img)

# get the shape of the image
shape = imgArray.shape

# get the number of rows
rows = shape[0]

# get the number of columns
cols = shape[1]

# get the number of channels
channels = shape[2]

# get the number of pixels
pixels = rows * cols
print("pixels: ", pixels)

# create a list of the pixel values
pixelList = []
for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            pixelList.append(imgArray[i][j][k])

# print("pixelList: ", pixelList)

# create a dataframe from the pixel list
df = pd.DataFrame()

columns = []
for i in range(pixels):
    columns.append("pixel" + str(i))

print("columns: ", columns)

df = pd.DataFrame([pixelList], columns=columns)
print("df: ", df.head())