import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self, other):
        if math.sqrt(self.x ** 2 + self.y ** 2) < math.sqrt(other.x ** 2 + other.y ** 2):
            return True
        return False

    def __str__(self):
        return (str(self.x) + " " + str(self.y))

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


def test_plus():
    vector1 = Vector(1, 2)
    vector2 = Vector(2, 1)
    vector3 = vector1 + vector2
    assert vector3 == Vector(3, 3)


def test_min():
    vector1 = Vector(3, 3)
    vector2 = Vector(2, 1)
    vector3 = vector1 - vector2
    assert vector3 == Vector(1, 2)


def test_razy():
    vector1 = Vector(2, 3)
    vector2 = vector1 * 2
    assert vector2 == Vector(4, 6)


def test_mniejszy():
    vector1 = Vector(1, 1)
    vector2 = Vector(5, 5)
    assert vector1 < vector2
    assert not vector2 < vector1


def test_rowny():
    vector1 = Vector(1, 1)
    vector2 = Vector(5, 5)
    vector3 = Vector(1, 1)
    assert vector1 == vector3
    assert not vector2 == vector1
