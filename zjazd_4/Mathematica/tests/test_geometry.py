from zjazd_4.Mathematica.geometry.figures import square_area, triangle_area

def test_geo():
    assert square_area(3) == 9
    assert triangle_area(2,2) == 2