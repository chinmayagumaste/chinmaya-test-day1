import pytest
@pytest.fixture(scope="function")
def pretest11():
    print("Pre work 11 ")
    return "Pass"

@pytest.fixture(scope="module")
def pretest22():
    print("Pre work 22 module ")
    yield
    print("Pre work 22 after yield module ")

def test_iniit1(pretest11,pretest22):
    print("Initial test")
    assert pretest11 == "Pass"
def test_iniit2(pretest11,pretest22):
    print("Initial test 2")