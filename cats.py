import pets
class Cat(pets.Pet):
    def __init__(self, name, type, tricks, age, color):
        super().__init__(name, type, tricks)
        self.age = age
        self.color = color
        self.health = 0
    def chasing_mice(self,num_of_mice):
        chased_mice = num_of_mice-1
        return chased_mice
    def running_distances(self, num_of_miles):
        return (self.health + num_of_miles)
        
my_cat = Cat("starle", "domestic", "chasingMice", 12, "ash-gold")
print(my_cat.chasing_mice(5))
print(my_cat.running_distances(5))
