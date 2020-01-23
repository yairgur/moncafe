class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
               INSERT INTO employees (id, name) VALUES (?, ?)
           """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM employees WHERE id = ?
        """, [employee_id])

        return Employee(*c.fetchone())


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (num, expected_output) VALUES (?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,expected_output FROM suppliers WHERE num = ?
            """, [id])

        return Supplier(*c.fetchone())


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO products (student_id, assignment_num, grade) VALUES (?, ?, ?)
        """, [product.id, product.description, product.price, product.quantity])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,expected_output FROM products WHERE num = ?
            """, [id])

        return Product(*c.fetchone())


class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
            INSERT INTO coffee_stands (student_id, assignment_num, grade) VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,expected_output FROM coffee_stands WHERE num = ?
            """, [id])

        return Coffee_stand(*c.fetchone())


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activitie):
        self._conn.execute("""
            INSERT INTO activities (student_id, assignment_num, grade) VALUES (?, ?, ?)
        """, [activitie.id, activitie.quantity, activitie.activator_id, activitie.date])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,expected_output FROM coffee_stands WHERE num = ?
            """, [id])

        return Activitie(*c.fetchone())

    # def find_all(self):
    #     c = self._conn.cursor()
    #     all = c.execute("""
    #         SELECT student_id, assignment_num, grade FROM grades
    #     """).fetchall()
    #
    #     return [Product(*row) for row in all]
