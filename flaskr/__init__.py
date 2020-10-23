from flask import Flask, render_template, request, current_app, url_for
import json

def create_app():
  # create the app
  app = Flask(__name__)

  # simple hello world page to get the
  # app running
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  # app for the main homepage for the user
  # to select the plants that they have
  @app.route('/', methods=['GET', 'POST'])
  def home():
    # currently manually defining the plants in our "database"
    plants = ['tomato', 'zucchini', 'rose', 'lettuce', 'calla lily']
  
    # Read in the data from the .json file
    with current_app.open_resource("data.json", "r") as read_file:
      data = json.load(read_file)

    plant_data = data['plant']
    # Get the plant section list
    plant_selection = request.form.getlist('plant_select')

    # loop through the plants to get the required space
    spaces = []
    for plant in plant_selection:
      curr_dict = next(item for item in plant_data if item["name"] == plant)
      spaces.append(curr_dict["space"])

    # return renders the html page at home/index.html
    # home page will return the plant_selection list supplied
    return render_template('home/index.html', plants=plants, data=plant_selection, sizes=spaces)

  @app.route('/plants')
  def plants():
    # currently manually defining the plants from our "database"
    plants = {"plants" : ['tomato', 'zucchini', 'rose', 'lettuce', 'calla lily']}
    return plants

  @app.route('/plantdata')
  def plantdata():
    # This location just returns the full dictionary that
    # contains all plant data from our database
    with current_app.open_resource("data.json", "r") as read_file:
      data = json.load(read_file)
     
    return data

  return app

  