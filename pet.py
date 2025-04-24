class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10

    def sleep(self):
        self.energy += 5
        if self.energy > 10:
            self.energy = 10

    def play(self):
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1

        if self.energy < 0:
            self.energy = 0
        if self.happiness > 10:
            self.happiness = 10
        if self.hunger > 10:
            self.hunger = 10

    def get_status(self):
        print("Pet Name:", self.name)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        print("Learned Tricks:")
        for trick in self.tricks:
            print("-", trick)