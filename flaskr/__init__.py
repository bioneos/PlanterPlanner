from flask import Flask, render_template, request, current_app
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
  @app.route('/', methods=['GET'])
  def home():
    # currently manually defining the plants in our "database"
    plants = ['tomato', 'zucchini', 'rose']
  
    # Read in the data from the .json file
    with current_app.open_resource("data.json", "r") as read_file:
      data = json.load(read_file)

    # return renders the html page at home/index.html
    return render_template('home/index.html', plants=plants, data=data)

  return app