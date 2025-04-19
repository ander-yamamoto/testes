import pytest
from beings import Person


@pytest.fixture()
def person():
    return Person("John Doe", 30, jobs=["Engineer"])


def test_init(person: Person):

    assert person.name == "John Doe"
    assert person.age == 30
    assert person.jobs == ["Engineer"]


def test_forename(person: Person):
    assert person.forename == "John"

def test_surname(person: Person):
    assert person.surname == "Doe"

def test_no_surname(person: Person):
    person.name = "John"
    assert not person.surname

def test_cebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 31

def test_add_job(person: Person):
    person.add_job("Manager")
    assert person.jobs == ["Engineer", "Manager"]
