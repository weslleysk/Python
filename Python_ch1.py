#Operations
x = 10
y = 2

print(x+y)
print(x-y)

print(x/y)
print(x//y)
print(x%y)

print(x**y)
print(pow(x, y))

print(abs(-x))

z = 2
w = 3
print(z//w)
print(round(z/w))

#Modules - import module module.function
import math
import cmath

print(math.floor(1.9))
print(math.ceil(1.2))

print(cmath.sqrt(9))
print(cmath.sqrt(-1))

#Strings
x = str("Claustrophobic hell is an ")
y = input()
print(x + y)

x = 12345
y = str(x)
print(y[0], y[1], y[2])
print(len(y))

print("\\n is a \n new line")

path = "C:\\nowhere"
print(path)
print(r'C:\Program Files')

print(len("String".encode("UTF-8")))
print(len("String".encode("UTF-32")))
