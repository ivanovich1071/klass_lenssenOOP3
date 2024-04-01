class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp chirp"

    def eat(self):
        return "клюет зерно"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Growl growl"

    def eat(self):
        return "ест корм"

class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        return "Hiss hiss"

    def eat(self):
        return "ест насекомых"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

class ZooKeeper:
    def feed_animal(self, animal):
        return f"Feeding {animal.name}"

class Veterinarian:
    def heal_animal(self, animal):
        return f"Healing {animal.name}"

# Пример использования
bird = Bird("тетерев", 2, 10)
mammal = Mammal("медведь", 5, "brown")
reptile = Reptile("Змея", 3, "stripped")

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

animals_in_zoo = zoo.animals
animal_sound(animals_in_zoo)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

for animal in animals_in_zoo:
    print(zookeeper.feed_animal(animal))
    print(veterinarian.heal_animal(animal))