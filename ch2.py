#Chapter 2 - Lists and Tuples

sequence1 = ["SK", "The Concept of Anxiety", "Philosophy", 400]
sequence2 = ["Huxley", "Devils of Loudun", "Literature", 200]
database = [sequence1, sequence2]

print(database)

sequence3 = [input("author: "), input("name: "), input("genre: "), int(input("quantity: "))]
author = sequence3[0]
name = sequence3[1]
genre = sequence3[2]
quantity = int(sequence3[3])

print(sequence3)
print(sequence3[0:2])
print(sequence3[-3:])

#sequence[start:finish:pace]
#len() min() max()

numbers = [1,2,3,4,5]
print(numbers[0:5:1])
print(numbers[5::-1])
print(numbers[5::-2])

print(len(numbers))
print(min(numbers))
print(max(numbers))

string = str(input("string: "))  #hikikomori
age = int(input("age: "))  #20
sequence = [string, age]
print(sequence)

#if [list] in [database] : print("")
#else : print("")

users = ["X", "Y", "Z"]
print("A" in users)

database2 = [["SK", "The Concept of Anxiety"], ["AH", "Devils of Loudun"]]
author = input("author: ")
book = input("book: ")
if [author, book] in database2: print("Author and Book available.")
else : print("Access denied.")

hikikomori = "hikikomori"
list1 = list(hikikomori)
list1[0] = "k"
print(list1)

books = ["The Concept of Anxiety", "Devils of Loudun", "Abolition of Man"]
print(books)
del books[1]
print(books)

#sequence[start:finish] = list("string")

bookname = list("Hikikomori")
bookname[4:] = list("neet")
bookname[8:] = []
print(bookname)

##List Methods - object.method(arguments) .sort() .sort(key=len) .sort(reverse=True) .append() .extend() .insert(index, int/string) 
#.remove() .pop(index) .clear() .copy() .count() .index()

sequence4 = ["SK", "AH"]
sequence4.append(str("CSL"))
print(sequence4)
sequence4.insert(0, "DH")
print(sequence4)
sequence4.pop()
sequence4.pop(0)
print(sequence4)
sequence4.clear()
print(sequence4)

a = [1,2,3]
b = a.copy()
b[0] = 2
print(a)
print(b)

c = [[1,2,3], 1, 1, [1, 1, 1]]
print(c.count(1))
d = ["a","b","c","d","a"]
print(d.count("a"))

e = [1,2,3]
f = [4,5,6]
e.extend(f)
print(e)

q = ["a","b","c"]
print(q.index("b"))

w = [1,2,2,3]
w.remove(2)
print(w)

q = [4,3,1,7]
w = q.copy()
w.sort()
e = sorted(q)
print(q)
print(w)
print(e)

x = ["qwe", "asd", "qwerty", "qwertyuio", "qa", "a"]
x.sort(key=len)
print(x)

y = [1,2,3,4,5]
y.sort(reverse=True)
print(y)

# Tuples - Immutable Sequences

sequence = [1,2,3]
x = tuple(sequence)
print(x)
print(x[0:2])






