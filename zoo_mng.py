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

        try:
            if anm.species not in self.animals:
                self.animals[anm.species] = []
                self.animals[anm.species].append(anm)
            else:
                self.animals[anm.species].append(anm)
        except AttributeError:
            print("The animal you want to add has no object in the animals")

    def get_animals_by_species(self, spc):
        name_list = []
        if spc in self.animals:
            dummy_list = self.animals[spc]
            for items in dummy_list:
                name_list.append(items.name)
            return name_list
        else:
            try:
                raise ValueError("The animal is not found")
            except ValueError as e:
                print(e)

    def remove_animal(self, anm_name):
        count = 0
        for item in self.animals:
            for i in self.animals[item]:
                if i.name == anm_name:
                    count += 1
                    index_i = self.animals[item].index(i)
                    self.animals[item].pop(index_i)
        if not count:
            try:
                raise ValueError(f"{anm_name} animal not found")
            except ValueError as e:
                print(e)


class Mammal(Animal):
    def __init__(self, name, species, age, diet, fur_color):
        super().__init__(name, species, age, diet)
        self.fur_color = fur_color

    def __str__(self):
        return f"{self.name}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, species, age, diet, wing_span):
        super().__init__(name, species, age, diet)
        self.wing_span = wing_span

    def __str__(self):
        return f"{self.name}, Wing Span: {self.wing_span}"


# Create some animals
lion = Mammal(name="Leo", species="Lion", age=5, diet="Carnivore", fur_color="Golden")
eagle = Bird(name="Eddy", species="Eagle", age=3, diet="Carnivore", wing_span=2.5)
zebra = Mammal(name="Zara", species="Zebra", age=2, diet="Herbivore", fur_color="Striped")
shir = Mammal(name="shir", species="Lion", age=5, diet="Carnivore", fur_color="Golden")

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
