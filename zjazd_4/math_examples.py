import math

class Kula:
    def __init__(self, r):
        self.promien = r

    def objetosc(self):
        #V=4/3*pi*R^3.
        return (4/3)*math.pi*math.pow(self.promien,3)

    def pp(self):
        return 4 * math.pi * math.pow(self.promien, 2)


kula = Kula(10)
print(kula.objetosc())
print(kula.pp())