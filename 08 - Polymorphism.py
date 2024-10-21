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
        return self._value

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

class Cves:
    def __init__(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise DomainException("Cves must be a non-negative integer")
        self._value = value

    @property
    def value(self):
        return self._value

    def __int__(self):
        return self._value

    def __repr__(self):
        return f"{self._value!r}"

class Hacker(Person):
    def __init__(self, name: Name, age: Age, cves: Cves):
        super().__init__(name, age)
        self.cves = cves

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: Name = None):
        if value is None:
            value = Name("Anonymous")
        self._name = value

    @property
    def cves(self):
        return self._cves

    @cves.setter
    def cves(self, value: Cves):
        if not value or not isinstance(value, Cves):
            raise DomainException("Cves cannot be null")
        self._cves = value

bob = Person(Name("Bob"), Age(33))
anonymous = Hacker(None, Age(25), Cves(5))

people = [bob, anonymous]
for person in people:
    print(person.name)
    print(type(person))