class Ship(object):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        self.health = size
        self.coordinateList = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def return_coordinates(self) -> tuple:
        return self.name, self.coordinateList

