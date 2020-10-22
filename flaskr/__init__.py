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
    plants = ['tomato', 'zucchini', 'rose']
  
    # Read in the data from the .json file
    with current_app.open_resource("data.json", "r") as read_file:
      data = json.load(read_file)

    # Get the plant section list
    plant_selection = []
    new_plant = request.form.getlist('plant_select')
    plant_selection.append(new_plant)

    # return renders the html page at home/index.html
    # home page will return the plant_selection list supplied
    return render_template('home/index.html', plants=plants, data=plant_selection)

  return app

  