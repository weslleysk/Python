#Chapter 11 - Files

#f = open("C:/users/username/onedrive/desktop/work/python/ch11.txt")

f = open("ch11.txt", mode = "a") #write mode w, append mode a

help(open)  #help(function)

print(f)

f.write(" More text.")

f.close()

f = open("ch11.txt", "r")

print(f.read())

f.close()

f = open("ch11.txt") #open a file every time you use it

for i in range(3):
    print(str(i) + " " + f.readline(), end="")
