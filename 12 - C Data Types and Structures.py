from ctypes import *

# https://docs.python.org/library/ctypes.html

b0 = c_bool(0)
b1 = c_bool(1)

print(b0)
print(b0.value)
print(b1)
print(b1.value)

print("----------")

i0 = c_uint(-1) #maximum unsigned integer wraps around
print(i0.value)

c0 = c_char_p(b"test")
print(c0.value)

print(c0) #memory address
c0 = c_char_p(b"test2")
print(c0) #memory address
print(c0.value)

print("----------")

p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

print("----------")

p0.value = b"a"
print(p0)
print(p0.raw)
print(p0.value)

print("----------")

i = c_int(42)
pi = pointer(i)

print(i)
print(pi)
print(pi.contents)

print("----------")

print(p0.value)
print(p0)
print(hex(addressof(p0)))

print("----------")

pt = byref(p0)
print(pt)

print("----------")

print(cast(pt, c_char_p).value)
print(cast(pt, POINTER(c_int)).contents)
print(ord('a'))

print("----------")

class PERSON(Structure):
    _fields_ = [("name", c_char_p),
                ("age", c_int)]
bob = PERSON(b"bob", 33)
print(bob.name)
print(bob.age)

print("----------")

person_array_t = PERSON * 3
print(person_array_t)
person_array = person_array_t()

person_array[0] = PERSON(b"bob", 33)
person_array[1] = PERSON(b"alice", 24)
person_array[2] = PERSON(b"mallory", 54)

for person in person_array:
    print(person)
    print(person.name)
    print(person.age)