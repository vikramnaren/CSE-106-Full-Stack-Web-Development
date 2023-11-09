from flask_sqlalchemy import SQLAlchemy
from flask_login import  UserMixin
db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    pw = db.Column(db.String, unique=True, nullable=False)
    is_admin = db.Column(db.Boolean,default=False)
    teacher = db.relationship("Teacher",backref="user_of_teacher")
    student = db.relationship("Student",backref="user_of_student")
    def __init__(self,name,pw):
        self.name = name
        self.pw = pw

class Teacher(db.Model):
    __tablename__='teacher'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id

class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id

class Course(db.Model):
    __tablename__='course'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship("Teacher", backref=db.backref("course_teacher",uselist=True))
    capacity = db.Column(db.Integer)
    time = db.Column(db.String)
    def __init__(self,name,teacher_id,capacity,time):
        self.name = name
        self.teacher_id = teacher_id
        self.capacity = capacity
        self.time = time

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    course = db.relationship("Course", backref=db.backref("enrollment_course",uselist=True))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", backref=db.backref("enrollment_student",uselist=True))
    grade = db.Column(db.Integer)
    def __init__(self, course_id, student_id, grade):
        self.course_id = course_id
        self.student_id = student_id
        self.grade = grade

if __name__ == '__main__':
    with app.app_context():
        db.create_all()