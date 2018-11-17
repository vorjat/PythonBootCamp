import pytest
from zjazd_4.Mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b = [
        [7, 8, 9],
        [10, 11, 12]
    ]

    result = add_matrices(a, b)
    assert result == [
        [8, 10, 12],
        [14, 16, 18]
    ]


def test_add_different_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b = [
        [7, 8],
        [10, 11]
    ]

    with pytest.raises(ValueError):
        add_matrices(a, b)

def test_sub_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b = [
        [7, 8, 9],
        [10, 11, 12]
    ]

    result = sub_matrices(a, b)
    assert result == [
        [-6, -6, -6],
        [-6, -6, -6]
    ]


def test_sub_different_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b = [
        [7, 8],
        [10, 11]
    ]

    with pytest.raises(ValueError):
        sub_matrices(a, b)