# meet.google.com/rsu-otrg-adm 
from replit import web
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/game/")
def game():
  return render_template('game.html')

@app.route("/about/")
def about():
  return render_template('aboutus.html')

web.run(app)
