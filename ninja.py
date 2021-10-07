import pets
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pets.Pet("Burger", "dog", "sit")
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()
# print(__name__)

ninja1 = Ninja("Milo", "Mr.Smith", "sdjhsjhd" "hsjdhjsd", "dhfjdhjf")

ninja1.walk()
ninja1.feed()
ninja1.feed()
ninja1.bathe()
print (ninja1.pet.energy)

print(ninja1.first_name)#"milo"


