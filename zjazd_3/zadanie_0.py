class dog():
    def __init__(self):
        self.energy = 10

    def get_energy(self):
        print(self.energy)

    def sleep(self):
        self.energy += 2
        print("ZZzzZZZZzzZZZzz")

    def bark(self):
        if self.energy > 0:
            self.energy -= 1
            print("Szczeku, szczeku")
        else:
            print("brak energii")


piesel = dog()

piesel.bark()
piesel.sleep()
piesel.get_energy()
