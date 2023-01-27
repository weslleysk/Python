#Chapter 5 - Conditionals, Loops, and some other Statements

# line comment

""" block
    comment
"""

#print

print("Soren", "Kierkegaard")

x = "Aldous Huxley"
y = "Sigmund Freud"
z = "Soren Kierkegaard"

print(x, y, z)

print("Same ", end="") #same line
print("Line")

print("") #new line

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

y = "devils"
y += " of loudun"
print(y)








#Identation: spaces - Blocks (conditionals, loops): group of statements that can be executed if a condition is true

#== != is is not in not in

#and or not

#False None 0 "" () [] {}

print(bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

#if condition is True:
#   ...
#elif condition is True:
#   ...
#elif condition is True:
#   ...
#else:
#   ...

name = input("The first name of the most neurotic philosopher of the world: ")

if name == "Soren":
    print("Kierkegaard")
elif name == "Aldous":
    print("Huxley")
else:
    print("Literature is dead.")


var = input("Are you a hikikomori? (yes/no) ")

if var == "yes":
    time = float(input("For how many years? "))
    if time < 0.6:
        print("Not hikikomori")
    elif 0.6 <= time <= 2:
        print("Beginner hikikomori")
    elif  2 < time <= 4:
        print("Normal hikikomori")
    else:
        print("Insane hikikomori")
else:
    print("You are not an hikikomori")


x = 2
y = [1, 2, 3, 4, 5]

print(x == y, x != y, bool(x is y), bool(x is not y), bool(x in y), bool(x not in y))

x = y = [1, 2]
z = [1, 2]

print(x == y, x == z, x is y, x is z)



var = input("Type something random: ")

if "a" in var : print("Random contains a")
else : print("Random does not contain a")

print("a".lower() < "B".lower(), ord("a"), ord("b"))




money = int(input("How much money do you have? "))
price = 800
credit = False
if(money >= 500) : credit = True

if((money >= price) and credit == True and not money < 0):
    print("Purchase was a success.")
elif ((money >= price) or credit == True):
    print("You need more money.")
else: 
    print("Purchase was a failure.")



# Assert

hikikomori = int(input("Through how many years have you been an hikikomori? "))
assert 0 < hikikomori <= 100, "Do not tell lies."





# Loops



# while

book = ""

while not book:
    book = input("Write the name of one book: ")
print("{} is the book.".format(book))

print("")


x = 0

while x <= 5:
    print(x, end=" ")
    x += 1

print("")



s = [1, 2, 3, 4, 5]

i = 0

while i <= len(s) - 1:
    print(s[i], end=" ")
    i += 1

print("")




# for

sequence = [1, 2, 3, 4, 5]

for s in sequence:
    print(s, end=" ")



print("")
print("")



# Dictionary iteration

d = {"key1":1, "key2": 2, "key3": 3}

for key in d:
    print(key, " : ", d[key])

print("")

for key, value in d.items():
    print(key, " : ", d[key])

print("")



# parallel iteration

s = ["Soren", "Huxley", "Lewis"]
b = ["Concept of Anxiety", "Devils of Loudun", "The Abolition of Man"]

for i in range(0, len(s)):
    print(s[i], " : ", b[i])

print("")

print(list(zip(s, b)))

for name, book in zip(s, b):
    print(name, " : ", book)

print("")




l = [30, 45, 100, 90, 50]

print(sorted(l))

s = "Kierkegaard"

print(''.join(list(reversed(s))))



from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(root)



""" for x in seq:
    if condition1: continue
    if condition2: continue
    if condition3: continue

    do_something()
    do_something_else()
    do_another_thing()
"""
    
""" for x in seq:
        if not (condition1 or condition2 or condition3):
        do_something()
        do_something_else()
        do_another_thing() 
"""

while True:
    word = input("Write the name of a book or author: ")
    if word == "" or word == " ":
        break


for n in range(99, 80, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        continue














