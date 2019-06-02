from random import shuffle, seed

# grid_template - a template for generating a grid of items, adding randomness, etc... 
# As inspired by https://github.com/aaronpenne/generative_art/tree/master/parc_pie

# Written in Python for Processing

debugShowGrid = False

# Canvas and grid size
w = 800
h = 600
colCount = 9
rowCount = 5

# Calculate the dimensions of the cell
cellWidth = w / colCount
cellHeight = h / rowCount
    
print("A cell is: " + str(cellWidth) + " by " + str(cellHeight) )
 
# Colour palettes 

# https://colorhunt.co/palette/144191
colorhunt144191 = ['#e8e8e8', '#5588a3', '#145374', '#00334e']

# https://colorhunt.co/palette/145468
colorhunt145468 = ['#22eaca', '#b31e6f', '#ee5a5a', '#ff9e74']


colPal = colorhunt145468


def setup():
    size(w, h)
    smooth()
    background(colPal[0])
    if debugShowGrid == True:
        stroke(200,0,0)
        for iRows in range(rowCount):
            line(0,iRows * cellHeight, w, iRows * cellHeight)
        for iCols in range(colCount):
            line(iCols*cellWidth,0, iCols*cellWidth, h)
    
   
def draw():
    for iRows in range(rowCount):
        print("In the loop at iRows = " + str(iRows) )
        for iCols in range(colCount):            
            drawCell(iCols, iRows) # Draw this cell
            translate(cellWidth,0) # Move the origin right for the next cell

        # Back to the far left side and down a row
        translate(-cellWidth*colCount,cellHeight)

    noLoop() 
        
def drawCell(iC, iR):
    # Draw the perfect circles in one colour, random for the others
    if iC == iR:
        fill(colPal[1])
    else:
        fill(colPal[int(random(2,3))])
    
    stroke(colPal[int(random(1,3))])
    ellipse(cellWidth/2, cellHeight/2,10+iR*10,10+iC*10)   
        
    
        
