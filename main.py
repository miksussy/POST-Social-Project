from flask import Flask, request, render_template
import os
import sys

app = Flask(__name__)

@app.route("/", methods=["POST"])
def rnder():
  f = open("templates/index.html", "wt")
  f.write(str(request.json))
  f.close()
  os.system("python restart.py")
  os.system('kill 1')
  
@app.route("/", methods=["GET"])
def hello():
  return render_template('index.html')

app.run(host='0.0.0.0', port=8080)