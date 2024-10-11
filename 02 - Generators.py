def gen_demo():
    n = 1
    yield n
    
    n+=1
    yield n

    n+=1
    yield n

test = gen_demo()
print(next(test))
print(next(test))

print("---------")

test = gen_demo()
for n in test:
    print(n)

print("---------")

def xor_static_key(a):
    key = 0x5
    for i in a:
        yield chr(ord(i) ^ key)
for i in xor_static_key("test"):
    print(i)

print("---------")

xor_static_key2 = (chr(ord(i) ^ 0x5) for i in "test")
for i in xor_static_key2:
    print(i)