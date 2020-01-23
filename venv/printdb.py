database = sqlite3.connect('moncafe.db')
cursor = database.cursor()

def printdb():
    print("employees")
    for item in cursor.execute("SELECT * FROM employees"):
        print(item)
    print("suppliers")
    for item in cursor.execute("SELECT * FROM suppliers"):
        print(item)
    print("products")
    for item in cursor.execute("SELECT * FROM products"):
        print(item)
    print("coffee_stands")
    for item in cursor.execute("SELECT * FROM coffee_stands"):
        print(item)
    print("activities")
    for item in cursor.execute("SELECT * FROM activities"):
        print(item)


