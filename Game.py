import copy
from Board import GameBoard

class lengthError(Exception):
    """Raised when the length of the input is not 2."""
    pass

class negativeError(Exception):
    """Raised when the length of the input is not 2."""
    pass

class Game(object):
    gameRound = 1
    gameSymbol = {"miss": "O", "hit": "X"}

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
        allowed_symbol = ["*", "X", "O"]
        masked_map = copy.deepcopy(defender.board.boardArray)
        max_length = len(max([cell for row in masked_map for cell in row], key=lambda x: len(x)))

        # to create a masked map from the defender's board
        print(f"{attacker.name}'s Scanning Board")
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
                row_str += col + (max_length - len(col) + 1) * " "
            print(row_str[0:-1])
        print()


        # to print attacker's board

        print(f"{attacker.name}'s Board")
        for row in attacker.board.boardArray:
            row_str = ""
            for col in row:
                row_str += col + (max_length - len(col) + 1) * " "
            print(row_str[0:-1])
        print()

    @staticmethod
    def player_attack(attacker: "player.Player", defender: "player.Player", round: "int", user_coordinates: tuple = None, symbol: object = gameSymbol)-> None:
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

            if user_coordinates:
                user_input = user_coordinates
            else:
                user_input = input(f"{attacker.name}, enter the location you want to fire at in the form row, column: ")

            try:
                coordinates = user_input.replace(" ", "").split(",")

                if len(coordinates) != 2:
                    raise (lengthError)
                else:
                    x, y = int(coordinates[1]), int(coordinates[0])
                    if x < 0:
                        print(f"col: Col should be non negative. {coordinates[1]} is NOT a positive number.")
                        raise negativeError
                    if y < 0:
                        print(f"row: Row should be non negative. {coordinates[0]} is NOT a positive number.")
                        raise negativeError
            except IndexError:
                print(f"{user_input} is not a valid location.\nEnter the firing location in the form row, column")
                continue
            except lengthError:
                print("The length of the coordinates must be 2.")
                continue

            except AttributeError:
                print(f"-----Your input is not in the format x, y")
                valid_attack = False
                continue
            except negativeError:
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
                    print(f"Miss")
                    Game.draw_board_side_by_side(attacker, defender, round)
                    valid_attack = True

                elif defender.board.boardArray[y+1][x+1] in [symbol["miss"], symbol["hit"]]:
                    # if already fired
                    print(f"You have already fired at {y}, {x}.")
                    valid_attack = False

                else: # the target is hit
                    defender.board.boardArray[y+1][x+1] = symbol["hit"]
                    for ship in defender.shipArray:
                        for c in ship.coordinateList:
                            if c == [x, y]:
                                print(f"You hit {defender.name}'s {ship.name}!")
                                ship.health -= 1
                                if ship.health == 0:
                                    print(f"You destroyed {defender.name}'s {ship.name}")
                                Game.draw_board_side_by_side(attacker, defender, round)
                    valid_attack = True
            except IndexError:
                y_length = len(defender.board.boardArray)
                x_length = len(defender.board.boardArray[0])
                if y_length < y + 1:
                    print("your row entry is out of bound")
                if x_length < x + 1:
                    print("your column entry is out of bound")
                    valid_attack = False
            except UnboundLocalError:
                valid_attack = False


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