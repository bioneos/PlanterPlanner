from flask import Flask, render_template, request, current_app, url_for
import json

def create_app():
  # create the app
  app = Flask(__name__)

  # route to return all plant names
  @app.route('/plants')
  def plants():
    # currently manually defining the plants from our "database"
    plants = {"plants" : ['tomato', 'zucchini', 'rose', 'lettuce', 'calla lily']}
    return plants

  # route to return all plant data
  @app.route('/plantdata')
  def plantdata():
    # This location just returns the full dictionary that
    # contains all plant data from our database
    data = readPlantData()
     
    return data

  # route the handle requests with the query for
  # data on a single plant
  @app.route('/singleplant', methods=["GET"])
  def singleplant():
    # get the query information from the request
    plant_name = request.args.get('plant')

    data = readPlantData()
    plant_data = data['plant']
    
    # find the plant information matching the query
    plant_dict = next(item for item in plant_data if item["name"] == plant_name)

    return plant_dict

  # This function acts as our "fake database" call
  # It reads in the plant data from the manually generated data.json file
  def readPlantData():
    with current_app.open_resource("data.json", "r") as read_file:
      data = json.load(read_file)

    return data

  return app

  