var origBoard;
var trn = 1;
const player1='X';
const player2='O';

const cells = document.querySelectorAll('.cell');

startGame();

function startGame() {

	document.getElementById("p1").innerHTML = "Is turn for X";
	document.getElementById("winner").innerHTML = "";

	trn = 1;

	$.ajax({
        url: '/reset',
        type: 'POST',
        success: function(response) {
            //console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
	});

	origBoard = Array.from(Array(9).keys());
	for(var i=0;i<cells.length;i++) {
		cells[i].innerText = '';
		cells[i].style.removeProperty('background-color');
		cells[i].addEventListener('click', turnClickPlayer, false);
	}
}

function turnClickPlayer(square) {
	if(origBoard[square.target.id] === 'X' || origBoard[square.target.id] === 'O') {
		return;
	}	
	if(trn > 0) {
		turnPlayer(square.target.id, player1);
		document.getElementById("p1").innerHTML = "Is turn for O";
		trn = -trn;	
	}
	else {
		turnPlayer(square.target.id, player2);
		document.getElementById("p1").innerHTML = "Is turn for X";
		trn = -trn;
	}

	$(function () {

		$.ajax({
			type: 'GET',
			url: '/winner',
			success: function(data) {
				//console.log('success', data);
				gameOver(data);
			}
		})
	})	
}

function gameOver(value) {
	var winner = value.winner;
	if(winner == 'X' || winner == 'O' || winner == 'Draw'){
		stopGame();
		if(winner == 'X') {
			document.getElementById("winner").innerHTML = "The winner is Player1 (X)";
		}
		if(winner == 'O') {
			document.getElementById("winner").innerHTML = "The winner is Player2 (O)";
		}
		if(winner == 'Draw') {
			document.getElementById("winner").innerHTML = "Nobody wins. Its a DRAW";
		}
	}
}

function stopGame() {
	for(var i=0;i<cells.length;i++) {
		cells[i].removeEventListener('click', turnClickPlayer, false);
	}
}

function turnPlayer(squareId, player) {
	//Marcheaza mapa creeaza obiectul si il trimite serverului
	origBoard[squareId] = player;
	document.getElementById(squareId).innerText = player;
	
	var object = [squareId, player];

    $.ajax({
        url: '/singlePlayer',
        data: JSON.stringify(object),
        contentType: 'application/json;charset=UTF-8',
        type: 'POST',
        success: function(response) {
            //console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
	});
}
