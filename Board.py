import typing
class GameBoard(object):
    def __init__(self, size: typing.Tuple[int, int]) -> None:
        self.horizontal = int(size[1])
        self.vertical = int(size[0])
        self.boardArray = []
        self._createBoard()

    def _createBoard(self) -> None:
        """ To create the game board """
        board_line = self.horizontal * "*"

        # create the boardArray
        self.boardArray.append(board_line)
        self.boardArray *= self.vertical

        # put in coordinates
        for i, y in enumerate(self.boardArray):
            self.boardArray[i] = list(y)
            self.boardArray[i].insert(0, str(i))
        x_coordinate = [str(num) for num in range(0, self.horizontal)]
        x_coordinate.insert(0, " ")
        self.boardArray.insert(0, x_coordinate)

    def _drawBoard(self) -> None:

        max_length = len(max([cell for row in self.boardArray for cell in row], key=lambda x: len(x)))
        for row in self.boardArray:
            row_str = ""
            for col in row:
                row_str += col + (max_length - len(col) + 1) * " "
            print(row_str[0:-1])

    def _placeShip(self, ship: str, direction: str, coordinate: typing.Tuple[int, int], shipArray: typing.List) -> None:
        """
        to place the ship into the board
        1. Check if the ship is out of bound
        2. Check if there if overlap
        :param ship, str: the name of the ship
        :param direction, str: direction of the ship
        :param coordinate, tuple:  coordination of the ship
        :return:
        """
        y = int(coordinate[0]) + 1
        x = int(coordinate[1]) + 1

        try:
            if "horizontal".find(direction) != -1:
                # check if the ship are overlapped
                valid_placement_check = all([self.boardArray[y][col] == "*" for col in range(x, x + ship.size)])
                if valid_placement_check == True:
                    for col in range(x, x + ship.size):
                        self.boardArray[y][col] = ship.name[0] # put the initial into the board
                        ship.coordinateList.append([col-1, y-1])
                    return True
                else:
                    print(shipArray)
                    for _ship in shipArray:
                        print(y-1, x-1)
                        print(_ship.coordinateList)
                        for y in _ship.coordinateList:
                            print((y-1, x-1)==y)

                    print(f"column: Cannot place {ship.name} vertically at 2, 0 because it would overlap with ['P']")

                    return False
        except:
            print(f"Cannot place {ship.name} {direction} at {coordinate[0]}, {coordinate[1]} because it would end up out of bounds..\n")
            return False

        try:
            if "vertical".find(direction) != -1:
                valid_placement_check = all([self.boardArray[row][x] == "*" for row in range(y, y + ship.size)])
                if valid_placement_check == True:
                    for row in range(y, y + ship.size):
                        self.boardArray[row][x] = ship.name[0]
                        ship.coordinateList.append([x - 1, row - 1])
                    return True
                else:
                    print("Invalid placement, there is already a ship there.")
                    return False
        except:
            print(f"Cannot place {ship.name} {direction} at {coordinate[0]}, {coordinate[1]} because it would end up out of bounds.\n")
            return False

    def checkHit(self, coordinate: typing.Tuple[int, int])-> None:
        x = coordinate[0] + 1
        y = coordinate[1] + 1
        if (x <= self.horizontal and y <= self.vertical):
            if (self.boardArray[x][y] == "O" or self.boardArray[x][y] == "X"):
                print("You have already attacked this position")

            else:
                self.boardArray[x][y] = "O"
            # print(self.boardArray)
        self._drawBoard()