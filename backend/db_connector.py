from pony.orm.serialization import to_dict # pip install flask, ponyorm
from pony import orm
DB = orm.Database()

class Student(DB.Entity):
    id = orm.PrimaryKey(int, auto=True)
    first_name = orm.Required(str)
    last_name = orm.Required(str)
    birth_date = orm.Required(str)
    attendance = orm.Optional(int)

DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)


def add_student(first_name, last_name, birth_date):
    try:
        with orm.db_session:

            Student(first_name=first_name, last_name=last_name, birth_date=birth_date, attendance=0)

            return {"response": "Success"}
    except Exception as e:
        print (e)
        return {"response": "Fail"}

def remove_student(id):
    try:
        with orm.db_session:

            student = Student.get(id=id)
            if not student:
                return {"response": "Fail"}
            
            student.delete()

            return {"response": "Success"}
    except Exception as e:
        print (e)
        return {"response": "Fail"}


def increase_attendance(id):
    try:
        with orm.db_session:

            student = Student.get(id=id)
            if not student:
                return {"response": "Fail"}

            increase = student.attendance + 1
            setattr(student, 'attendance', increase)

            return {"response": "Success"}
    except Exception as e:
        print (e)
        return {"response": "Fail"}


def get_students(minAttendance=None):
    try:
        with orm.db_session:
            
            students = Student.select()

            if minAttendance is not None:
                minAttendanceInt = int(minAttendance)
                students = filter(lambda s: s.attendance >= minAttendanceInt, students)

            students_list =  [s.to_dict() for s in students]

            return students_list
    except Exception as e:
        print (e)
        return {"response": "Fail"}