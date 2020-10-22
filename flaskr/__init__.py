from flask import Flask, render_template, request

def create_app():
  # create the app
  app = Flask(__name__)

  # simple hello world page to get the
  # app running
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  @app.route('/', methods=['GET'])
  def home():
    plants = ['tomato', 'zucchini', 'rose']
    return render_template('home/index.html', plants=plants)

  return app