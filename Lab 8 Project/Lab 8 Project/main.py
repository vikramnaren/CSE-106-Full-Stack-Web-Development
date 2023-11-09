from flask import Flask,request, render_template, redirect, url_for
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager, login_required,login_user, current_user,logout_user
from models import db, User, Teacher,Student,Course,Enrollment

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SECRET_KEY"] = "cse106"

bcrypt=Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(uid):
    return db.session.get(User, int(uid))

class AuthedMV(ModelView):  
    def is_accessible(self):
        if(current_user.is_authenticated and current_user.is_admin):
            return True
        return False
    
class UserMV(AuthedMV):
    column_list=('name','pw','teacher','student','is_admin')

admin = Admin(app)

admin.add_view(UserMV(User,db.session))
admin.add_view(AuthedMV(Teacher,db.session))
admin.add_view(AuthedMV(Student,db.session))
admin.add_view(AuthedMV(Course,db.session))
admin.add_view(AuthedMV(Enrollment,db.session))

class LoginForm(FlaskForm):
    username=StringField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"Username"})
    password=PasswordField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"Password"})
    submit = SubmitField("login")
    
@app.route('/')
def index():
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        user = User.query.filter_by(name=form.username.data).first()
        if(user):
            if(bcrypt.check_password_hash(user.pw, form.password.data)):
                login_user(user)
                is_teacher = Teacher.query.filter_by(user_id=user.id).first()
                if user.is_admin:
                    return redirect('/admin')
                if(is_teacher):
                    return redirect(url_for('teacher'))
                else:
                    return redirect(url_for('student'))
    return render_template('login.html',form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/student')
@login_required
def student():
    res = db.session.query(Enrollment,Student, User,Course).filter(Student.user_id==User.id).filter(Enrollment.student_id == Student.id).filter(Course.id == Enrollment.course_id).filter(User.id == current_user.id).all()
    temp = db.session.query(Course,Teacher, User).filter(Course.teacher_id==Teacher.id).filter(Teacher.user_id==User.id).all()
    student_name = db.session.query(Student,User).filter(Student.user_id==User.id).filter(User.id==current_user.id).first()[0].name
    others = []
    arr = []
    for r in res:
        enroll = db.session.query(Enrollment,Course).filter(Enrollment.course_id==Course.id).count()
        arr.append({'name':r[3].name,'teacher':r[3].teacher.name,'time':r[3].time,'enrollment':str(enroll)+'/'+str(r[3].capacity)})
    for t in temp:
        enroll = db.session.query(Enrollment,Course).filter(Enrollment.course_id==Course.id).count()
        others.append({
                        'id':t[0].id,
                        'name':t[0].name,
                       'teacher':t[0].teacher.name,
                       'time':t[0].time,
                       'enrollment':str(enroll)+'/'+str(t[0].capacity), 
                       'enrolled': any([course['name']==t[0].name for course in arr])})
    return render_template('student.html', courses=arr, others = others,student_name = student_name)

@app.route('/student/remove', methods=['POST'])
@login_required
def rm_student():
    data = request.form['course']
    stud=db.session.query(Enrollment,Course,Student,User).filter(Enrollment.course_id==Course.id).filter(Enrollment.student_id==Student.id).filter(Enrollment.course_id==data).filter(Student.user_id==current_user.id).first()
    db.session.delete(stud[0])
    db.session.commit()
    return redirect('/student')

@app.route('/student/add', methods=['POST'])
@login_required
def add_student():
    data = request.form['course']
    stud = db.session.query(Student).filter(Student.user_id==current_user.id).first()
    
    en = Enrollment(course_id=int(data),student_id=int(stud.id),grade = -1)
    db.session.add(en)
    db.session.commit()
    return redirect('/student')

@app.route('/teacher')
@login_required
def teacher():
    temp = db.session.query(Course,Teacher, User).filter(Teacher.user_id==User.id).filter(User.id==current_user.id).all()
    arr=[]
    for t in temp:
        enroll = db.session.query(Enrollment,Course).filter(Enrollment.course_id==Course.id).count()

        arr.append({
                       'id':t[0].id,
                       'name':t[0].name,
                       'teacher':t[0].teacher.name,
                       'time':t[0].time,
                       'enrollment':str(enroll)+'/'+str(t[0].capacity)
                       })
    return render_template('teacher.html',courses=arr)

@app.route('/teacher/<id>',methods=['GET','POST'])
@login_required
def grades(id):
    if request.method=='GET':
        temp = db.session.query(Enrollment, Course, Student).filter(Enrollment.course_id==Course.id).filter(Enrollment.student_id==Student.id).filter(Course.id==id).all()
        arr=[]
        for t in temp:
            arr.append({'id':t[0].id,'name':t[2].name,'grade':t[0].grade,'cname':t[1].name})
    elif request.method == 'POST':
         temp = db.session.query(Enrollment).filter(Enrollment.id == request.form['id']).first()
         temp.grade = int(request.form['grade'])
         db.session.commit()
         return redirect('/teacher/'+id)
    return render_template('grades.html',grade_arr=arr,cid=id)


if __name__ == '__main__':
    db.init_app(app)
    app.run()