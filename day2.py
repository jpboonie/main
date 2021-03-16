#Day 2 Lecture 
a=2 
print('id(2) =', id(2))

print('id(2) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))

a = 5 
a = 'Hello World!'
a = [1,2,3]
def printHello():
  print("Hello")

a = printHello

a()

def outer_function():
  b = 34 
  def inner_function():
    c = 42
  
  a = 20

def outer_function():
    
  a=34

  def inner_function():
      a=20
      print('a = ', a)
    
  inner_function()
  print('a = ', a)

a=20
outer_function()
print('a = ', a)

def identity(x):
  return x

x= (lambda x: x + 1)(2)
print(x)

x= lambda a: a + a+20
print(x(5))

x= lambda a,b,c : a+b+c
print(x(5,4,2))

def myfunc(m):
  return lambda a : a * m

mydouble = myfunc(2)
print(mydouble(10))

b = 200
a = 20

if b > a:
  print("b greater than a")

class Account:
  def __init__(self, account_name, balance=0):
    self.account_name = account_name
    self.balance = balance

  def deposit (self, amount):
    self.balance += amount

  def withdraw (self, amount):
    if amount <= self.balance:
      self.balance -= amount 
    else:
      print('cant withdraw amount as no funds')

myAccount = Account("john", 100)

myAccount.deposit(100)
myAccount.withdraw(100)
print(myAccount.balance)

#Data hiding
class dummycounter:
  __secretCount=0

  def count(self):
    self.__secretCount += 1
    print (self.__secretCount)

Counter = dummycounter()
Counter.count()
Counter.count()

print(Counter._dummycounter__secretCount)

