#!/usr/bin/python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import urllib.request
import urllib.parse
import os

app = Flask(__name__, static_url_path='/static')
Bootstrap(app)

@app.route('/')
def home():
    concaten = ""
    liste = []
    for parent, dnames, fnames in os.walk("files/"):
      for fname in fnames:
        filename = os.path.join(parent, fname)
        liste.append(filename)
    return render_template('index.html', liste=liste)

@app.route('/<path:path>')
def machines(path):
     tableau = []
     with open(path) as f:
       for line in f:
           tableau.append(line)
     return render_template('tableau.html', tableau=tableau)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)

