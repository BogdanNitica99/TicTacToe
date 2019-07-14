from flask import Flask

import tic_tac_toe as TTT

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello"

if __name__ == "__PyToWeb__":
	app.run()