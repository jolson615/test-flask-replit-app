# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/sendBreakfast', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
      return redirect("/")
    else:
      return request.form

@app.route('/secret')
def secret():
    return "You found the secret route"

