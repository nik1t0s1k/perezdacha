class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def pet_description(self):
        print(f"Питомец: {self.name}, Вид: {self.species}, Возраст: {self.age}")


my_pet = Pet("Барсик", "Кот", 3)

my_pet.pet_description()
