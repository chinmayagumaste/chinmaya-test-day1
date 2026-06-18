import pytest


@pytest.fixture(scope="module")
def prework():
    print("Pre work")


def test_iniit(prework):
    print("Initial test")


def test_iniit2(prework2):
    print("Initial test 2")
