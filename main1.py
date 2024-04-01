class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp chirp"

    def eat(self):
        return "клюет зерно"

    def sleep(self):
        return "спит на ветке"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Growl growl"

    def eat(self):
        return "ест корм"

    def sleep(self):
        return "спит в вальере"

class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        return "Hiss hiss"

    def eat(self):
        return "ест насекомых"

    def sleep(self):
        return "спит в террариуме"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

def animal_eat(animals):
    for animal in animals:
        print(animal.eat())
def animal_sleep(animals):
    for animal in animals:
        print(animal.slip())

bird = Bird("тетерев", 2, 10)
mammal = Mammal("медведь", 5, "brown")
reptile = Reptile("Змея", 3, "stripped")

animals = [bird, mammal, reptile]
animal_sound(animals)
animal_eat(animals)
animal_sleep(animals)