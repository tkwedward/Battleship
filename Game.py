import copy
from Board import GameBoard

def colorSentence(sentence: str, color: str="red") -> str:
    """
    To colorize the output in the console
    :param sentence: the str you want to colorize
    :param color: the color you want to choose, only red and yellow
    :return: the colorized sentence
    """
    if color == "red":
        CRED = '\033[91m'
        CEND = '\033[0m'
    else:
        CRED = '\033[33m'
        CEND = '\033[0m'
    return (CRED +  sentence + CEND)

class lengthError(Exception):
    """Raised when the length of the input is not 2."""
    pass

class Game(object):
    gameRound = 1
    gameSymbol = {"miss": "✖", "hit": "◎"}

    def __init__(self, player1: "player.Player", player2: "player.Player", board1: GameBoard, board2: GameBoard) -> None:
        self.player1 = player1
        self.player2 = player2
        self.player1.board = board1
        self.player2.board = board2

    @staticmethod
    def draw_board_side_by_side(attacker: "player.Player", defender: "player.Player", round: int) -> None:
        """
        To draw the two boards side by side
        :param attacker: attacker player
        :param defender: defender player
        :param round: number of round
        :return: None
        """
        allowed_symbol = ["*", "◎", Game.gameSymbol["miss"]]
        masked_map = copy.deepcopy(defender.board.boardArray)
        max_length = len(max([cell for row in masked_map for cell in row], key=lambda x: len(x)))

        print("=" * 20, f" {attacker.name}'s Round (round {round}) ", "=" * 20)
        # to print attacker's board
        for row in attacker.board.boardArray:
            row_str = ""
            for col in row:
                if col == Game.gameSymbol["miss"]:
                    row_str += colorSentence(col + (max_length - len(col) + 2) * " ")
                elif col == Game.gameSymbol["hit"]:
                    row_str += colorSentence(col + (max_length - len(col) + 2) * " ", "yellow")
                else:
                    row_str += col + (max_length - len(col) + 2) * " "
            print(row_str)
        print(f"attacker: {attacker.name}\n")

        # to create a masked map from the defender's board

        for i, row in enumerate(masked_map):
            for j, cell in enumerate(row):
                if cell in allowed_symbol or cell.isdigit() or cell == " ":
                    pass
                else:
                    masked_map[i][j] = "*"

        # to print out the masked map
        for row1 in masked_map:
            row_str = ""
            for col in row1:
                if col == Game.gameSymbol["miss"]:
                    row_str += colorSentence(col + (max_length - len(col) + 2) * " ")
                elif col == Game.gameSymbol["hit"]:
                    row_str += colorSentence(col + (max_length - len(col) + 2) * " ", "yellow")
                else:
                    row_str += col + (max_length - len(col) + 2) * " "
            print(row_str)
        print(f"defender: {defender.name}\n")

        ship_info = ", ".join(f"{ship.name}: {ship.health}" for ship in attacker.shipArray)
        print(f"{attacker.name}'s ships information [{ship_info}]")

    @staticmethod
    def player_attack(attacker: "player.Player", defender: "player.Player", round: "int", symbol: object = gameSymbol)-> None:
        """
        To allow players attack each other
        :param attacker: the attacker
        :param defender: the defender
        :param round: number of round
        :param symbol: the allowed symbols such as hit and miss
        :return: None
        """
        valid_attack = False

        Game.draw_board_side_by_side(attacker, defender, round)
        while not valid_attack:
            user_input = input(colorSentence(f"Please enter coordinates (in the format: x, y) to attack {defender.name}. "))


            coordinates = user_input.replace(" ", "").split(",")

            try:
                if len(coordinates) != 2:
                    raise (lengthError)
                else:
                    x, y = int(coordinates[0]), int(coordinates[1])
            except IndexError:
                print(f"{user_input} is not a valid location.\nEnter the firing location in the form row, column")
                continue
            except lengthError:
                print("The length of the coordinates must be 2.")
                continue
            except:
                if not coordinates[0].isdigit():
                    print(f"row: Row should be an integer. {coordinates[0]} is NOT an integer.")
                if not coordinates[1].isdigit():
                    print(f"col: Column should be an integer. {coordinates[1]} is NOT an integer.")
                continue

            try:
                if defender.board.boardArray[y+1][x+1] == "*":
                    # if miss
                    defender.board.boardArray[y+1][x+1] = symbol["miss"]
                    Game.draw_board_side_by_side(attacker, defender, round)
                    print(colorSentence(f"Miss. Nothing is at {x}, {y}."))
                    valid_attack = True

                elif defender.board.boardArray[y+1][x+1] in [symbol["miss"], symbol["hit"]]:
                    # if already fired
                    print(colorSentence(f"You have already fired at {x}, {y}."))
                    valid_attack = False

                else: # the target is hit
                    defender.board.boardArray[y+1][x+1] = symbol["hit"]
                    for ship in defender.shipArray:
                        for c in ship.coordinateList:
                            if c == [x, y]:
                                print(colorSentence(f"You hit {defender.name}'s {ship.name} at {x, y}."))
                                ship.health -= 1
                                if ship.health == 0:
                                    print(colorSentence(f"You destroyed {defender.name}'s {ship.name}."))
                    valid_attack = True
            except IndexError:
                y_length = len(defender.board.boardArray)
                x_length = len(defender.board.boardArray[0])
                if y_length < y + 1:
                    print("your y coordinate is out of bound")
                if x_length < x + 1:
                    print("your x coordinate is out of bound")



    @staticmethod
    def check_end(defender: "player.Player") -> str:
        """
        To check if the game end
        :param defender: the defender player
        :return: a str indicating if the game finishes or not.
        """
        endGame = all([ship.health == 0 for ship in defender.shipArray])
        if endGame == True:
            return "endGame"
        else:
            return "continue"