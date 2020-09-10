''' Exercise #8. Python for Engineers.'''


class Animals:  # father to Vegetarian and Carnivore

    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity

    def __repr__(self):
        return self.name + " v " + str(self.velocity)

    def get_name(self):
        return self.name

    def get_velocity(self):
        return self.velocity

    def fight(self, other):
        if isinstance(self, Vegetarians) and isinstance(other, Plants):
            return True
        if isinstance(self, Carnivore) and isinstance(other, Vegetarians):
            return True
        if isinstance(self, Vegetarians) and isinstance(other, Carnivore):
            return False


class Carnivore(Animals):  # father to Lion and Alligator
    def __init__(self, name, velocity, power):
        Animals.__init__(self, name, velocity)
        self.power = power

    def get_power(self):
        return self.power

    def __repr__(self):
        return Animals.__repr__(self) + " p " + str(self.power)

    def fight(self, other):
        if isinstance(self, Carnivore) and isinstance(other, Carnivore):
            if self.power > other.power:
                return True
            else:
                return False
        return Animals.fight(self, other)


class Lion(Carnivore):
    def __init__(self, velocity, power):
        Carnivore.__init__(self, "Lion", velocity, power)

    def fight(self, other):
        if isinstance(self, Lion) and isinstance(other, Plants):
            raise TypeError("Predators eat meat")
        return Carnivore.fight(self, other)


class Alligator(Carnivore):
    def __init__(self, velocity, power):
        Carnivore.__init__(self, "Alligator", velocity, power)

    def fight(self, other):
        if isinstance(self, Alligator) and isinstance(other, Plants):
            raise ValueError("Predators eat meat")
        return Carnivore.fight(self, other)


class Vegetarians(Animals):  # father to Rabbit and Zebra
    def __init__(self, name, velocity, age):
        Animals.__init__(self, name, velocity)
        self.age = age

    def __repr__(self):
        return Animals.__repr__(self) + " a " + str(self.age)

    def get_age(self):
        return self.age

    def fight(self, other):
        if isinstance(self, Vegetarians) and isinstance(other, Vegetarians):
            if self.age > other.age:
                return True
            else:
                return False
        return Animals.fight(self, other)


class Zebra(Vegetarians):
    def __init__(self, velocity, age):
        Vegetarians.__init__(self, "Zebra", velocity, age)


class Rabbit(Vegetarians):
    def __init__(self, velocity, age):
        Vegetarians.__init__(self, "Rabbit", velocity, age)


class Plants:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name


class Mango(Plants):

    def __init__(self):
        Plants.__init__(self, "Mango")


class Grass(Plants):
    def __init__(self):
        Plants.__init__(self, "Grass")


class Jungle:
    def __init__(self, organisms):
        self.organisms = organisms

    def __getitem__(self, key):
        return self.organisms[key]

    def get_organisms(self):
        return self.organisms

    def get_mean_velocity(self):
        if self.organisms == list():
            return 0.0
        number_of_animals = 0.0
        sum_velocities = 0.0
        for i in self.organisms:
            if hasattr(i, "velocity"):
                number_of_animals += 1
                sum_velocities += i.velocity
        return sum_velocities/float(number_of_animals)

    def get_predators(self):
        predators = list()
        for animal in self.organisms:
            if isinstance(animal, Carnivore):
                predators.append(animal)
        return sorted(predators, key=Carnivore.get_power, reverse=True)

    def run_fight(self, first, second):
        if isinstance(self.organisms[first], Plants) and isinstance(self.organisms[second], Plants):
            return None
        if isinstance(self.organisms[first], Plants) and isinstance(self.organisms[second], Carnivore):
            return None
        if isinstance(self.organisms[first], Carnivore) and isinstance(self.organisms[second], Plants):
            return None
        if isinstance(self.organisms[first], Plants) and isinstance(self.organisms[second], Vegetarians):
            self.organisms[second].fight(self.organisms[first])
            self.organisms.pop(first)
        elif self.organisms[first].fight(self.organisms[second]):
            self.organisms.pop(second)
        else:
            self.organisms.pop(first)

