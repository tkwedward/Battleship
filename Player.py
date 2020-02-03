from Board import GameBoard

class Player(object):
    def __init__(self, name: str, board: "Board.GameBoard") -> None:
        self.name = name
        self.shipArray = []
        self.board = board

    def print_ship_array(self) -> None:
        """
        print the ships of the player
        :return:
        """
        print(f"{self.name}'s ship")
        for ship in self.shipArray:
            print(f"{ship}, {ship.size}, {ship.health}")
        print("========================")


    def player_place_ship(self, default_list:list = []) -> None:
        """
        Do the move of the player. Check if its direction and location inputs are valid or not.
        If the values are valid, update the board and then draw the board.
        :param default_list:
        :return:
        """


        for i, ship in enumerate(self.shipArray):
            while True:
                print(f"{self.name}'s Placement Board")
                self.board._drawBoard()
                while True:
                    if default_list: # if a hardcoded list provided
                        print(f"{self.name} enter horizontal or vertical for the orientation of {ship.name} which is {ship.size} long: horizontal")
                        direction = default_list[i][0]
                    else:
                        direction = input(f"{self.name} enter horizontal or vertical for the orientation of {ship.name} which is {ship.size} long: ")
                        direction = direction.lower()

                    direction_len = len(direction)
                    if "horizontal"[0: direction_len] == direction:
                        direction = "horizontal"
                        break
                    elif "vertical"[0: direction_len] == direction:
                        direction = "vertical"
                        break
                    else:
                        print(f"{direction} does not represent an Orientation.")
                        continue


                while True:
                    if default_list:
                        print(
                            f"{self.name}, enter the starting position for your {ship.name} ship ,which is {ship.size} long, in the form row, column:")
                        coordinates = default_list[i][1].replace(" ", "").split(",")
                    else:
                        user_input = input(f"{self.name}, enter the starting position for your {ship.name} ship, which is {ship.size} long, in the form row, column: ")
                        coordinates = user_input.replace(" ", "").split(",")

                    if len(coordinates) != 2:
                        print(f"{user_input} is not in the form x,y.\n")
                        continue
                    elif not coordinates[0].isdigit() or not coordinates[1].isdigit():
                        if not coordinates[0].isdigit():
                            print(f"row: {coordinates[0]} is not a valid value for row.\nIt should be an integer between 0 and {self.board.horizontal - 1}\n")
                        if not coordinates[1].isdigit():
                            print(f"col: {coordinates[1]} is not a valid value for column.\nIt should be an integer between 0 and {self.board.vertical - 1}\n")
                        continue
                    else:
                        break

                valid_placement = self.board._placeShip(ship, direction, coordinates, self.shipArray)
                if (valid_placement):
                    if i == len(self.shipArray)-1:
                        print(f"{self.name}'s Placement Board")
                        self.board._drawBoard()
                    break