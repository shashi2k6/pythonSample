import sys
from collections import namedtuple

from main import a


class Employee:

    def __init__(self, first):
        self.first = first

    def update(self):
        self.first = "Kumar"


emp_1 = Employee('shashi')

print(emp_1.first)
emp_1.update()
print(emp_1.first)
print("-------------")

print(sys.version_info)
