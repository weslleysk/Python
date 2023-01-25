#Chapter 4 - Dictionaries

# dictionary = {"key":"value", "key2":"value2", "key3":"value3"}

#dict() len() del d[key]   d[key] = value  d.pop(key)   d[key1][key2]...  d.clear() d.copy() d[key].remove(value) d[key].append(value) d.update(d2)
#d.get(key) d.items() d.keys() d.values() 

#d = {}.fromkeys(['key', 'key2'], 'values') d.setdefault(key, value)

items = [('key1', 'value1'), ('key2', 'value2')]
d = dict(items)
print(d)
print(d["key1"])

d = dict(name="AH", book="Devils of Loudun")
print(d)

d = {"AH":"Devils of Loudun", "SK": "Concept of Anxiety"}
print(d)
print("number of pairs - key:value = {x}".format(x = len(d)))
print(d["AH"])
d["AH"] = "Stories and Poems" #dictionary[key1] = value1 
print(d["AH"])
if input("author: ") in d : print("Author is inside the dictionary.")
else : print("Author is not inside the dictionary.")
del d["AH"]
print(d)
d["Freud"] = "Biography"
print(d)

#Simple Database

oeuvre = {

    "Soren" : 
        {
            "book":"Concept of Anxiety",
            "quantity":200
        },
    "Huxley" :
        {
            "book":"Devils of Loudun",
            "quantity":100
        },
    "Freud" :
        {
            "book":"Biography",
            "quantity":250
        }

    }

author = input("author: ")
request = input("Book (b) or Quantity (q)?")
if request == "b" : key = "book"
if request == "q" : key = "quantity"

if author in oeuvre : print("{} : {}".format(author, oeuvre[author][key] ))
else : print("Author is not inside the oeuvre.")

#def new_func(oeuvre, author, key):
#    if oeuvre.get(author) != None : print("{} : {}".format( author, oeuvre[author][key] ))
#    else : print("Author is not inside the oeuvre.")

#new_func(oeuvre, author, key) 


#Dictionary Methods

d = {"a":"b", "c":{"d":"e"}, "f":"g"}
print(d)
print(d["c"]["d"])
d.clear()
print(d)


d = { "user":"a", "password":"p", "config":[1,2,3] }
x = d.copy()
x["user"] = "b"
x["password"] = "q"
x["config"].remove(1)
print(x)
print(x["config"][0]) #list



from copy import deepcopy   #from module import function

d = { "user": [1,2] }
x = d.copy()
y = deepcopy(d)
d["user"].append(3)
print("x: {} y: {}".format(x, y))


d = {}.fromkeys(["key1", "key2"], 0)
print(d)


d = {}
print(d.get("key", None))
d["key"] = 1
print(d.get("key"))


d = {"a":1, "b":2, "c":3}
print(d.items())
print(d.keys())


d.pop("a")
print(d)


d = {}
d.setdefault("key","value")
print(d)
d["key"] = 1
d.setdefault("key","value")
print(d)


d = {
    "author":"SK",
    "book":"concept of anxiety",
    "quantity":10
    }
x = { "quantity": 5 }

d.update(x)

print(d)
print(d.values())







