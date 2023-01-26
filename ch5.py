#Chapter 5 - Conditionals, Loops, and some other Statements

#print

print("Soren", "Kierkegaard")

x = "Aldous Huxley"
y = "Sigmund Freud"
z = "Soren Kierkegaard"

print(x, y, z)

print("Same ", end="")
print("Line")

#module

#import module  from module import function, function2, function3   from module import *

import math
print(math.sqrt(4))

from math import sqrt as sq
x = int(sq(36))
print("{:.0f}".format(x))

#assignement

x, y, z = 1, 2, 3
print(x, y, z)
values = 4, 5, 6
print(values)
x, y, z = values
print(x, y, z)

d = {"user":"weslley", "book":"devils of loudun"}
key, value = d.popitem()
print(key, value)

a, b, *rest = 1, 2, 3, 4, 5, 6
print(rest)
print(*rest)

name = "heinrich otto leah claudia chevalier vampire"
first, *middle, last = name.split()
print(middle)

#augmented assignments

x = 0
x += 1
x *= 2
x %= 3
x /= 4
print(x)





