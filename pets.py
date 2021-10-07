
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy +=5
        self.health +=5
    def play(self):
        self.health +=5
    def noise(self):
        print("this is the pet's noise")
print(__name__)

