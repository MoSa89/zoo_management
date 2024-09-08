class Animal:
    def __init__(self, name, species, age, diet):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    def __str__(self):
        return f"{self.name} the {self.species}, {self.age} years old, Diet: {self.diet}"


class Zoo:
    def __init__(self):
        self.animals = {}

    def add_animal(self, anm):
        if not isinstance(anm, Animal):
            raise ValueError(f"{anm} is not an instance of Animals")
        else:
            if anm.species not in self.animals:
                self.animals[anm.species] = []
            self.animals[anm.species].append(anm)

    def get_animals_by_species(self, spc):
        if spc in self.animals:
            return [animal.name for animal in self.animals[spc]]
        else:
            raise ValueError(f"The animal or the species is not found{spc})")

    def remove_animal(self, anm_name):
        for spec,animal_list in self.animals.items():
            for i, animal in enumerate(animal_list):
                if anm_name == animal.name:
                    del self.animals[spec][i]
                    return
        raise ValueError(f"This animal {anm_name} not found to remove")


class Mammal(Animal):
    def __init__(self, name, species, age, diet, fur_color):
        super().__init__(name, species, age, diet)
        self.fur_color = fur_color

    def __str__(self):
        return f"{super().__str__()}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, species, age, diet, wing_span):
        super().__init__(name, species, age, diet)
        self.wing_span = wing_span

    def __str__(self):
        return f"{super().__str__()}, Wing Span: {self.wing_span}"


# Create some animals
lion = Mammal(name="Leo", species="Lion", age=5, diet="Carnivore", fur_color="Golden")
eagle = Bird(name="Eddy", species="Eagle", age=3, diet="Carnivore", wing_span=2.5)
zebra = Mammal(name="Zara", species="Zebra", age=2, diet="Herbivore", fur_color="Striped")
shir = Mammal(name="shir", species="Lion", age=5, diet="Carnivore", fur_color="Golden")

print(shir)
# Create a zoo and add animals to it
zoo = Zoo()
zoo.add_animal(lion)
zoo.add_animal(eagle)
zoo.add_animal(zebra)
zoo.add_animal(shir)


# Attempt to get animals by species
try:
    lions = zoo.get_animals_by_species("Lion")
    print("Lions in the zoo:", lions)
except ValueError as e:
    print(e)


# Attempt to remove an animal
try:
    zoo.remove_animal("Eddy")
except ValueError as e:
    print(e)

# Try removing an animal that doesn't exist
try:
    zoo.remove_animal("NonExistentAnimal")
except ValueError as e:
    print(e)

# Try adding an object that isn't an animal
try:
    zoo.add_animal("NotAnAnimal")
except ValueError as e:
    print(e)


