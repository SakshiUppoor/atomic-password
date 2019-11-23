#IF STATEMENT

'''
age = int(input('Enter your age'))

if age >=18:
    print("You are an adult")
else:
    print("You are not an adult") 
'''

#ELIF STATEMENT

'''
marks =int(input('Enter your marks'))

if marks >= 90:
    print('Grade A')
elif marks >=80:
    print('Grade B')
elif marks >=60:
    print('Grade C')
elif marks <60:
    print('Grade D')
'''

#LISTS

'''
names=["Mike","John","Rob"]

print(names,names[0])

numbers = [1,2,3,4,5]

print(numbers[4])

abc = []
print(abc)
'''

#LIST OPERATIONS

'''
numbers = [1,1,1,1,1]
#numbers[2] = 5
#print(numbers)

newnumbers = [2,2,2,2,2]

print(numbers * 3)

fruits = ['Apple','Mango','Peach']

print("Orange" in fruits)
'''

#LIST FUNCTIONS

'''
fruits=["Apple","Mango","Peach","Orange"]

#fruits.append("Banana")
#print(len(fruits))
#fruits.insert(1,"Banana")
#print(fruits.index("Peach"))
'''

#RANGE FUNCTION

'''
#numbers = list(range(10))
#numbers = list(range(3,8))
#numbers = list(range(1,30,3))

print(numbers)
'''

#FUNCTIONS

'''
def function():
    print("Sakshi)
    print("Apple")
    print("Mumbai")

function()
function()
function()
'''

#FOR LOOP

'''
for x in range(1,11):
    print(x)

fruits=["Apple","Mango","Peach","Orange"]
for x in fruits:
    print(x)

for x in range(0,21,2):
    print(x)
'''

#BOOLEAN LOGIC

'''
username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Valid User")
else:
    print("Invalid user")
'''

#WHILE LOOP

'''
counter = 0
while counter<=10:
    print(counter)
    counter+=1
'''

#FUNCTION ARGUMENTS

'''
def add(a,b):
    print(a+b)

add(2,3)
'''

#RETURNING VALUES

'''
def add(a,b):
    c = a + b 
    return c 

result = add(2,3)

print(result)
'''

#PASSING FUNCTION AS AN ARGUMENT

'''
def add(a,b):
    return a + b 

def square(c):
    return c**2

result = square(add(2,3))

print(result)
'''

#MODULES

'''
import random

for x in range(5):
    result = random.randint(1,6)
    print(result)
'''

#ERRORS & EXCEPTIONS

'''
1. Syntax error:
eg:
def add(a,b)
    print(a+b)
add(2,3)

2. Logical error
eg:
def add(a,b):
    print(a*b)
add(2,3)

Exceptions:
1. Divide by 0
'''

#EXCEPTION HANDLING

'''
try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error")
finally:
    print("This is going to execute no matter what")
'''

#FILE HANDLING

'''
file = open("demo.txt","r")
content = file.read(10)
print(content)
file .close()

file = open("demo.txt","a")
file.write("Hello,World\n")
file.close()

file = open("demo.txt","r")
content = file.read()
print(content)
file.close()
'''

#DICTIONARIES

'''
people = {"John": 32,"Jane": 23}
print(people["John"])

numbers = {
    1:"One",
    2:"Two",
    3:"Three"
}
print(numbers.get(5,"Key not found"))
'''

#TUPLES

'''
fruits = "Apple","Mango","Peach"
print(fruits[0])
'''

#LIST SLICING

'''
numbers = [0 , 100 , 200 , 300 , 400 , 500 , 600]

print(numbers[6:1:-1])
'''

#LIST COMPREHENSION

'''
square = [x**2 for x in range(5)]
print(square)

even = [x for x in range(16) if x%2 == 0]
print(even)
'''

#STRING FORMATTING

'''
numbers = [4,5,6]
newstring = "Numbers:{0}{1}{2}".format(numbers[0],numbers[1],numbers[2])
print(newstring)

a = "{x}/{y}".format(x=100,y=200)
print(a)
'''

#STRING FUNCTIONS

'''
print(",".join(["Apple","Mango","Peach"]))

print("Hello there".replace("there","World"))
newstring = "This is a string"
print(newstring.startswith("This"))
print(newstring.endswith("This"))
print(newstring.upper())
print(newstring.lower())
'''

#NUMERIC FUNCTIONS

'''
print(min(1,2,2,3,3,4,5,5,6))
print(max(1,2,3,4,5,6,7))
print(abs(2+3j))
'''

#FUNCTIONAL PROGRAMMIMG

'''
def add_ten(x):
    return x+10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten,10))
'''

#LAMBDAS

'''
def square(x):
    return x**2

print(square(30))

result = (lambda x: x**2)(30)
print(result)
'''

#MAP

'''
def add(x):
    return x+2

newlist = [10,20,30,40,50,60]

result = list(map(add,newlist))

print(result)

newlist = [10,20,30,40,50,60]

result = list(map(lambda x:x+2,newlist))

print(result)
'''

#FILTERS

'''
newlist = [1,2,3,4,5,6,7]

result = list(filter(lambda x:x%2== 0,newlist))

print(result)
'''

#GENERATORS

'''
def function():
    counter = 0
    while counter < 5:
        yield counter 
        counter +=1

for x in function():
    print(x)

def even(x):
    for i in range(x):
        if i%2 == 0:
            yield i

print(list(even(21)))
'''

#CLASS & INHERITANCE

'''
class Students:

    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print('Accepting data')
        self.name = input('Enter your name')
        self.contact = input('Enter your contact')

    def putdata(self):
        print('Name:'+self.name,'  Contact:'+self.contact)

class ScienceStudent(Students):

    def __init__(self, age):
        self.age = age

    def science(self):
        print('I am a science student')

Rob = ScienceStudent(20)
Rob.science()
Rob.getdata()
Rob.putdata()
'''

#RECURSION

'''
def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)

result = fact(5)

print(result)
'''

#SETS

'''
numbers = {1,2,3,4,5,6}

numbers.add(9)
numbers.remove(4)
print(numbers)

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

print(seta|setb)
print(seta&setb)
print(seta-setb)
'''

#ITERTOOLS

'''
from itertools import count

for i in count(3):
    print(i)

    if i >= 20:
        break

from itertools import accumulate,takewhile

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x<=10,numbers)))
'''

#OPERATOR OVERLOADING

'''
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        x = self.x + other.x
        y= self.y + other.y
        return Point(x,y)

    def __str__(self):
        return "{0},{1}".format(self.x,self.y)

point1 =Point(1,4)
point2 = Point(2,8)
print(point1 + point2)
'''

#DATA HIDING

'''
class Myclass:
    __hiddenvariable = 0

    def add(self,increment):
        self.__hiddenvariable+=increment
        print(self.__hiddenvariable)

objectone = Myclass()
objectone.add(5)
print(objectone.__hiddenvariable)
'''

#Regular expression
'''
import re

pattern = r"eggs"

if re.match(pattern,"baconeggsbaconeggseggs"):
    print("Match found")

else:
    print("No match found")

if re.search(pattern,"baconeggsbaconeggseggs"):
    print("Match found")

else:
    print("No match found")

print(re.findall(pattern,"baconeggsbaconeggs"))
'''

#FIND & REPLACE
'''
import re

string = "My name is John. Hi, I'm John"
pattern = r"John"
newstring = re.sub(pattern,"Rob",string)
print(newstring)
'''

#DOT METACHARACTER
'''
import re

pattern = r"gr.y"

if re.match(pattern,"grey"):
    print("Match found")
'''

#Caret & DOLLAR METACHARACTER
'''
import re

pattern = r"^gr.y$"

if re.match(pattern,"grey"):
    print("Match 1")
'''

#CHARACTER CLASS
'''
import re

pattern = r"[A-Z][A-Z][0-9]"

if re.match(pattern,"AD2"):
    print("match found")
'''

#STAR METACHARACTER
'''
import re

pattern = r"eggs[bacon]*"

if re.match(pattern,"eggsg"):
    print("Match found")
'''

#GROUP
'''
import re

pattern = r"bread[eggs]*bread"

if re.match(pattern,"breadeggseggsbreadeggs"):
    print("Match found")
'''

