import sys
a = [7]
b = a
c = [a, a]
b = None
del c

print(sys.getrefcount(a))