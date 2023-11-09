from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////test.db'
db = SQLAlchemy(app)
CORS(app)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    Name = db.Column(db.String, nullable = True, unique = True)
    Grade = db.Column(db.Integer, nullable = True, unique = False)
    def __init__ (self, Name, Grade):
        self.Name = Name
        self.Grade = Grade



def hello():
    with app.app_context():
        db.create_all()
    return render_template('Gradebook.html')

@app.route('/grades', methods = ['GET'])
def get_grades():
    return CreateJson(Student.query.all()) 

@app.route('/grades/<name>', methods = ['GET'])
def get_student(Name):
    return CreateJson(Student.query.filter_by(Name = Name))

@app.route('/grades' , methods = ['POST'])
def add_student():
    submission = request.get_json()
    Name = submission['name']
#     Grade = submission['grade'] 
#     Student1 = Student(Name, Grade)
#     db.session.add(Student1)
#     db.session.commit()
#     return {Name:Grade}

# @app.route('/grades/<name>', methods = ['PUT'])
# def update_grade(Name):
    submission = request.get_json()
    NewGrade = submission['grade']
    Student1 = Student.query.filter_by(Name = Name)
    Student1 = Student.update(dict(Grade = NewGrade))
    db.session.commit()
    return CreateJson(Student.query.all())

@app.route('/grades/<name>', methods = ['DELETE'])
def delete_student(Name):
    db.session.delete(Student.query.filter_by(Name=Name).first())
    db.session.commit()
    # return CreateJson(Student.query.all())

if __name__ == '__main__':
        app.run()f