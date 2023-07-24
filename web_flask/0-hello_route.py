#!/usr/bin/env python3
from flask import Flask
# script for starting flask on port 5000


app = Flask(__name__)

app.route("/", strict_slashes=False)
def hello_hbnb():
   """root home function"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
