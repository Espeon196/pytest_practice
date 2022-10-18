import pytest


@pytest.fixture
def before_and_after():
    print("BEFORE")
    yield
    print("AFTER")


def test_foo(before_and_after):
    print(before_and_after)
