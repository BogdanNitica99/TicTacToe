
from flask import Flask, render_template, request, jsonify, redirect, url_for, json
import tictactoe as ttt

app = Flask(__name__)

isGameOver = False
winner = 'None'

#Here you choose sP or mP and then redirect you to the corect page
@app.route('/', methods = ["GET", "POST"])
def index():

	#if the user clicks on one of the button I recive the gameMode through a POST method
	if request.method == 'POST':

		gameMode = request.get_json()

		if str(gameMode) == "['singlePlayer']":
			return redirect(url_for('singlePlayer'))
		elif str(gameMode) == "['multiPlayer']":
			return redirect(url_for('multiPlayer'))
	else:
		return render_template('index.html')

#SinglePlyaer gamemode - Player vs Player
@app.route('/singlePlayer', methods = ["GET", "POST"])
def singlePlayer():

	global isGameOver
	global winner
	
	#if the user clicks on a tile, it generates a POST method
	if request.method == "POST":
		#cellId from the JavaScript
		cellId = request.get_json()
		#I send the cellID to the python code, and i recive if the game is over and who is the winner
		(isGameOver, winner) = ttt.GameModeFromWeb1(cellId[0], cellId[1])

	return render_template('tictactoe.html')


@app.route('/multiPlayer', methods = ["GET", "POST"])
def multiPlayer():
	global isGameOver
	global winner

	if request.method == "POST":

		cellId = request.get_json()

		(isGameOver, winner) = ttt.GameModeFromWeb2(cellId[0], cellId[1])

	print("Trebuie sa trimit din codul Python catre server pozitia jucata de calculator")

	return render_template('tictactoe.html')


@app.route('/reset', methods = ["POST"])
def reset():
	global isGameOver
	global winner

	isGameOver = False
	winner = 'None'

	ttt.resetGame()

	return render_template('tictactoe.html')

@app.route('/winner', methods = ["GET"])
def winner():
	data = {'winner': winner}
	return jsonify(data)


if __name__ == '__main__':
	app.run()