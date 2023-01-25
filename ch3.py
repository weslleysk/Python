#Chapter 3 - Strings

#"{x}".format(x=s) "{x:type.2f}".format(x=n) "{x:b}".format(x)

h = ["NEET", "Hikikomori"]
s = "A person who is a social recluse and withdrawl from society: {name[1]}".format(name=h)
print(s)

s = "The string is {num:s}".format(num='42')
print(s)

n = "The number is {num}".format(num=42)
print(n)
f = "The number is {num:f}".format(num=42)
print(f)
b = "The number is {num:b}".format(num=42) #2**1 + 2**3 + 2**5 (10101)
print(b)
p = "The percentage is {num:.2%}".format(num=0.8)
print(p)

pi = 3.140000000
p = "Pi is equal to {pi:.2f}".format(pi=pi)
print(p)

#String Methods .center() .strip() .find() .join() .split() .lower() .replace() .translate()

title = "The Devils of Loudun".center(40, "|")
print(title)

t = "Lily of the Field".center(40)
print(t.strip())

title2 = "The Anxiety"
print(title2.find("Anxiety"))

title3 = "Crime and Punishment"
print(title3.find("Punishment", 5, 20)) #word, start, end

dirs = ['', 'usr', 'bin', 'env']
print("C:" + '\\'.join(dirs))

seq = "\\usr\\bin\\env"
print(seq.split("\\"))

name = "X"
names = ['x', 'y', 'z']
if name.lower() in names : print("Yes")

print("Sigmund Freud".replace("Sigmund", "C.G JUNG"))

table = str.maketrans('ct', 'ly')
print("Occult".translate(table))







