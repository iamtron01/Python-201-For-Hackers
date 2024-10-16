import re

class DomainException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

class Name:
    def __init__(self, value: str):
        if not value or not isinstance(value, str):
            raise DomainException("Name cannot be null or empty")
        if not re.match(r'^[a-zA-Z]{1,24}$', value):
            raise DomainException(
                "Name must only contain letters "
                "and be no longer than 24 characters")
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self._value

    def __repr__(self):
        return f"{self._value!r}"

class Age:
    def __init__(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise DomainException("Age must be a non-negative integer")
        self._value = value

    @property
    def value(self):
        return self._value

    def __int__(self):
        return self._value

    def __repr__(self):
        return f"{self._value!r}"
    
    def __add__(self, other):
        return self._value + other._value
    
    def __lt__(self, other):
        return self._value < other._value
    
class Person:
    def __init__(self, name: Name, age: Age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: Name):
        if not value or not isinstance(value, Name):
            raise DomainException("Name cannot be null")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: Age):
        if not value or not isinstance(value, Age):
            raise DomainException("Age cannot be null")
        self._age = value

    def __str__(self):
        return (
            "My name is {} and I'm {} years old"
                .format(self.name, self.age))
    
    def __add__(self, other):
        return self.age + other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
bob = Person(Name("bob"), Age(33))
alice = Person(Name("alice"), Age(25))
print(bob)
print(bob + alice)
print(alice < bob)