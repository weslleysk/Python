#Chapter 4 - Dictionaries

# dictionary = {"key":"value", "key2":"value2", "key3":"value3"}

#dict() len() del d[key] d[key] = value

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

