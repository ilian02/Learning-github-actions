from src.person import Person

def test_init():
    person = Person("Ivan", 22)
    assert person.name == "Ivan"
    assert person.age == 22

def test_age_group():
    person = Person("Ivan", 22)
    assert person.age_group() == 'Adult'

    person2 = Person("Ivancho", 8)
    assert person2.age_group() == 'Kid'
