try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except Exception: 
    print("Error")
"""except:
    print("Error")
"""
## AttributeError, OSError, etc

while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        print(x / y)
    except:
        print('Invalid input. Please try again.')
    else:
        break   #it will only break when both numbers are correct

database = {"author":"soren", "book":"concept of anxiety"}

def description(d):
    print(d["author"])
    print(d["book"])
    try:
        print(d["genre"])
    except:
        print("Genre does not exist in dictionary")                                              
    """if "genre" in d : print(d["genre"])
    else : print("Genre does not exist in dictionary")"""

description(database)

