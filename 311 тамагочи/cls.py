class Pet:
    def __init__(self, name, hp, food):
        self.name = name
        self.hp = hp
        self.food = food

    def feed(self):
        self.food += 10
        print(self.name, "поел")


x = int(10)
pet = Pet("Вася", 100, 100)
pet.feed()