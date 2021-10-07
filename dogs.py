
import pets
class Dog(pets.Pet):
    def __init__(self, name, type, tricks, age, height, weight):
        super().__init__(name, type, tricks)
        self.age = age
        self.height = height
        self.weight = weight
        
    # def dog_description(self, name, age):
    #     return f"{self.name} is {self.age} years old"
    def dog_description(self):
        return f"{self.name} is {self.age} years old"
    
    def dog_sound(self,sound):
        return f"{self.name}'s sound is {sound}"

my_dog = Dog("Bob", "canis Familiaris", "sits", 4, 10, 12)

print(my_dog.dog_description())