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
        return "pecks at seeds"

    def sleep(self):
        return "sleeps on a branch"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Growl growl"

    def eat(self):
        return "eats food"

    def sleep(self):
        return "sleeps in a den"

class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        return "Hiss hiss"

    def eat(self):
        return "eats insects"

    def sleep(self):
        return "sleeps in a terrarium"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

bird = Bird("Sparrow", 2, 10)
mammal = Mammal("Bear", 5, "brown")
reptile = Reptile("Snake", 3, "stripped")

animals = [bird, mammal, reptile]
animal_sound(animals)