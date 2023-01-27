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







