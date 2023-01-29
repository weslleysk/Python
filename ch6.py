#Chapter 6 - Abstractions

# functions    def function(parameter): "docstring" ... return    function.__doc__     help(function)      

def f(author):
    return "My favorite author is " + author
print(f("Kierkegaard"))

def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result
print(fibs(10))

def sqre(x):
    "calculates x*x"  #docstring
    return x*x
print(sqre.__doc__)


help(enumerate)    



#1 initializes a data structure (dictionary)

def init(data):
    data["first"] = {}
    data["middle"] = {}
    data["last"] = {}

#2 look the data inside the data structure

def look(data, label, name):
    return data[label].get(name)

#3 adds / stores data to the data structure

def store(data, fullname):

    labels = ["first", "middle", "last"]
    names = fullname.split()

    if len(names) == 2 : names.insert(1, "")

    for label, name in zip(labels, names):
        people = look(data, label, name)
        if people : people.append(fullname)
        else : data[label][name] = [fullname]

#4 Create a data structure

storage = {}
init(storage)
store(storage, "Soren Kierkegaard")
store(storage, "Aldous Huxley")
store(storage, "CS Lewis")
print(look(storage, "first", "Weslley"))
print(look(storage, "last", "Kierkegaard"))
print(look(storage, "middle", ""))

