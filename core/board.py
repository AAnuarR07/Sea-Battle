from core.ship import Ship

class Board:
    EMPTY = "~"
    SHIP = "S"
    HIT = "X"
    MISS = "O"

    def __init__(self, size=10):
        self.size = size
        self.grid = [[self.EMPTY for _ in range(size)] for _ in range(size)]
        self.ships = []

    def is_valid_coordinate(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def can_place_ship(self, coordinates):
        for x, y in coordinates:
            if not self.is_valid_coordinate(x, y):
                return False

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx = x + dx
                    ny = y + dy

                    if self.is_valid_coordinate(nx, ny):
                        if self.grid[nx][ny] == self.SHIP:
                            return False
        return True

    def place_ship(self, start_x, start_y, length, horizontal=True):
        coords = []

        for i in range(length):
            x = start_x
            y = start_y

            if horizontal:
                y += i
            else:
                x += i
            coords.append((x, y))

        if not self.can_place_ship(coords):
            return False

        for x, y in coords:
            self.grid[x][y] = self.SHIP

        self.ships.append(Ship(coords))
        return True

    def receive_shot(self, x, y):
        if not self.is_valid_coordinate(x, y):
            return None

        if self.grid[x][y] in [self.HIT, self.MISS]:
            return None

        if self.grid[x][y] == self.SHIP:
            self.grid[x][y] = self.HIT

            for ship in self.ships:
                if (x, y) in ship.coordinates:
                    ship.register_hit((x, y))
            return "hit"

        self.grid[x][y] = self.MISS
        return "miss"

    def display_public(self):
        print("    " + " ".join(str(i + 1) for i in range(self.size)))

        for i in range(self.size):
            row = []

            for j in range(self.size):
                if self.grid[i][j] == self.SHIP:
                    row.append(self.EMPTY)
                else:
                    row.append(self.grid[i][j])

            print(f"{i + 1:2}  " + " ".join(row))

    def display_private(self):
        print("    " + " ".join(str(i + 1) for i in range(self.size)))

        for i in range(self.size):
            print(f"{i + 1:2}  " + " ".join(self.grid[i]))

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def remaining_ship_cells(self):
        return sum(ship.remaining_cells() for ship in self.ships)