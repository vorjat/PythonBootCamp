class CashMachine:
    def __init__(self):
        self.bills = []

    def is_available(self):
        if len(self.bills) > 0:
            return True
        else:
            return False

    def show_money(self):
        print(self.bills)

    def put_money(self, new_bills):
        for bill in new_bills:
            if bill == 50 or bill == 100 or bill == 200:
                self.bills.append(bill)

    def withdraw_money(self, amount):
        self.withdrawed = []
        if amount > sum(self.bills):
            print("Not enough money!")
        elif amount % 50 != 0:
            print("Not divisable by 50!")
        else:
            while amount >= 200 and 200 in self.bills:
                amount -= 200
                self.bills.remove(200)
                # print ('poszlo 200!')
                self.withdrawed.append(200)
            while amount >= 100 and 100 in self.bills:
                amount -= 100
                self.bills.remove(100)
                # print('poszlo 100!')
                self.withdrawed.append(100)
            while amount >= 50 and 50 in self.bills:
                amount -= 50
                self.bills.remove(50)
                # print('poszlo 50!')
                self.withdrawed.append(50)
            return (self.withdrawed)


cashMachine = CashMachine()
# print(cashMachine.is_available())
cashMachine.put_money([50, 50, 100, 33, 200, 200, 200, 50, 50, 50, 50, 50, 50, 50])
# print(cashMachine.is_available())
# cashMachine.show_money()
cashMachine.withdraw_money(1000)


def test_cash_machine_withdraw_money():
    cashMachine = CashMachine()
    cashMachine.put_money([200, 100, 100, 50])
    assert cashMachine.withdraw_money(150) == [100, 50]
