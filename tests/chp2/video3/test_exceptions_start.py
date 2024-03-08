from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as ex:
        Point("Lublin", 455.2, 1111.4)
    assert str(ex.value) == "Invalid value!"
