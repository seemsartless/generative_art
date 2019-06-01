from random import shuffle, seed

# grid_template - a template for generating a grid of items, adding randomness, etc... 
# As inspired by https://github.com/aaronpenne/generative_art/tree/master/parc_pie

# Written in Python for Processing

# Canvas size
w = 800
h = 600

# Colour palettes 

# https://colorhunt.co/palette/144191
colorhunt144191 = ['#e8e8e8', '#5588a3', '#145374', '#00334e']
colPal = colorhunt144191

def setup():
    size(w, h) # (width, height)
    smooth()
    background(colPal[0])
