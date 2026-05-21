class Ability:
    def __init__(self, name):
        self.name = name
        self.used = False

class Nuke(Ability):
    def __init__(self):
        super().__init__("Nuke")

class Submarine(Ability):
    def __init__(self):
        super().__init__("Submarine")