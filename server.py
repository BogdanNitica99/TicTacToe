from flask import Flask, render_template, request, jsonify, redirect, url_for, json
import tictactoe as ttt

app = Flask(__name__)

is_game_over = False
player_winner = 'None'

# Here you choose sP or mP and then redirect you to the corect page
@app.route('/', methods=["GET", "POST"])
def index():

    # if the user clicks on one of the button I recive the game_mode through a
    # POST method
    if request.method == 'POST':

        game_mode = request.get_json()

        if str(game_mode) == "['singlePlayer']":
            return redirect(url_for('singlePlayer'))
        elif str(game_mode) == "['multiPlayer']":
            return redirect(url_for('multiPlayer'))
    else:
        return render_template('index.html')

# SinglePlyaer game_mode - Player vs Player
@app.route('/singlePlayer', methods=["GET", "POST"])
def singlePlayer():

    global is_game_over
    global player_winner

    # if the user clicks on a tile, it generates a POST method
    if request.method == "POST":
        # cell_id from the JavaScript
        cell_id = request.get_json()
        # I send the cell_id to the python code, and i recive if the game is
        # over and who is the winner
        (is_game_over, player_winner) = ttt.game_mode_web1(
            cell_id[0], cell_id[1])

    return render_template('tictactoe.html')


@app.route('/multiPlayer', methods=["GET", "POST"])
def multiPlayer():
    global is_game_over
    global player_winner

    if request.method == "POST":

        cell_id = request.get_json()

        (is_game_over, player_winner) = ttt.game_mode_web2(
            cell_id[0], cell_id[1])

    print("Trebuie sa trimit din codul Python catre server pozitia jucata de calculator")

    return render_template('tictactoe.html')


@app.route('/reset', methods=["POST"])
def reset():
    global is_game_over
    global player_winner

    is_game_over = False
    player_winner = 'None'

    ttt.reset_game()

    return render_template('tictactoe.html')


@app.route('/winner', methods=["GET"])
def winner():
    data = {'winner': player_winner}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
