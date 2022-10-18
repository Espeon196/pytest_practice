import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)

    assert all(fruit.cubed for fruit in fruit_salad.fruit)


@pytest.fixture
def first_entry():
    return 'a'


@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    order.append('b')

    assert order == ["a", "b"]


def test_int(order):
    order.append(2)

    assert order == ["a", 2]


@pytest.fixture
def second_entry():
    return 2


@pytest.fixture
def order_2(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_all(order_2, expected_list):
    order_2.append(3.0)

    assert order_2 == expected_list


@pytest.fixture
def empty():
    return []


@pytest.fixture
def append_first(empty, first_entry):
    return empty.append(first_entry)


def test_string_only(append_first, empty, first_entry):
    assert empty == [first_entry]
