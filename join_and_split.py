#!/usr/bin/env python
from PIL import Image
import math
import os

def join_and_split(horiz_cut, image_dir, output_dir):
    maxheight = 0
    maxwidth = 0 # should come out to be 800
    images = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    imagefiles = os.listdir(image_dir)
    for imagefile in imagefiles:
        im = Image.open(image_dir+imagefile);
        width, height = im.size
        maxheight += height
        if width > maxwidth:
            maxwidth = width
        print(imagefile + " (" + str(width)+","+str(height) +")")
        images.append(im)

    print("new image size: (" + str(maxwidth) + ", " + str(maxheight) + ")")

    output = Image.new("RGB", (maxwidth, maxheight))
    currentheight = 0

    # loop through images and paste on output
    for image in images:
        width, height = image.size
        output.paste(image, (0, currentheight))
        currentheight += height

    # output composite image
    output.save(output_dir + "output_full" + ".jpg", quality=95)

    # split composite image
    slices = math.ceil(maxheight/horiz_cut)
    upper = 0
    left = 0

    for i in range(slices):
        top = horiz_cut * i
        # check if we reached the bottom
        if i+1 == slices:
            bottom = maxheight
            output_height = maxheight % horiz_cut
        else:
            bottom = top + horiz_cut
            output_height = horiz_cut
        im = Image.new("RGB", (maxwidth, output_height))
        outputregion = output.crop((0, top, maxwidth, bottom))
        im.paste(outputregion, (0, 0))
        im.save(output_dir + "output_" + str(i) +".jpg", quality=95)

if __name__ == '__main__':
    ## This means...
    #  - read in from the ./images directory
    #  - the resulting images should have height = 1240px or less
    #  - save all the output files to the output directory
    join_and_split(1240, "./images/", "./output/")
