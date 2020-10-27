from graphics import *
import requests

#Author: KodyPetersen
#Input/output: input is the window being drawn to; no return value/output
#Function: displays basic instructions/app flow; clicking the mouse progresses the app
#TODO: make more thorough intructions, carry through numbered theme, explore progression without clicking
def app_instructions(window):  
  win = window
  instructions = Text(Point((win.getWidth())//2, (win.getHeight())//12),"Instructions:\n1. Select Planter\n 2. Select Size\n 3. Select Plant\n 4. Select Position\n")
  instructions.draw(win)
  win.getMouse()
  instructions.undraw()

#Author: KodyPetersen
#Input/output: takes the window being drawn to, as well as that windows size parameters; returns shape selected
#Function: allows user to type their planter shape (circle or rectangle), not allowing them to progress until it is a supported option
def select_planter(window,height,width):  
  win = window
  flag = False

  #draw instructions and a text entry box for user to type their selected shape
  shape_msg = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Is the planter a circle, or rectangle:")
  shape_msg.draw(win)
  shape_select = Entry(Point(width//2, height//8), 20)
  shape_select.draw(win)
  win.getMouse()
  shape = shape_select.getText()

  #determine if user entered value was valid, if not re-ask them for a valid entry, otherwise return the selection
  if (shape == "circle") or (shape == "rectangle"):
    shape_select.undraw()
    shape_msg.undraw()
    flag = True
    return shape
  
  while flag == False:
    shape_select.undraw()
    incorrect_text = Text(Point((win.getWidth())//2, (win.getHeight())//8), "Please enter either 'rectangle' or 'circle'")
    incorrect_text.draw(win)
    win.getMouse()
    incorrect_text.undraw()
    shape_select = Entry(Point(width//2, height//8), 20)
    shape_select.draw(win)
    win.getMouse()
    shape = shape_select.getText()

    if (shape == "circle") or (shape == "rectangle"):
      shape_select.undraw()
      shape_msg.undraw()
      flag = True
      return shape

#Author: KodyPetersen
#Input/Output: window to draw into and it's size params; no output
#Function: the user enters the relevant size parameters of their shape and it is then drawn to the window
#based on where the user clicks; they can then reposition the shape if it isn't in a position they like
#TODO: currently rectangle shaped planters seem to draw irregularly, possibly based on window coord system 
# or the way the Rectangle object is determining corner positions
def draw_planter(window, height, width):  
  win = window                         
  flag = False
  #calls select_planter within to get the shape choice
  planter_choice = select_planter(window, height, width)

  #depending on shape selected, begin instructions and drawing process for either circle or rectangle shapes
  if planter_choice == "circle":
    #present size param instructions and text entry for entering
    #TODO limit valid entries to only numbers
    circle_size = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Diameter of planter (inches):")
    circle_size.draw(win)
    size_select = Entry(Point(width//2, height//8), 20)
    size_select.draw(win)
    win.getMouse()
    circle_size.undraw()
    size_select.undraw()
    diameter = int(size_select.getText())
    draw_instruct = Text(Point((win.getWidth())//2, (win.getHeight())//10), "Click where to create your planter (center)")
    draw_instruct.draw(win)
    draw_point = win.getMouse()

    #draw circle based on entered params
    my_circle = Circle(draw_point, (diameter//2)*10)
    my_circle.draw(win)
    draw_instruct.undraw()

    #until user is happy with position of drawn planter, allow them to redraw the planter
    confirm_placement = Text(Point((win.getWidth())//2, (win.getHeight())//10), "Press 'y' if you like the position of the planter, 'n' to reposition")
    confirm_placement.draw(win)
    circle_confirm = win.getKey()
    while circle_confirm != "y":
      confirm_placement.undraw()
      draw_instruct.draw(win)
      my_circle.undraw()
      draw_point = win.getMouse()
      draw_instruct.undraw()
      my_circle = Circle(draw_point, (diameter//2)*10)
      my_circle.draw(win)
      confirm_placement.draw(win)
      circle_confirm = win.getKey()
      
      if circle_confirm == 'y':
        confirm_placement.undraw()
        
  elif planter_choice == "rectangle":
    #instruct and allow entry of size params
    rectangle_size = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Length of planter (inches):")
    rectangle_size.draw(win)
    size_select = Entry(Point(width//2, height//8), 10)
    size_select.draw(win)
    win.getMouse()
    rectangle_size.undraw()
    size_select.undraw()
    length = int(size_select.getText())
    rectangle_size = Text(Point((win.getWidth())//2, (win.getHeight())//12), "Width of planter (inches):")
    rectangle_size.draw(win)
    size_select = Entry(Point(width//2, height//8), 10)
    size_select.draw(win)
    win.getMouse()
    width = int(size_select.getText())
    rectangle_size.undraw()
    size_select.undraw()

    #draw the rectangle
    draw_instruct = Text(Point((win.getWidth())//2, (win.getHeight())//10), "Click where to create your planter (upperLeft corner)")
    draw_instruct.draw(win)
    draw_point = win.getMouse()
    draw_pointX = draw_point.getX()
    draw_pointY = draw_point.getY()
    my_rectangle = Rectangle(draw_point, Point((draw_pointX + length)*2,(draw_pointY + width)*2))
    my_rectangle.draw(win)  
    draw_instruct.undraw()

    #allow repositioning of rectangle until user is satisfied
    confirm_placement = Text(Point((win.getWidth())//2, (win.getHeight())//10), "Press 'y' if you like the position of the planter, 'n' to reposition")
    confirm_placement.draw(win)
    rectangle_confirm = win.getKey()
    while rectangle_confirm != "y":
      confirm_placement.undraw()
      draw_instruct.draw(win)
      my_rectangle.undraw()
      draw_point = win.getMouse()
      draw_instruct.undraw()
      my_rectangle = Rectangle(draw_point, Point((draw_pointX + length)*2,(draw_pointY + width)*2))
      my_rectangle.draw(win)
      confirm_placement.draw(win)
      rectangle_confirm = win.getKey()
      if rectangle_confirm == 'y':
        confirm_placement.undraw()


    
#Author: JoeyCicchese
#Input/Output: window drawn to; N/A
#Function: request the plant names and display them in the window
def list_plants(window):
  win = window
  # Get the plant names through request
  response = requests.get("http://127.0.0.1:5000/plants")

  # get plant dictionary from json reponse and plant names
  plant_dict = response.json()
  plant_list = plant_dict['plants']

  names = "\n".join(plant_list)
  names_text = Text(Point((win.getWidth())//12, (win.getHeight())//12), names)
  names_text.draw(win)
  win.getMouse()
  names_text.undraw()

#Author: JoeyCicchese
#Input/Output: window drawn to; N/A
#Function: select which plants to generate shapes from list of plants and
#returns a dictionary based on the request response
def select_plant(window):
  win = window
  # make the plant selection message and entry box
  plant_msg = Text(Point((win.getWidth())//2, (win.getHeight())//12), "What plant do you want to draw?")
  plant_msg.draw(win)
  plant_select = Entry(Point(win.getWidth()//2, win.getHeight()//8), 20)
  plant_select.draw(win)
  win.getMouse()
  plant = plant_select.getText()

  # make the request based on the plant name
  response = requests.get("http://127.0.0.1:5000/singleplant", {"plant" : plant})

  return response.json()

#Author: JoeyCicchese
#Input/Output: window drawn to and selected plants data; N/A
#Function: Draw a plant based on the given plant data
def draw_plant(win, plant_data):
  plant_size = int(plant_data['space'])
  draw_point = win.getMouse()
  plantCircle = Circle(draw_point, plant_size)
  plantCircle.draw(win)

#Author: KodyPetersen
#Input/Output: N/A; outputs GUI window element
#Function: creates window drawn into by other functions; calls those functions in order of app workflow
def mainFunc():
  win = GraphWin("Planter Planner", 960, 540)
  winHeight = win.getHeight()
  winWidth = win.getWidth()
    
  app_instructions(win)
  draw_planter(win, winHeight, winWidth)
  win.getMouse()
  list_plants(win)
  plant_data = select_plant(win)
  draw_plant(win, plant_data)
  win.getMouse()

mainFunc()