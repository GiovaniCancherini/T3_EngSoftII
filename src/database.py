import psycopg2

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def register_student(self, student_data):
        query = "INSERT INTO students (name, document_number, address) VALUES (%s, %s, %s) RETURNING registration_number"
        self.cursor.execute(query, student_data)
        registration_number = self.cursor.fetchone()[0]
        self.conn.commit()
        return registration_number

    def get_student_by_registration(self, registration_number):
        query = "SELECT * FROM students WHERE registration_number = %s"
        self.cursor.execute(query, (registration_number,))
        student_data = self.cursor.fetchone()
        return student_data

    def get_students_by_name(self, name):
        query = "SELECT * FROM students WHERE name LIKE %s"
        self.cursor.execute(query, ('%' + name + '%',))
        students_data = self.cursor.fetchall()
        return students_data

    def get_all_students(self):
        query = "SELECT * FROM students"
        self.cursor.execute(query)
        students_data = self.cursor.fetchall()
        return students_data

    def register_discipline(self, discipline_data):
        query = "INSERT INTO disciplines (code, name, schedule, class) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, discipline_data)
        self.conn.commit()

    def enroll_student_in_discipline(self, registration_number, discipline_code, discipline_class):
        query = "INSERT INTO enrollments (student_registration, discipline_code, discipline_class) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (registration_number, discipline_code, discipline_class))
        self.conn.commit()

    def get_disciplines_by_student(self, registration_number):
        query = """
            SELECT d.code, d.name, d.schedule, d.class
            FROM disciplines AS d
            INNER JOIN enrollments AS e ON d.code = e.discipline_code AND d.class = e.discipline_class
            WHERE e.student_registration = %s
        """
        self.cursor.execute(query, (registration_number,))
        disciplines_data = self.cursor.fetchall()
        return disciplines_data

    def get_students_by_discipline(self, discipline_code, discipline_class):
        query = """
            SELECT s.registration_number, s.name, s.document_number, s.address
            FROM students AS s
            INNER JOIN enrollments AS e ON s.registration_number = e.student_registration
            WHERE e.discipline_code = %s AND e.discipline_class = %s
        """
        self.cursor.execute(query, (discipline_code, discipline_class))
        students_data = self.cursor.fetchall()
        return students_data