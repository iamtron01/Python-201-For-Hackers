import pickle

hackers = {
    "neut": 1,
    "geohot": 100,
    "neo": 1000}

for key, value in hackers.items():
    print(key, value)

print("---------")

serialized = pickle.dumps(hackers)
print(serialized)

deserialized = pickle.loads(serialized)
print(deserialized)

print("---------")

with open("hackers.pickle", "wb") as handle:
    pickle.dump(hackers, handle)
with open("hackers.pickle", "rb") as handle:
    print(pickle.load(handle))