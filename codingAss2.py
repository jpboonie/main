print("hello")

num = [20, 10, 3, 4]
print(max(num))

#Question 1
def maxnum(num1, num2):
  if num1 > num2:
    print(f"{num1} is the greatest")
  else:
    print(f"{num2} is the greatest")

maxnum(4, 5)

#Question 2
def fizz_buzz(num):
  if(num%5 == 0 and num%3 == 0):
    return "FizzBuzz"
  if(num%3 == 0):
    return"Fizz"
  if(num%5 == 0):
    return "Buzz"
  else:
    return num

print(fizz_buzz(3))

#Question 3
def speed_limit(speed):
  limit = 70
  counter = 1
  points = 0
  if speed < limit:
    print("OK")
  else:
    while limit < speed:
      if counter == 5:
        points += 1
        counter = 0

      counter += 1
      limit += 1
  
  print(f"Points: {points}")
  if points >= 12:
    print("License suspended")

speed_limit(131)

#Question 4
def showNumbers(limit):
  counter = 0

  while counter <= limit:
    if counter % 2 == 0:
      print(f"{counter} EVEN")
    else:
      print(f"{counter} ODD")
    
    counter += 1

showNumbers(8)

def multiples(limit):
  counter = 0
  sum = 0

  while counter <= limit:
    if counter % 3 == 0 or counter % 5 == 0:
      sum += counter
    counter += 1
  print(sum)  

multiples(5)

#Question 6
def show_stars(rows):
  counter = 1

  while counter <= rows:
    print("*" * counter)
    counter += 1

show_stars(10)

#Question 7
def prime_numbers(limit):
  primes = []
  counter1 = 2
  counter2 = 1
  factor = 0

  while counter1 <= limit:
    factor = 0
    counter2 = 1
    while counter2 <= counter1:
      if counter1 % counter2 == 0:
        factor += 1
      counter2 += 1
    if factor == 2:
      primes.append(counter1)
    counter1 += 1

  print(primes)

prime_numbers(20)
