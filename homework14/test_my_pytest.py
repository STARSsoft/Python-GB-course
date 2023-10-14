
import pytest
from  users_13 import *

@pytest.fixture
def Bob():
    Bob=Employee("Bob", "Johnson", "Brown", 40, 123453)
    return Bob


def test_InvalidNameError():
    with pytest.raises(InvalidNameError):
        
        person = Person("", "John", "Doe", 30)

def test_InvalidAgeError():
    with pytest.raises(InvalidAgeError):
        person = Person("Alice", "Smith", "Johnson", -5)
        
def test_InvalidIdError():
    with pytest.raises(InvalidIdError):
        employee = Employee("Bob", "Johnson", "Brown", 40, 12345)                


def test_Check_level(Bob):
    
    assert Bob.get_level()==4,"Неверный Уровень"
    
def test_Check_Birthday(Bob):
    Bob.birthday()
    assert Bob.get_age()==41,"День рожденья не работает"
    
def test_Check_Age(Bob):
    
    assert Bob.get_age()==40,"Неверный возраст"


if __name__ == '__main__':
    pytest.main(['-v'])
    
def run():
    pytest.main(['-v'])
    
