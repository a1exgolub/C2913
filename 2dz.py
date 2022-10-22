import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.sytost = 25
        self.progress = 0
        self.alive = True
    def to_eat(self):
        print("pokyshatc")
        self.sytost += 0.5
        self.progress -= 1
    def to_pospat(self):
        print("pospat")
        self.sytost -= 1
        self.progress += 0.5
    def to_poigrat(self):
        print("poigrat")
        self.sytost -= 1.5
        self.progress += 1
    def is_alive(self):
        if self.progress <= -0.5:
            print("zhirnyy")
            self.alive = False
        elif self.sytost <=0:
            print("umer ot goloda")
            self.alive = False
        elif self.progress >=5:
            print("schastlivay zhizn")
            self.alive = False
    def end_of_day(self):
        print(f"Sytost = {self.sytost}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_pospat()
        elif live_cube == 3:
            self.to_poigrat()
            self.end_of_day()
            self.is_alive()

kot = Cat(name = "Stepan")
for day in range(365):
    if kot.alive == False:
        break
    kot.live(day)
