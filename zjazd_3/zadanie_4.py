class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity):
        basket_entry = BasketEntry(product, quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        sum_all = 0
        for e in self.entries:
            sum_all += e.count_price()
        return sum_all

    def generate_report(self):
        # print("Produkty w koszyku:")
        # sum_all = 0
        # for e in self.entries:
        #     print(f"- {e.product.name}({e.product.ID}), cena: {e.product.price} x {e.quantity}")
        #     sum_all += e.count_price()
        # print(f"W sumie: {sum_all}")

        finaltext = "Produkty w koszyku:\n"
        sum_all = 0
        for e in self.entries:
            finaltext = finaltext + f"- {e.product.name}({e.product.ID}), cena: {e.product.price} x {e.quantity}\n"
            sum_all += e.count_price()
        finaltext = finaltext + f"W sumie: {sum_all}"

        return finaltext


class Product:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity

basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
basket.generate_report()




def test_add_product():
    basket = Basket()
    product = Product(1, 'Woda', 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1


def test_basket_count_total_price():
    basket = Basket()
    product = Product(1, 'Woda', 10)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50

def test_basket_generate_report():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.generate_report() == """Produkty w koszyku:
- Woda(1), cena: 10.0 x 5
W sumie: 50.0"""