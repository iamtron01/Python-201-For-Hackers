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
    def cves(self):
        return self._cves

    @cves.setter
    def cves(self, value: Cves):
        if not value or not isinstance(value, Cves):
            raise DomainException("Cves cannot be null")
        self._cves = value

import unittest

class TestName(unittest.TestCase):
    def test_valid_name(self):
        name = Name("Alice")
        self.assertEqual(name.value, "Alice")

    def test_invalid_name_empty(self):
        with self.assertRaises(DomainException):
            Name("")

    def test_invalid_name_non_string(self):
        with self.assertRaises(DomainException):
            Name(123)

    def test_invalid_name_special_characters(self):
        with self.assertRaises(DomainException):
            Name("Alice123")

    def test_invalid_name_too_long(self):
        with self.assertRaises(DomainException):
            Name("A" * 25)

class TestAge(unittest.TestCase):
    def test_valid_age(self):
        age = Age(25)
        self.assertEqual(age.value, 25)

    def test_invalid_age_negative(self):
        with self.assertRaises(DomainException):
            Age(-1)

    def test_invalid_age_non_integer(self):
        with self.assertRaises(DomainException):
            Age("twenty")

class TestPerson(unittest.TestCase):
    def test_person_creation(self):
        name = Name("Bob")
        age = Age(30)
        person = Person(name, age)
        self.assertEqual(person.name.value, "Bob")
        self.assertEqual(person.age.value, 30)

    def test_person_creation_invalid_name(self):
        with self.assertRaises(DomainException):
            Person(None, Age(30))

    def test_person_creation_invalid_age(self):
        with self.assertRaises(DomainException):
            Person(Name("Bob"), None)

    def test_person_creation_invalid_name_type(self):
        with self.assertRaises(DomainException):
            Person("Bob", Age(30))

    def test_person_creation_invalid_age_type(self):
        with self.assertRaises(DomainException):
            Person(Name("Bob"), "30")

    def test_person_set_name(self):
        person = Person(Name("Bob"), Age(30))
        person.name = Name("Alice")
        self.assertEqual(person.name.value, "Alice")

    def test_person_set_invalid_name(self):
        person = Person(Name("Bob"), Age(30))
        with self.assertRaises(DomainException):
            person.name = None

    def test_person_set_invalid_name_type(self):
        person = Person(Name("Bob"), Age(30))
        with self.assertRaises(DomainException):
            person.name = "Alice"

    def test_person_set_age(self):
        person = Person(Name("Bob"), Age(30))
        person.age = Age(35)
        self.assertEqual(person.age.value, 35)

    def test_person_set_invalid_age(self):
        person = Person(Name("Bob"), Age(30))
        with self.assertRaises(DomainException):
            person.age = None

    def test_person_set_invalid_age_type(self):
        person = Person(Name("Bob"), Age(30))
        with self.assertRaises(DomainException):
            person.age = "35"

class TestCve(unittest.TestCase):
    def test_valid_cve(self):
        cve = Cves(12345)
        self.assertEqual(cve.value, 12345)

    def test_invalid_cve_negative(self):
        with self.assertRaises(DomainException):
            Cves(-1)

    def test_invalid_cve_non_integer(self):
        with self.assertRaises(DomainException):
            Cves("CVE-2023-12345")

class TestHacker(unittest.TestCase):
    def test_hacker_creation(self):
        name = Name("Charlie")
        age = Age(28)
        cves = Cves(10)
        hacker = Hacker(name, age, cves)
        self.assertEqual(hacker.name.value, "Charlie")
        self.assertEqual(hacker.age.value, 28)
        self.assertEqual(hacker.cves.value, 10)

    def test_hacker_creation_invalid_name(self):
        age = Age(28)
        cves = Cves(10)
        with self.assertRaises(DomainException):
            Hacker(None, age, cves)

    def test_hacker_creation_invalid_age(self):
        name = Name("Charlie")
        cves = Cves(10)
        with self.assertRaises(DomainException):
            Hacker(name, None, cves)

    def test_hacker_creation_invalid_cves(self):
        name = Name("Charlie")
        age = Age(28)
        with self.assertRaises(DomainException):
            Hacker(name, age, None)

    def test_hacker_creation_invalid_name_type(self):
        age = Age(28)
        cves = Cves(10)
        with self.assertRaises(DomainException):
            Hacker("Charlie", age, cves)

    def test_hacker_creation_invalid_age_type(self):
        name = Name("Charlie")
        cves = Cves(10)
        with self.assertRaises(DomainException):
            Hacker(name, "28", cves)

    def test_hacker_creation_invalid_cves_type(self):
        name = Name("Charlie")
        age = Age(28)
        with self.assertRaises(DomainException):
            Hacker(name, age, "10")

    def test_hacker_set_name(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        hacker.name = Name("Alice")
        self.assertEqual(hacker.name.value, "Alice")

    def test_hacker_set_invalid_name(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        with self.assertRaises(DomainException):
            hacker.name = None

    def test_hacker_set_invalid_name_type(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        with self.assertRaises(DomainException):
            hacker.name = "Alice"

    def test_hacker_set_age(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        hacker.age = Age(35)
        self.assertEqual(hacker.age.value, 35)

    def test_hacker_set_invalid_age(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        with self.assertRaises(DomainException):
            hacker.age = None

    def test_hacker_set_invalid_age_type(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        with self.assertRaises(DomainException):
            hacker.age = "35"

    def test_hacker_set_cves(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        hacker.cves = Cves(20)
        self.assertEqual(hacker.cves.value, 20)

    def test_hacker_set_invalid_cves(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        with self.assertRaises(DomainException):
            hacker.cves = None

    def test_hacker_set_invalid_cves_type(self):
        hacker = Hacker(Name("Charlie"), Age(28), Cves(10))
        with self.assertRaises(DomainException):
            hacker.cves = "20"

if __name__ == '__main__':
    unittest.main()