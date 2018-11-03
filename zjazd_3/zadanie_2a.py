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
        print(f"Pracownik {self.imie} {self.nazwisko} dostaje zapłaty: {to_pay}")
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
        to_pay = super().pay_salary()
        return to_pay + self.bonus


class Company:
    def __init__(self, name, employee_list):
        self.name = name
        self.employee_list = set()

    def add_employee(self, employee):
        self.employee_list.add(employee)

    def list_employees(self):
        print(self.employee_list)

    def pay_all_salary(self):
        sum_all = 0
        for employee in self.employee_list:
            sum_all += Employee.pay_salary(employee)
        return sum_all


    def size(self):
        return len(self.employee_list)


JanNowak = Employee('Jan', 'Nowak', 100.0)
JanNowak.register_time(10)

ZbychKowalski = Employee('Zbych', 'Kowalski', 105.0)
ZbychKowalski.register_time(8)

Company1 = Company("Company1", "")
#print (Company1.size())
Company1.add_employee(JanNowak)
Company1.add_employee(ZbychKowalski)
#print (Company1.size())
# Company1.list_employees()
Company1.pay_all_salary()
print("---------------Druga tura-----------------")
Company1.pay_all_salary()


def test_company():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google = Company("google", "")
    google.add_employee(employee)
    assert google.size() == 1
    assert google.pay_all_salary() == 500
    assert google.pay_all_salary() == 0
    employee2 = Employee("Krzysztof", "Nowak", 200.0)
    employee2.register_time(5)
    employee.register_time(10)
    google.add_employee(employee2)
    assert google.pay_all_salary() == 2200
