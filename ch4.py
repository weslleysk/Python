#Chapter 4 - Dictionaries

# dictionary = {"key":"value", "key2":"value2", "key3":"value3"}

#dict() len() del d[key] d[key] = value   d[key1][key2]...

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


