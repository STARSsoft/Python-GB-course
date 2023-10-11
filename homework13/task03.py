'''
В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число). 
Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). 
Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.
'''


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        self._validate_name(last_name)
        self._validate_name(first_name)
        self._validate_name(middle_name)
        self._validate_age(age)
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def _validate_name(self, name):
        if not isinstance(name, str) or name == "":
            raise InvalidNameError(name)

    def _validate_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id_number):
        super().__init__(last_name, first_name, middle_name, age)
        self._validate_id(id_number)
        self.id_number = id_number

    def _validate_id(self, id_number):
        if not isinstance(id_number, int) or id_number <= 0 or len(str(id_number)) != 6:
            raise InvalidIdError(id_number)

    def get_level(self):
        return sum(int(digit) for digit in str(self.id_number)) % 7


class InvalidNameError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Invalid name: {self.val}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Invalid age: {self.val}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Invalid id: {self.val}. Id should be a 6-digit positive integer between 100000 and 999999."


if __name__ == "__main__":
    person = Person("", "John", "Doe", 30)
    person = Person("Alice", "Smith", "Johnson", -5)
    employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.get_age())
