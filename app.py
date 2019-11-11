from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user, current_user
import web_sql
import os, sys
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'
name = 'Tom'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
res = web_sql.search.teacher.teacherName('王')
app = Flask(__name__)
# 定义数据库模型
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'lib.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))
db = SQLAlchemy(app)


class Administrator(db.Model):
    AdminNO = db.Column(db.String(8), primary_key=True)
    AdminName = db.Column(db.String(5), nullable=False)
    Gender = db.Column(db.Integer)
    Phone = db.Column(db.String(11))


class Book(db.Model):
    ISBN = db.Column(db.String(9), primary_key=True)
    BookName = db.Column(db.String(10), nullable=False)
    Writer = db.Column(db.String(8))
    WhereFloor = db.Column(db.String(10))
    State = db.Column(db.String(10))
    Price = db.Column(db.Float)
    PublisherNo = db.Column(db.String(20))


class BookClass(db.Model):
    __tablename__ = 'BookClass'
    ClassNo = db.Column(db.String(4), primary_key=True)
    ClassName = db.Column(db.String(10))


class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    StudentNo = db.Column(db.String(8))
    ISBN = db.Column(db.String(9))
    BorrowDate = db.Column(db.Date)
    ShouldData = db.Column(db.Date)
    ReturnDate = db.Column(db.Date)


class Publisher(db.Model):
    PublisherNo = db.Column(db.String(4), primary_key=True)
    PublisherName = db.Column(db.String(20))
    PublisherDate = db.Column(db.Date)


class Student(db.Model, UserMixin):
    StudentNo = db.Column(db.String(8), primary_key=True)
    StudentName = db.Column(db.String(5), nullable=False)
    Gender = db.Column(db.Integer)
    Class = db.Column(db.String(8))
    Major = db.Column(db.String(10))
    AllBorrowNum = db.Column(db.Integer)
    BorrowNum = db.Column(db.Integer)
    PassWord_Hash = db.Column(db.String(128))

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.PassWOrd_Hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.PassWord_Hash, password)  # 返回布尔值

    def get_id(self):
        return self.StudentNo


class Teacher(db.Model):
    TeacherNo = db.Column(db.String(8), primary_key=True)
    TeacherName = db.Column(db.String(5))
    Gender = db.Column(db.Integer)
    Office = db.Column(db.String(10))
    Phone = db.Column(db.String(11))


login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(student_no):
    studennt = Student.query.get(str(student_no))
    return studennt


@app.route('/')
@login_required
def index():
    return render_template('index.html', name=name, movies=movies, res=res)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))
        student = Student.query.get(str(username))
        if student:
            if check_password_hash(student.PassWord_Hash, password):
                login_user(student, False)  # 登入用户
                flash('Login success.')
                return redirect(url_for('searchbook'))
            else:
                flash('Invalid username or password.')  # 如果验证失败，显示错误消息
                return redirect(url_for('login'))
        else:
            flash('Invalid username or password.')  # 如果验证失败，显示错误消息
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/logout')
@login_required  # 用于视图保护
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    return redirect(url_for('index'))  # 重定向回首页


@app.route('/searchbook/', methods=['GET', 'POST'])
@login_required
def searchbook():
    if request.method == 'POST':
        bookname = request.form.get('bookname')
        author = request.form.get('author')
        return render_template('show.html')
    else:
        return render_template('search.html')


@app.route('/show/', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        bookname = request.form.get('bookname')
        author = request.form.get('author')
        if author.strip() == '':
            resname = web_sql.search.book.book_name(bookname)
            return render_template('show.html', bookname=resname, author=[], result=[])
        if bookname.strip() == '':
            resauthor = web_sql.search.book.writer(author)
            return render_template('show.html', author=resauthor, bookname=[], result=[])
        if author.strip() != '' and bookname.strip() != '':
            result = web_sql.search.book.book_name_author(bookname, author)
            return render_template('show.html', result=result, bookname=[], author=[])
        if author.strip() == '' and bookname.strip() == '':
            return '请输入查询数据！'
    else:
        return 'Please Input Date！'


app.config['DEBUG'] = True
app.run(host='0.0.0.0', port=5000)
