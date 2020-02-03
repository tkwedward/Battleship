import sys
from Board import GameBoard
from Player import Player
from Ship import Ship
from Game import Game

####################
# Load Configuration File
####################
configuration_path = sys.argv[1]
test = False
test_case = 0
test_fire_input_only = True
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
if test or test_fire_input_only:
    player1_name = "Bob"
else:
    player1_name = input("Player 1 please enter your name: ")
    # player1_name = "Bob"

player1 = Player(player1_name, board1)
for shipData in ship_data_array:
    name = shipData[0]
    size = shipData[1]
    player1.shipArray.append(Ship(name, size))

if test or test_fire_input_only:
    if test_case == 0:
        player1.player_place_ship([["horizontal", "2, 0"], ["horizontal", "0, 0"]])

else:
    # player1.player_place_ship([["horizontal", "2, 0"], ["horizontal", "0, 0"]])
    player1.player_place_ship()

while True:
    if test or test_fire_input_only:
        player2_name = "Sally"
    else:
        # player2_name = "Sally"
        player2_name = input("Player 2 please enter your name: ")

    if (player1_name == player2_name):
        print("Name is repeated. Please enter a name different from Player 1.")
    else:
        player2 = Player(player2_name, board2)
        for shipData in ship_data_array:
            name = shipData[0]
            size = shipData[1]
            player2.shipArray.append(Ship(name, size))

        if test or test_fire_input_only:
            player2.player_place_ship([["vertical", "2,0"], ["horizontal", "4, 2"]])

        else:
            # player2.player_place_ship([["vertical", "2,0"], ["horizontal", "4, 2"]])
            player2.player_place_ship()
        break

####################
# Create Game
####################
game = Game(player1, player2, board1, board2)


####################
# Start the game
####################
if test_case == 0:
    player1_list = ['1, 3', '1, 0', '2, 0', '2, 1', '3, 0', '3, 1', '4, 0', '2, 2', '2, 3', '1, 1', '0, 4', '4, 4',
                    '4, 3', '3, 4', '4, 2', '4, 4', '0, 3', '1, 2', '0, 0', '0, 1', '1, 0', '0, 2', '1, 1', '2, 3',
                    '3, 2', '3, 4', '4, 1', '2, 2', '1, 3']
elif test_case == 1:
    player1_list = ['bob', 'cat', 'you,there', '2, -9', '0, 6 ', '1, 3 ', '1, 0 ', '0, 6', '1, 0', '1, 2', '0, 0', '0, 1', '1, 0',
     '0, 2', '1, 1', '2, 3', '3, 2', '3, 4', '4, 1', '2, 2', '1, 3', '1, 3', '1, 0', '2, 0', '2, 1', '3, 0', '3, 1',
     '4, 0', '2, 2', '2, 3', '1, 1', '0, 4', '4, 4', '4, 3', '3, 4', '4, 2', 'bob', 'cat', 'you,there', '2, -9',
     '0, 6 ', '1, 3 ', '1, 0 ', '0, 6', '1, 0', '1, 2', '0, 0', '0, 1', '1, 0', '0, 2', '1, 1', '2, 3', '3, 2',
     '3, 4', '4, 1', '2, 2', '1, 3', '1, 3', '1, 0', '2, 0', '2, 1', '3, 0', '3, 1', '4, 0', '2, 2', '2, 3', '1, 1',
     '0, 4', '4, 4', '4, 3', '3, 4', '4, 2']

if test_case == 0:
    player2_list = ['4, 4', '0, 3', '1, 2', '0, 0', '0, 1', '1, 0', '0, 2', '1, 1', '2, 3', '3, 2', '3, 4', '4, 1',
                    '2, 2', '1, 3', '1, 3', '1, 0', '2, 0', '2, 1', '3, 0', '3, 1', '4, 0', '2, 2', '2, 3', '1, 1',
                    '0, 4', '4, 4', '4, 3', '3, 4', '4, 2']
elif test_case == 1:
    player2_list = ['-3, 7', '8', 'cat,man', '8, 9, 10, 54', '3, 4 hello', '5, 5', '4, 4', '0, 3', '1,3', '2, 0', '2, 1', '3, 0',
     '3, 1', '4, 0', '2, 2', '2, 3', '1, 1', '0, 4', '4, 4', '4, 3', '3, 4', '4, 2', '4, 4', '0, 3', '1, 2', '0, 0',
     '0, 1', '1, 0', '0, 2', '1, 1', '2, 3', '3, 2', '3, 4', '4, 1', '2, 2', '1, 3', '-3, 7', '8', 'cat,man',
     '8, 9, 10, 54', '3, 4 hello', '5, 5', '4, 4', '0, 3', '1,3', '2, 0', '2, 1', '3, 0', '3, 1', '4, 0', '2, 2',
     '2, 3', '1, 1', '0, 4', '4, 4', '4, 3', '3, 4', '4, 2', '4, 4', '0, 3', '1, 2', '0, 0', '0, 1', '1, 0', '0, 2',
     '1, 1', '2, 3', '3, 2', '3, 4', '4, 1', '2, 2', '1, 3']


if test:
    for i, (x, y) in enumerate(zip(player1_list, player2_list)):
        print(i, x)
        print(f"{player1.name}, enter the location you want to fire at in the form row, column:")
        Game.player_attack(player1, player2, Game.gameRound, x)
        endGame = Game.check_end(player2)
        if endGame == "endGame":
            print(f"{player1.name} won the game!")
            break

        print(f"{player2.name}, enter the location you want to fire at in the form row, column:")
        Game.player_attack(player2, player1, Game.gameRound, y)
        Game.gameRound += 1
        endGame = Game.check_end(player1)
        if endGame == "endGame":
            print(f"{player2.name} won the game!")
            break
else:
    #
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
    

