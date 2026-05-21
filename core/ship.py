class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.hits = set()

    def register_hit(self, coord):
        if coord in self.coordinates:
            self.hits.add(coord)

    def is_sunk(self):
        return len(self.hits) == len(self.coordinates)

    def remaining_cells(self):
        return len(self.coordinates) - len(self.hits)