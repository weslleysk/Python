# Chapter 7

# creating a class

class Person:
    
    def set_name(self, name):    #function definitions inside a class statement
        self.name = name         #'self' is a parameter of the function, it will refer to the object itself

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello {}".format(self.name))



author = Person()                #object = class()
author.set_name("Soren")         #object.function(parameter)
author.greet()                   #object.function()

print("")

print(author.set_name)
print(author.get_name)
print(author.greet)

print("")

print(author.name)
author.greet()

print("")

author.name = "Huxley"
author.greet()

print("")


class Bird():
    song = "~~~~"
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()


class Security:
    def __private(self):
        print("Private")

    def public(self):
        print("Public")
        self.__private()

var = Security()
var.public()



print("")



def f(x): return x * x
print(f(2))

y = lambda x: x * x
print(y(3))



print("")



class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)