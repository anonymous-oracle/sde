import gc
print(gc.collect())
a = [1]
b = [2]
del a, b

print(gc.collect())

a = [1]
b = [a]
a.append(b)

del a, b
print(gc.collect())