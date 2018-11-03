class ElectricCar:
    def __init__(self, battery):
        self.battery = battery
        self.max_range = battery

    def charge(self):
        self.battery = self.max_range

    def drive(self, units):
        if units <= self.battery:
            self.battery -= units
            return units
        else:
            temp = self.battery
            self.battery = 0
            return temp

def test1():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
