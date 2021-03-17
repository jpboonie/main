#File editing 

f = open("demofile.txt", "a")
f.write("Now file has more content!")
f.close()

f = open("test.txt", "w")
f.write("This is some data that our Python script created.\n")
f.close()

file = open("demofile.txt")

print(file.read())

f = open("pic.PNG", "rb")
print(f.read(50))

f = open("test.txt", "r")
readfile = f.read(7)
print(readfile) 
f.close()

f = open("test.txt", "r")
readfile = f.readline()
print(readfile)
f.close()

f = open("demofile.txt", "r")
# f.write("Now there is more!")
lines = f.readlines()
for x in lines:
  print(x)
f.close()

f = open("demofile.txt", "w")
f.write("Oops! Ii have to delete the content")
f.close()

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 

#import os
#os.rmdir("myemptyfolder")

#logging
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("test_logger")

logger.info("This will not show up.")
logger.warning("This will.")

import logging
log = logging.getLogger("my-logger")
log.info("Hello, world")

import logging
import os
 
class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)
 
    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result
 
import logging

log = logging.getLogger(__name__)

def do_something():
    log.debug("Doing something!")

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("This  will get logged") 

import logging
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning') 

import logging
name = 'kumar'
logging.error('%s raised an error', name)

print("*" * 10 )

#Date and Time
#Current Date and Time
import datetime

current_date = datetime.datetime.today()
print(current_date)


#Creating a new Date and time object
from datetime import datetime
my_datetime = datetime(2020,2,26,1,15,30)
print(my_datetime)

#What's inside datetime?
import datetime

print(dir(datetime))

from datetime import datetime, timezone, timedelta

naive_today = datetime.now()
print(naive_today)

aware_today = datetime.now(timezone.utc)
print(aware_today)

print(aware_today.strftime('%Y-%m-%d %H:%M:%S'))

#timedelta
tomorrow = aware_today + timedelta(days=1)
print(tomorrow.strftime('%Y-%m-%d %H:%M:%S'))

#user_date = input("Input your date in format YYYY-MM-DD:")
#user_date = datetime.strptime(user_date,'%Y-%m-%d')

#print(user_date)

name = "John Smith"

print(name.__contains__("John"))
hi = range(1, 10, 2)
print(hi)

#Regex
# Module Regular Expression is imported using __import__(). 
import re 
  
# compile() creates regular expression character class [a-e], 
# which is equivalent to [abcde]. 
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'. 
p = re.compile('[a-e]') 
  
# findall() searches for the Regular Expression and return a list upon finding 
print(p.findall("Aye, said Mr. Gibenson Stark")) 


import re

regex = re.compile(r'-?[0-9]+(\.[0-9]+)?')

while True:
    num = input('Type some text: ')
    if regex.match(num):
         print('That is a valid number!')
    else:
         print('That is not a number!')
