# comic_util
Some scripts that help me make comics faster

### join_and_split.py
This script takes all images in ./images, stacks them all on top of each other then splits the composite image by slice size.

After 25 chapters published on [Webtoons](http://www.webtoons.com/en/challenge/a-fools-deception/list?title_no=2758), I got really tired of splitting images over 800x1240 so I made a script that does it for me.

#### Installation/Usage
Install [python](https://www.python.org/downloads/), and [Pillow](http://pillow.readthedocs.io/en/3.1.x/installation.html).

Take a look at the script and change any directories/sizes you need.

run the script  
`python stack.py`

or if you're on windows, just doubleclick the file. If it doesn't work, you might need to add python to your environmental variables.

There are some test images and a psd to play with.

#### //TODO
 - It would be nice to have it also scale images down to a specific width and keep aspect ratio.
 - Use PIL.verify to make sure we're only using valid images.
 - Option to convert incoming images and output images to same mode (RGB RGBA, etc...) Otherwise you get `ValueError: images do not match`  
