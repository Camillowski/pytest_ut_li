import pytest


@pytest.fixture
def setup_data():
    return "Hello Kamil"


def test_gimme_fixture(setup_data):
    assert setup_data == "Hello Kamil"
