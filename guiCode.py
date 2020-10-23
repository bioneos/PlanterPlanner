from graphics import *
import requests

def appInstructions(window):
    win = window
    instructions = Text(Point((win.getWidth())//2, (win.getHeight())//12),"Instructions:\n1. Select Planter\n 2. Select Size\n 3. Select Plant\n 4. Select Position\n")
    instructions.draw(win)
    win.getMouse()
    instructions.undraw()


def selectPlanter(window,height,width):   #reformat as while loop for invalid entry, use the Entry class instead of input
    win = window
    flag = False

    shapeMsg = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Is the planter a circle, or rectangle:")
    shapeMsg.draw(win)
    shapeSelect = Entry(Point(width//2, height//8), 20)
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
            incorrectText = Text(Point((win.getWidth())//2, (win.getHeight())//8), "Please enter either 'rectangle' or 'circle'")
            incorrectText.draw(win)
            win.getMouse()
            incorrectText.undraw()
            shapeSelect = Entry(Point(width//2, height//8), 20)
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
        circleSize = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Diameter of planter (inches):")
        circleSize.draw(win)
        sizeSelect = Entry(Point(width//2, height//8), 20)
        sizeSelect.draw(win)
        win.getMouse()
        circleSize.undraw()
        sizeSelect.undraw()
        diameter = int(sizeSelect.getText())

        drawInstruct = Text(Point((win.getWidth())//2, (win.getHeight())//10), "Click where to create your planter (center)")
        drawInstruct.draw(win)

        drawPoint = win.getMouse()
        #add ability to redraw if not satisfied with location
        myCircle = Circle(drawPoint, (diameter//2)*10)  #determine max scale based on window, make drawn shape take up as much window space as possible "zoom"
        myCircle.draw(win)
        

    elif planterChoice == "rectangle":
        recSize = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Length of planter (inches):")
        recSize.draw(win)
        sizeSelect = Entry(Point(width//2, height//8), 10)
        sizeSelect.draw(win)
        win.getMouse()
        recSize.undraw()
        sizeSelect.undraw()
        length = int(sizeSelect.getText())
        recSize = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Width of planter (inches):")
        recSize.draw(win)
        sizeSelect = Entry(Point(width//2, height//8), 10)
        sizeSelect.draw(win)
        win.getMouse()
        width = int(sizeSelect.getText())
        recSize.undraw()
        sizeSelect.undraw()

        drawInstruct = Text(Point((win.getWidth())//2, (win.getHeight())//10), "Click where to create your planter (upperLeft corner)")
        drawInstruct.draw(win)
        drawPoint = win.getMouse()
        drawPointX = drawPoint.getX()
        drawPointY = drawPoint.getY()

        myRectangle = Rectangle(drawPoint, Point((drawPointX + length)*2,(drawPointY + width)*2)) #Point((drawPoint.getX()+length)*10,(drawPoint.getY()+width)*10)
        myRectangle.draw(win)  #needs to be scaled still
    

# function to request the plant names and display them in the window
def listPlants(window):
    # Get the plant names through request
    response = requests.get("http://127.0.0.1:5000/plants")

    # get plant dictionary from json reponse and plant names
    plant_dict = response.json()
    plant_list = plant_dict['plants']

    names = "\n".join(plant_list)
    names_text = Text(Point((window.getWidth())//12, (window.getHeight())//12), names)
    names_text.draw(window)
    window.getMouse()
    names_text.undraw()

# function to select which plants to generate shapes from
# function returns a dictionary based on the request response
def selectPlant(win):
    # make the plant selection message and entry box
    plantMsg = Text(Point((win.getWidth())//2, (win.getHeight())//12), "What plant do you want to draw?")
    plantMsg.draw(win)
    plantSelect = Entry(Point(win.getWidth()//2, win.getHeight()//8), 20)
    plantSelect.draw(win)
    win.getMouse()
    plant = plantSelect.getText()

    # make the request based on the plant name
    response = requests.get("http://127.0.0.1:5000/singleplant", {"plant" : plant})

    return response.json()

# Draw a plant based on the given plant data
def drawPlant(win, plant_data):
    plant_size = int(plant_data['space'])
    drawPoint = win.getMouse()
    plantCircle = Circle(drawPoint, plant_size)
    plantCircle.draw(win)


def mainFunc():
    win = GraphWin("Planter Planner", 960, 540)
    winHeight = win.getHeight()
    winWidth = win.getWidth()
    
    appInstructions(win)
    drawPlanter(win, winHeight, winWidth)
    win.getMouse()
    listPlants(win)
    plant_data = selectPlant(win)
    drawPlant(win, plant_data)
    win.getMouse()

mainFunc()