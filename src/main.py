from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)

# Configuração do banco de dados
dbname = 'db'
user = 'postgres'
password = 'postgres'
host = 'db'
port = '5432'

# Criação de uma instância da classe Database
db = Database(dbname, user, password, host, port)


@app.route('/students', methods=['POST'])
def register_student():
    student_data = request.get_json()
    registration_number = db.register_student(student_data)
    return jsonify({'registration_number': registration_number}), 201


@app.route('/students/<registration_number>', methods=['GET'])
def get_student(registration_number):
    student = db.get_student_by_registration(registration_number)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Estudante não encontrado.'}), 404


@app.route('/students/search', methods=['GET'])
def search_students():
    name = request.args.get('name')
    students = db.get_students_by_name(name)
    return jsonify(students)


@app.route('/students', methods=['GET'])
def get_all_students():
    students = db.get_all_students()
    return jsonify(students)


@app.route('/disciplines', methods=['POST'])
def register_discipline():
    discipline_data = request.get_json()
    db.register_discipline(discipline_data)
    return jsonify({'message': 'Disciplina cadastrada com sucesso.'}), 201


@app.route('/enroll', methods=['POST'])
def enroll_student():
    enrollment_data = request.get_json()
    registration_number = enrollment_data['registration_number']
    discipline_code = enrollment_data['discipline_code']
    discipline_class_number = enrollment_data['discipline_class_number']
    db.enroll_student_in_discipline(registration_number, discipline_code, discipline_class_number)
    return jsonify({'message': 'Estudante matriculado na disciplina com sucesso.'}), 201


@app.route('/students/<registration_number>/disciplines', methods=['GET'])
def get_student_disciplines(registration_number):
    disciplines = db.get_disciplines_by_student(registration_number)
    return jsonify(disciplines)


@app.route('/disciplines/<discipline_code>/<discipline_class_number>/students', methods=['GET'])
def get_discipline_students(discipline_code, discipline_class_number):
    students = db.get_students_by_discipline(discipline_code, discipline_class_number)
    return jsonify(students)


if __name__ == '__main__':
    app.run()
