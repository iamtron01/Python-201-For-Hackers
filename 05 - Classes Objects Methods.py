class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def print_name(self):
        print("My name is {}".format(self.name))

    def print_age(self):
        print("My age is {}".format(self.age))

    def birthday(self):
        self.age += 1

    wants_to_hack = True

bob = Person("bob", 30)
alice = Person("alice", 20)
mallory = Person("mallory", 50)

print(bob)
print(alice)
print(mallory)

print(hasattr(bob, "age"))
print(hasattr(bob, "asd"))

setattr(bob, "asd", 100)
print(getattr(bob, "asd"))

print("---------")

bob.print_name()
bob.print_age()

bob.age =31
bob.birthday()
bob.print_age()

print(bob.wants_to_hack)
print(Person.wants_to_hack)

print("---------")

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)