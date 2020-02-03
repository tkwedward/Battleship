import sys
from Board import GameBoard
from Player import Player
from Ship import Ship
from Game import Game

####################
# Load Configuration File
####################
configuration_path = sys.argv[1]

with open(configuration_path) as f:
    try:
        lines = f.readlines()
        board_size = lines[0].replace("\n", "").split(" ")
        ship_data_array = []
        for x in lines[1:]:
            ship_data = x.replace("\n", "").split(" ")
            ship_data[1] = int(ship_data[1])
            ship_data_array.append(tuple(ship_data))
        board1 = GameBoard(board_size)
        board2 = GameBoard(board_size)
    except:
        print("Some error is in the configuration file. Please check the file.")
        sys.exit()


####################
# Create Players and Ships
####################
#

player1_name = input("Player 1 please enter your name: ")
player1 = Player(player1_name, board1)
for shipData in ship_data_array:
    name = shipData[0]
    size = shipData[1]
    player1.shipArray.append(Ship(name, size))
player1.player_place_ship()

while True:
    player2_name = input("Player 2 please enter your name: ")

    if (player1_name == player2_name):
        print("Name is repeated. Please enter a name different from Player 1.")
    else:
        player2 = Player(player2_name, board2)
        for shipData in ship_data_array:
            name = shipData[0]
            size = shipData[1]
            player2.shipArray.append(Ship(name, size))
        player2.player_place_ship()
        break

####################
# Create Game
####################
game = Game(player1, player2, board1, board2)


####################
# Start the game
####################
while True:
    # Player 1's Turn
    Game.player_attack(player1, player2, Game.gameRound)
    endGame = Game.check_end(player2)
    if endGame == "endGame":
        print(f"{player1.name} won the game!")
        break

    # Player 2's Turn
    Game.player_attack(player2, player1, Game.gameRound)
    Game.gameRound += 1
    endGame = Game.check_end(player1)
    if endGame == "endGame":
        print(f"{player2.name} won the game!")
        break

