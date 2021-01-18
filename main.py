import requests
from string import Template
from math import pi
import Cal
import os

from Dog import Dog

import random

print("Current working dir : " + os.getcwd())
print(type(pi))

import datetime

x = datetime.datetime.now()
print(x)

# print ( from keyword.kwlist)
name = "kumar"
count = 12

d1 = Dog("1","TEST");
print("---> ",d1.bark())

a = dict(one=1, two=2, three=3)
print("dict : ", a)
print("Length :", len(a))

format = 'PI with 3 decimal values : %.3f'

# print(format % pi)

s = Template('$x, val $x!')
print(s.substitute(x='shashi'))

if count > 12:
    print(count, "is postive")
else:
    print("less than 12")


# print("Lower CASE  :", "SHASHI Kumar".lower())


def my_function(names, age=34):
    # name ="shush kumar";  # type: str
    # print("My name is :", names, "and my age is :", age)
    return names


# print("Result ", Cal.sub(2536, 55))

# print("Function return value : " + my_function("shashi"))

y = 10
x = 12

word_string = f'{x} plus {y} equals : {x + y}'

# print(word_string)

x = lambda a: a + 10
print('Examples --> ',x(5))

for x in range(2):
    print("Test :", random.randrange(0, 20))

d1 = Dog("123", "12")
d2 = Dog("456", "12")
d3 = Dog("789", "12")

# print(d1.description())

list = [d1, d2, d3]

for x in list:
    print(x.description())

# print(list.__getitem__(0).description())
