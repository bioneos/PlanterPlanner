from flask import Flask, render_template

def create_app():
  # create the app
  app = Flask(__name__)

  # simple hello world page to get the
  # app running
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  @app.route('/')
  def home():
    return render_template('home/index.html')


  return app