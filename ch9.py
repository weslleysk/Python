# Class Constructor __init__

class C:
    def __init__(self):
        self.somevar = 10

x = C()
print(x.somevar)

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

x = Bird()
x.eat()
#x = Bird()
x.eat()
