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


# Recursion - function calls function

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
print(factorial(4))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(3))

def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result
print(power(2,3))

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
print(power(2,4))


# binary search

def search(sequence, number, lower=0, upper=None):

    if upper == None : upper = len(sequence) - 1

    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
    if number > sequence[middle]:
        return search(sequence, number, middle + 1, upper)
    else:
        return search(sequence, number, lower, middle)

seq = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
seq.sort()
print(search(seq, 3))