from scripts.chp2.video4.mapmaker_challenge import Point, Map
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp.value) == "Invalid latitude, longitude combination."


def test_cityname_is_string():
    with pytest.raises(TypeError) as exp:
        Point(1234, 44.44, 55.55)
    assert str(exp.value) == "Invalid type! Provide string"
    """
    Your solution here! You will need to edit the following source code
    file to get your test running:

        File path:
        scripts/chp2/video4/mapmaker_challenge import

    It has already been imported for you on the first line of this file
    """


def test_map_has_created_points():
    poland = Map("Polska")
    p1 = Point("Dakar", 14.7167, 17.4677)
    poland.add_point(Point("Dakar", 14.7167, 17.4677))
    assert p1 in poland.get_points()


def test_map_has_only_unique_points():
    poland = Map("Polska")
    poland.add_point(Point("Dakar", 14.7167, 17.4677))
    poland.add_point(Point("Senegal", 79.6937, -169.44406))
    with pytest.raises(ValueError) as exp:
        poland.add_point(Point("Dakar", 14.7167, 17.4677))
    assert str(exp.value) == "Point already exists!"


def test_map_has_only_appended_points():
    poland = Map("Polska")
    poland.add_point(Point("Dakar", 14.7167, 17.4677))
    assert Point("Senegal", 79.6937, -169.44406) not in poland.get_points()
