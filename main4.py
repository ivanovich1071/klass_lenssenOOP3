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
    def make_sound(self):
        return "крук-крукл"

    def eat(self):
        return "ест корм"

    def sleep(self):
        return "спит в вальере"


class Mammal(Animal):
    def make_sound(self):
        return "рычит"

    def eat(self):
        return "ест мясо"

    def sleep(self):
        return "спит в клетке"


class Reptile(Animal):
    def make_sound(self):
        return "шипит"

    def eat(self):
        return "ест корм"

    def sleep(self):
        return "спит в террариуме"


class ZooKeeper:
    def feed_animal(self, animal):
        return f"ZooKeeper кормит {animal.name}"


class Veterinarian:
    def heal_animal(self, animal):
        return f"Veterinarian лечит {animal.name}"


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_txt(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f"{animal.name}, {animal.age}\n")
            for employee in self.employees:
                file.write(f"{employee[0]}, {employee[1]}\n")

    def save_to_json(self, filename):
        data = {
            "animals": [(animal.name, animal.age) for animal in self.animals],
            "employees": [(employee[0], str(employee[1])) for employee in self.employees]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
bear = Mammal("медведь", 5)
lion = Mammal("лев", 7)
eagle = Bird("орел", 3)
ostrich = Bird("страус", 2)
monitor_lizard = Reptile("варан", 4)
crocodile = Reptile("крокодил", 6)
zookeeper1 = ZooKeeper()
zookeeper2 = ZooKeeper()
veterinarian1 = Veterinarian()
veterinarian2 = Veterinarian()

# Создание зоопарка
zoo = Zoo()

# Добавление животных в зоопарк
zoo.add_animal(bear)
zoo.add_animal(lion)
zoo.add_animal(eagle)
zoo.add_animal(ostrich)
zoo.add_animal(monitor_lizard)
zoo.add_animal(crocodile)

# Добавление сотрудников в зоопарк
zoo.add_employee(("Игорь", zookeeper1))
zoo.add_employee(("Дина", zookeeper2))
zoo.add_employee(("Алиса", veterinarian1))
zoo.add_employee(("Егор", veterinarian2))
print("Функции для животных:")
for animal in zoo.animals:
    print(f"{animal.name}: {animal.make_sound()}, {animal.eat()}, {animal.sleep()}")

# Вывод всех функций для сотрудников
print("\nФункции для сотрудников:")

for employee in zoo.employees:
    if isinstance(employee[1], ZooKeeper):
        print(f"{employee[0]} (ZooKeeper): {employee[1].feed_animal(zoo.animals[0])}")
    elif isinstance(employee[1], Veterinarian):
        print(f"{employee[0]} (Veterinarian): {employee[1].heal_animal(zoo.animals[0])}")

zoo.save_to_txt("zoo.txt")
zoo.save_to_json("zoo.json")