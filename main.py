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

#question 3
x='hannah'
print(x)
s = "My lucky number is %d, what is yours?" % 7
print(s[3:8])
s = "The date is %d/%d/%d" % (7, 7, 2016)
print(s)

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