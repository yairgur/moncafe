import sqlite3
import os
import atexit
import sys
import DTO
import DAO
from Repository import _Repository

if os.path.exists('moncafe.db'):
    os.remove('moncafe.db')
#database = sqlite3.connect('moncafe.db')

repo = _Repository()


inputFile = open(sys.argv[1], 'r')
repo.create_tables()

for line in inputFile:
    if line.split(", ")[0] == 'E':
        type, id, name, salary, coffee_stand = line.split(", ")
        employee = Employee(id, name, salary, coffee_stand)
    elif line.split(", ")[0] == 'S':
        type, id, name, contact_information = line.split(", ")
        supplier = Supplier(id, name, contact_information)
    elif line.split(", ")[0] == 'P':
        type, id, description, price, quantity = line.split(", ")
        product = Product(id, description, price, quantity)
    elif line.split(", ")[0] == 'C':
        type, id, location, number_of_employees = line.split(", ")
        coffee_stand = Coffee_stand(id, location, number_of_employees)

    def split(self, inputFile):
        i = 1

repo._close()
