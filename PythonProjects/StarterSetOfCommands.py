#I am Don Jones. This is a comment!

#Python variable 
firstName = str(input("Name "))

#snakecase ex
last_name = str(input("Surname "))

#int ex
primeNumber = 7

#float ex 
halfOfThree = 1.5

#boolean ex (True and False must be capitalized)
areWeevilsCute = True

#function ex (use a colon instead of curly braces, just one after the parenthases)
#preface w/ def
def subtractNumbers():
    #everything tabbed over is in the function, elsewise it is not. 
    difference = 2 - 5

#this is no longer in the function. e-z!
num = int(input("Enter a number: "))
numInt = 0

#loops
#for loop-usually has a defined number of times to occur
#while loop-sometimes if/else dependent, other times boolean dependent; goes no matter what

#file reading /and/ writing waow
#open- first is file name 
#then how to open 
    # w - write <create and overwrite contents if it exists> 
    # a - append <creates and adds text to existing file>

with open("creation.txt", "a") as file:
    file.write("Hello. I made this teehee. This is one instance of this being written. ")

#to read contents of a file use <r>
with open("creation.txt", "r") as file:
    content = file.read()
    print("It says", content)

#if/else nesting and otherwise
    #restricts input to numbers, allows input and gives an input prompt
numNum = int(input("Enter a number in numerical form please... "))

while True:
    if numNum > 30:
        print("That's not the number I was thinking of. Go lower.")
    elif numNum < 30: 
        print("That's not the number I was thinking of. Go higher.")
    elif numNum == 30:
        print("That's what I was thinking!")
        break
        #the catchall for other outliers
    else:
        print("Please enter a number.")

#loops
for i in range(1, 6):
    print("Bloody Mary " * i)

anArray = ["Boof ", "Slibby ", "Pipis "]

for things in anArray:
    print("pet name: ", things)

count = 5

while count > 0:
    print(count)
    count -= 1
print("Zero!!!")