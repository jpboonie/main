x=5
y='john'
print(x)
print(y)

'''
#question 1
print('jacob')
print("""Here comes my happiness again
Right back to where it should have been
'Cause now she's gone and I am free
And she can't do a thing to me

I just wanna dance the night away
With senoritas who can sway
Right now tomorrow's lookin' bright
Just like the sunny mornin' light

And if you should see her
Please let her know that I'm well
As you can tell
And if she should tell you
That she wants me back
Tell her no
I gotta go

I just wanna dance the night away
With senoritas who can sway
Right now tomorrow's lookin' bright
Just like the sunny mornin' light

And if you should see her
Please let her know that I'm well
As you can tell

And if she should tell you
That she wants me back
Tell her no
I gotta go

I just wanna dance the night away
With senoritas who can sway
Right now tomorrow's lookin' bright
Just like the sunny mornin' light

I just wanna dance the night away
With senoritas who can sway
Right now tomorrow's lookin' bright
Just like the sunny mornin' light""")

#question 2
print("1 2 3 4 5 6 7")
print(10 + 7)
x=7
y=10
print(x+y)
'''
#question 3 "strings"
x='hannah'
print(x)
s = "My lucky number is %d, what is yours?" % 7
print(s[3:8])
s = "The date is %d/%d/%d" % (7, 7, 2016)
print(s)

#string replace 
rstring = "my name is name jacob"
print(rstring.replace("name", "dog", 2))

#String find
print(rstring.find("jacob"))

#String join
jstring = "likes to have fun"
print(f'{rstring} {jstring}')
print(rstring +" "+ jstring)

#String split
places = "World,Earth,America,Canada"
print(places)
print(places.split(","))

'''
#Question 4
import random 

x = random.randrange(0,10)
print(x)

import random as r

print(r.randrange(0,10))
print(r.randrange(0,10))
print(r.randrange(0,10))

#Question 5 
number = input("enter number: ")
print("Your phone number is : " + number)
lang = input("Python or ruby?: ")
print("You chose : " + lang)


#Questions 6 
x = input("Number: ")
x = int(x)

if x < 0 or x > 10:
  print("Invalid number")
else:
  print("Good choice")

password = input("Password: ")

if password == "code":
  print("Correct")
else:
  print("Incorrect")
'''
#Question 7 loops
clist = ['Canada', 'USA', 'Mexico', 'Australia']
for c in clist:
  print(c)

clist = ['Canada', 'USA', 'Mexico', 'Australia']
size = len(clist)
i=0

while i < size:
  print(clist[i])
  i = i + 1

#functions
#!/usr/bin/env python3
def sum(list):
  sum = 0
  for e in list:
    sum = sum + e
  return sum

mylist = [1, 2, 3, 4, 5]
print(sum(mylist))

x = [ (3,6),(4,7),(5,9),(8,4),(3,1)] 
x.sort()
print(x)

from operator import itemgetter 
x.sort(key=itemgetter(1))
print(x) 

#Range
x = list(range(1,1001)) 
print(x) 

x = list(range(1,1001)) 
print(min(x)) 
print(max(x)) 

x = list(range(1,11,2)) 
y = list(range(2,11,2)) 
print(x) 
print(y) 

#Dictionary
words = {}
words["US"] = "United States" 
words["UK"] = "United Kingdom" 
words["AUS"] = "Australia" 

#write to file
f = open("test.txt","w") 
f.write("Take it easy\n") 
f.close() 

f = open("test.txt","w") 
f.write("open(\"text.txt\")\n") 
f.close() 

#read from file
for key, value in words.items():  
  print(key + " = " + value) 

filename = "test.txt" 
with open(filename) as f: 
  lines = f.readlines() 
i = 1 
for line in lines: 
  print(str(i) + " " + line)
  i = i + 1

#nested loops
for x in range(1,4): 
 for y in range(1,4): 
  print(str(x) + "," + str(y)) 

persons = [ "John", "Marissa", "Pete", "Dayton" ] 
for p1 in persons: 
 for p2 in persons: 
  print(p1 + " meets " + p2) 

print()

#slices
pizzas = ["Hawai","Pepperoni","Fromaggi","Napolitana","Diavoli"] 
slice = pizzas[2] 
print(slice) 
slice = pizzas[3:5] 
print(slice) 

s = "Hello World" 
slices = s.split(" ") 
print(slices[1])

#mutpile returns
def sum(a,b): 
 return a+b 
print( sum(2,4) ) 

def getUser(): 
 name = "Laura" 
 age = 26 
 job = "Pilot" 
 education = "University" 
 nationality = "Spain" 
 return name,age,job,education, nationality 
data = getUser() 
print(data) 

#Scope
balance = 10 
def reduceAmount(x): 
 global balance 
 balance = balance - x 
reduceAmount(1) 
print(balance) 

def calculate(): 
 x = 3 
 y = 5 
 return x+y 
x = calculate() 
print(x)

#time and date
import time 
timenow = time.localtime(time.time()) 
year,month,day,hour,minute = timenow[0:5] 
print(str(year) + "-" + str(month) + "-" + str(day)) 

#class
class Website: 
 def __init__(self,title): 
  self.title = title 
  self.location = "the web" 
 def showTitle(self): 
  print(self.title) 
 def showLocation(self): 
  print(self.location) 

obj = Website('pythonbasics.org') 
obj.showTitle() 
obj.showLocation() 

#Constructor
class Human: 
 def __init__(self): 
  self.legs = 2
  self.arms = 2
  self.eyes = 2

print()

#Getter and Setter
class Friend: 
 def __init__(self): 
  self.job = "None" 
  self.age = 0 
 def getJob(self): 
  return self.job 
 def setJob(self, job): 
  self.job = job 
 def getAge(self): 
  return self.age 
 def setAge(self, age): 
  self.age = age 
Alice = Friend() 
Alice.setJob("Carpenter") 
Alice.setAge(33) 
print(Alice.job) 
print(Alice.age) 

#Modules
import math 
print(math.sin(3)) 

def snake():
  print("ssss im a slithery lil snake")

import questions
questions.snake()

#Inheritance

'''class iPhone(App): 
 def getVersion(self): 
  print('iPhone version') '''

class A: 
 def start(self): 
  print('starting') 

class B: 
 def go(self): 
  print('go') 

class C(A,B): 
 def getVersion(self): 
  print('Multiple inheritance class') 

app = C() 
app.getVersion()
app.start() 
app.go() 

#Enumerate
for item in enumerate(["a", "b", "c","d"]): 
 print(item) 

'''
Write Answers to Questions that require no coding:

Strings
1. yes
2. it works with phrases as well
3. It only finds the first one
4. yes, it can be split on multiple characters
5. yes, you can split on phases

While loops
1. for loops automatically increment and while loops need a    counter to be defined
2.Yes 
3.Yes

Nested loops 
1. O(n^2)

Functions
1. Yes
2. Yes
3. No

Read file
1. You would still be allowed to read the file as long as the document is accessible to the code.

Try Exeption
1.No
2.Yes 
3.If you don't want to catch and handle an exception

Class 
1. Yes, a python file can define more than one class. 
2. Yes, you can create multiple objects from the same class 3. Objects cannot create classes, but you can create objects from classes

Getter and Setter
 A getter and setter help you to create clean code. By calling the methods instead of changing variables, you can prevent accidentally changing the variable to a number you do not want.  Say you have a class Human with a variable age, in the setter you could prevent the variable from being set to negative numbers of numbers higher than 150 using an if statement. 

Static methods 
1. Yes, such a method is a static method 
2. Because static methods go against the paradigm of object orientation. The general consensus is that objects are created from classes. The objects methods are defined in the class. If you create a static method, that method is accessible without creating an object. 

Iterable 
1. an object that can be used as a sequence 
2. lists, strings, dictionaries and sets 

Classmethod 
1. a method that’s accessible by all objects and the class 
2. a static method doesn’t have access to the class 

Multiple inheritance 
1. No, only some programming languages support multiple inheritance. 
2. It increases cohesion between the classes. If you have very strong cohesion throughout your code, your classes are not reusable in other projects. 
3. No, there is no limit. 
'''



