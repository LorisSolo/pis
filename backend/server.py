from flask import Flask, jsonify, make_response, request
from db_connector import add_student, remove_student, increase_attendance, get_students
from flask_cors import CORS

server = Flask(__name__)
cors = CORS(server, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PATCH", "DELETE"]}})

@server.route("/students", methods=["POST"])
def route_add_student():
    try:
        
        add_student(
            request.json['first_name'],
            request.json['last_name'],
            request.json['birth_date']
        )

        response = {"response": "Success"}
        return make_response(jsonify(response), 201)
    
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)



@server.route("/students", methods=["GET"])
def route_get_students():
    try:
        response = get_students(request.args.get('minAttendance'))
        return make_response(jsonify(response), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)




@server.route("/students", methods=["PATCH"])
def route_increase_attendance():
    try:
        
        increase_attendance(request.json['id'])

        return make_response(jsonify({'response': 'Success'}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)




@server.route("/students", methods=["DELETE"])
def route_remove_student():
    try:
        remove_student(request.json['id'])

        return make_response(jsonify({'response': 'Success'}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)



if __name__ == "__main__":
    server.run(port=8080)
