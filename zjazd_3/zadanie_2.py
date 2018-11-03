class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.time = 0

    def pay_salary(self):

        if self.time <= 8:
            to_pay = self.time * self.stawka
        else:
            to_pay = (8 * self.stawka) + ((self.time - 8) * (self.stawka * 2))
        self.time = 0
        return to_pay

    def register_time(self, time):
        self.time += time


class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):
        #        temptime = self.time
        #        self.time = 0
        #        if temptime <= 8:
        #            return temptime * self.stawka + self.bonus
        #        else:
        #            return (8 * self.stawka) + ((temptime - 8) * (self.stawka * 2)) + self.bonus
        to_pay = super().pay_salary()
        return to_pay + self.bonus

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


def test4():
    employee = PremiumEmployee("Jan", "Nowak", 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500


def test5():
    employee = PremiumEmployee("Jan", "Nowak", 100.0)
    employee.register_time(3)
    assert employee.pay_salary() == 300
