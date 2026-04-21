from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
next_id = 1

@app.route('/')
def home():
    return "App is working"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()
    student = {
        'id': next_id,
        'name': data['name'],
        'roll': data['roll']
    }
    students[next_id] = student
    next_id += 1
    return jsonify(student), 201

if __name__ == '__main__':
    app.run(debug=True)