import sqlite3
import sqlite3
import os
import atexit
import sys
from DAO import _Employees
from DAO import _Activities
from DAO import _Coffee_stands
from DAO import _Products
from DAO import _Suppliers
import DTO


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.employees = _Employees(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.products = _Products(self._conn)
        self.coffee_stands = _Coffee_stands(self._conn)
        self.activities = _Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        _conn.executescript("""
        CREATE TABLE employees (
            id      INTEGER         PRIMARY KEY,
            name    TEXT        NOT NULL,
            salary  REAL        NOT NULL,
            coffee_stand    INTEGER REFERENCES Coffee_stand(id)
        );

        CREATE TABLE suppliers (
            id                 INTEGER     PRIMARY KEY,
            name     TEXT    NOT NULL,
            contact_information TEXT
        );

        CREATE TABLE products (
            id      INTEGER     PRIMARY KEY,
            description  TEXT     NOT NULL,
            price           REAL     NOT NULL,
            quantity        INTEGER     NOT NULL
        );
        CREATE TABLE coffee_stands (
            id      INTEGER     PRIMARY KEY,
            location  TEXT     NOT NULL,
            number_of_employees INTEGER
        );
        CREATE TABLE activities (
        product_id  INTEGER REFERENCES Product(id),
        quantity  INTEGER     NOT NULL,
        activator_id    INTEGER     NOT NULL,
        date DATE NOT NULL
    );
    """)




# the repository singleton
repo = _Repository()
atexit.register(repo._close)
