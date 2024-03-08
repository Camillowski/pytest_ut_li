from scripts.chp2.video2.mapmaker_start import Point
import pytest

def test_make_one_point():
    p1 = Point("Dakar", 14.7161, 17.4677)
    assert p1.get_lat_long() == (14.7161, 17.4677)

def test_invalid_point_generation():
    with pytest.raises(Exception) as exc:
        p1 = Point("Lublin", 23.333, -555.87)