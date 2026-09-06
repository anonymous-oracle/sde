# S1: literals & numeric representation

print(0b1010, 0o17, 0x2A, 0x1F) 

# S1: names & mutability

a = [1,2]
b = a
c = a[:]
a.append(3)
print(a, b, c)

# S1: conditions, loops, truthiness
for v in ["", 0, None, "hi", [], [1]]:
    print(v, bool(v))

# S1: functions & contracts
def add_item(item, bucket=[]) -> list:
    bucket.append(item)
    return bucket
# Example usage
print(add_item(1))
print(add_item(2))

def add_item_safe(item, bucket=None) -> list:
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

# Example usage
print(add_item_safe(1))
print(add_item_safe(2))

# S1: collections
data = [1,1,2,3,3,3]
print(set(data))
counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1
print(counts)

# S1: modules
import helpers
print(helpers.shout("hello"))

# S1: exceptions & file/JSON I/O
try:
    open("nope.txt")
except FileNotFoundError as e:
    print(f"File missing")
import json
json.dump({"a":1}, open("d.json","w"))
with open("d.json") as f:
    data = json.load(f)
print(data)

# S1: pytest
def square(x: float) -> float:
    return x * x

def test_square():
    assert square(3) == 9

def test_square_neg_raises():
    import pytest
    with pytest.raises(TypeError):
        square("a")

