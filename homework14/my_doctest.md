My doctest file.
testing 1: imports:

    >>> from users_13 import *

testing 2:

    >>> person = Person("", "John", "Doe", 30)
    Traceback (most recent call last):
    ...
    users_13.InvalidNameError: Invalid name: . Name should be a non-empty string.


testing 3:

    >>> person = Person("Alice", "Smith", "Johnson", -5)
    Traceback (most recent call last):
    ...
    users_13.InvalidAgeError: Invalid age: -5. Age should be a positive integer.

testing 4:

    >>> employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
    Traceback (most recent call last):
    ...
    users_13.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.

testing 5-6:

    >>> employee = Employee("Bob", "Johnson", "Brown", 40, 123453)
    >>> print(employee.get_level())
    4
