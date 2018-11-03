class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.time = 0

    def pay_salary(self):
        temptime = self.time
        self.time = 0
        if temptime <= 8:
            return temptime * self.stawka
        else:
            return (8 * self.stawka) + ((temptime - 8) * (self.stawka * 2))

    def register_time(self, time):
        self.time += time


def test1():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.imie == "Jan"
    assert employee.nazwisko == "Nowak"
    assert employee.stawka == 100
    employee.register_time(5)
    assert employee.pay_salary() == 500.0
    assert employee.pay_salary() == 0.0


def test2():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200.0


def test3():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.register_time(5)
    assert employee.pay_salary() == 1200.0
    assert employee.pay_salary() == 0.0
