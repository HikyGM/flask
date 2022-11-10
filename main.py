from flask import Flask, render_template, request, redirect
import sqlite3
from static.database import db_session
from static.database.User import User
from static.database.Categories import Categories
from flask_login import LoginManager, login_user

from static.vendors.p_scripts.Login import LoginForm
from static.vendors.p_scripts.Register import RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'bfy45ue7iuyilutgbkwycu4b7e46ytwu4etriuw34yiuitwyeiut54'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)





@app.errorhandler(404)
def http_404_handler(error):
    return render_template('error_pages/404.html'), 404


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', page='index', categories=categories())


@app.route('/calendar')
def calendar():
    return render_template('index.html', title='Запись', page='calendar')


@app.route('/contacts')
def contacts():
    return render_template('index.html', title='Запись', page='contacts')


@app.route('/login', methods=['POST', 'GET'])
def login():
    print('я тут!!!!!')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email_user == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)





@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', title='Регистрация', form=form)
    if request.method == 'POST':
        if request.form['password'] == request.form['r_password']:
            db_sess = db_session.create_session()
            if not db_sess.query(User).filter(User.email_user == request.form['email']).first():
                user = User()
                user.email_user = request.form['email']
                user.login_user = request.form['login']
                user.password_user = request.form['password']
                user.first_name_user = request.form['first_name']
                user.last_name_user = request.form['last_name']
                user.gender_user = request.form['gender']
                user.set_password(form.password.data)
                db_sess.add(user)
                db_sess.commit()

                return login()
            else:
                return render_template('register.html', title='Регистрация', error_email='border-color: red;')
        else:
            return render_template('register.html', title='Регистрация', error_pass='border-color: red;')


@app.route('/gallery')
def gallery():
    con = sqlite3.connect('static/database/database.db')
    cur = con.cursor()
    query = 'SELECT path_im FROM gallery'
    res = cur.execute(query).fetchall()
    return render_template('index.html', title='Запись', page='gallery', gallery=res)


def main():
    db_session.global_init("static/database/database.db")
    app.run(port=8080, host='127.0.0.1')


def categories():
    db_sess = db_session.create_session()
    return db_sess.query(Categories).all()


if __name__ == '__main__':
    main()
