
import json

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
    def __init__(self, name, age, attribute):
        super().__init__(name, age)
        self.fur_color = attribute
    def make_sound(self):
        return "Chirp chirp"

    def eat(self):
        return "eats seeds"

    def sleep(self):
        return "sleeps in nest"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Growl growl"

    def eat(self):
        return "ест"

    def sleep(self):
        return "спит в вальере"

class Reptile(Animal):
    def __init__(self, name, age, attribute):
        super().__init__(name, age)
        self.fur_color = attribute
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
        print(animal.sleep())
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def to_json(self):
        return {
            "animals": [animal.__dict__ for animal in self.animals],
            "employees": [(employee[0], employee[1].__class__.__name__) for employee in self.employees]
        }

class ZooKeeper:
    def feed_animal(self, animal):
        return f"Кормил {animal.name}"

class Veterinarian:
    def heal_animal(self, animal):
        return f"Лечил {animal.name}"

def save_zoo(zoo):
    with open('zoo.json', 'w') as file:
        json.dump(zoo.to_json(), file, indent=4)

def load_zoo():
    with open('zoo.json', 'r') as file:
        zoo_data = json.load(file)
        return zoo_data

def main():
    zoo = Zoo()

    while True:
        choice = input("Введите 'Bird', 'Mammal' или 'Reptile' для создания животного (или 'end' для завершения): ")
        if choice == 'end':
            break
        if choice == 'Bird':
            name, age, attribute = input("Введите название, возраст и атрибуты птицы через запятую: ").split(',')
            animal = Bird(name, int(age), attribute)
            zoo.add_animal(animal)
        elif choice == 'Mammal':
            name, age, fur_color = input("Введите название, возраст и цвет шерсти млекопитающего через запятую: ").split(',')
            animal = Mammal(name, int(age), fur_color)
            zoo.add_animal(animal)
        elif choice == 'Reptile':
            name, age, attribute = input("Введите название, возраст и атрибуты рептилии через запятую: ").split(',')
            animal = Reptile(name, int(age), attribute)
            zoo.add_animal(animal)

    while True:
        employee = input("Введите 'ZooKeeper' или 'Veterinarian' для добавления сотрудника (или 'end' для завершения): ")
        if employee == 'end':
            break
        if employee == 'ZooKeeper':
            name = input("Введите имя служащего : ")
            employee = ZooKeeper()
            zoo.add_employee((name, employee))
        elif employee == 'Veterinarian':
            name = input("Введите имя ветеринара: ")
            employee = Veterinarian()
            zoo.add_employee((name, employee))

    save_zoo(zoo)
def interact_with_animal(animal):
    print(animal.make_sound())
    print(animal.eat())
    print(animal.sleep())
if __name__ == "__main__":
    print("Здравствуйте, вы смотритель зоопарка")
    main()