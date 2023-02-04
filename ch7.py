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