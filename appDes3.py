from graphics import *

def initializeWindow():
    win = GraphWin("Planter Planner")
    win.setCoords(0,0,100,100)
    win.title = "Planter Planner"
    win.getMouse()
    return win

def appInstructions(window):
    win = window
    instructions = Text(Point((win.getWidth())//2, (win.getHeight())//2),"Instructions:\n1. Select Planter\n 2. Select Size\n 3. Select Plant\n 4. Select Position\n")
    instructions.draw(win)
    win.getMouse()
    instructions.undraw()


def selectPlanter(window,height,width):   #reformat as while loop for invalid entry, use the Entry class instead of input
    win = window
    flag = False

    shapeMsg = Text(Point((win.getWidth())//2, (win.getHeight())//3), "Is the planter a circle, or rectangle:")
    shapeMsg.draw(win)
    shapeSelect = Entry(Point(width//2, height//2), 10)
    shapeSelect.draw(win)
    win.getMouse()
    shape = shapeSelect.getText()
    if (shape == "circle") or (shape == "rectangle"):
        shapeSelect.undraw()
        shapeMsg.undraw()
        flag = True
        return shape
        

    elif flag == False:
        while flag == False:
            shapeSelect.undraw()
            incorrectText = Text(Point((win.getWidth())//2, (win.getHeight())//2), "Please enter either 'rectangle' or 'circle'")
            incorrectText.draw(win)
            win.getMouse()
            incorrectText.undraw()
            shapeSelect = Entry(Point(width//2, height//2), 10)
            shapeSelect.draw(win)
            win.getMouse()
            shape = shapeSelect.getText()
            if (shape == "circle") or (shape == "rectangle"):
                shapeSelect.undraw()
                shapeMsg.undraw()
                flag = True
                return shape
    
    
    

def drawPlanter(window, height, width):
    win = window
    planterChoice = selectPlanter(window, height, width)

    if planterChoice == "circle":
        circleSize = Text(Point((win.getWidth())//2, (win.getHeight())//3), "Diameter of planter (inches):")
        circleSize.draw(win)
        sizeSelect = Entry(Point(width//2, height//2), 10)
        sizeSelect.draw(win)
        win.getMouse()
        diameter = sizeSelect.getText()
        print(diameter)

    elif planterChoice == "rectangle":
        recSize = Text(Point((win.getWidth())//2, (win.getHeight())//3), "Length of planter (inches):")
        recSize.draw(win)
        sizeSelect = Entry(Point(width//2, height//2), 10)
        sizeSelect.draw(win)
        win.getMouse()
        recSize.undraw()
        sizeSelect.undraw()
        length = sizeSelect.getText()
        recSize = Text(Point((win.getWidth())//2, (win.getHeight())//3), "Width of planter (inches):")
        recSize.draw(win)
        sizeSelect = Entry(Point(width//2, height//2), 10)
        sizeSelect.draw(win)
        win.getMouse()
        width = sizeSelect.getText()
        print(length, width)



def mainFunc():
    win = GraphWin("Planter Planner")
    winHeight = win.getHeight()
    winWidth = win.getWidth()
    
    appInstructions(win)
    drawPlanter(win, winHeight, winWidth)
    win.getMouse()

mainFunc()