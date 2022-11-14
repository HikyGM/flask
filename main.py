from flask import Flask, render_template, redirect
import sqlite3
from static.database import db_session
from static.database.Main_menu import Main_menu
from static.database.User import User
from static.database.Categories import Categories
from flask_login import LoginManager, login_user, login_required, logout_user
from static.vendors.forms.Login import LoginForm
from static.vendors.forms.Register import RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'bfy45ue7iuyilutgbkwycu4b7e46ytwu4etriuw34yiuitwyeiut54'


def categories():
    db_sess = db_session.create_session()
    return db_sess.query(Categories).all()


def main_menu():
    menu_dict = dict()
    db_sess = db_session.create_session().query(Main_menu).all()
    for item in db_sess:
        if item.parent == 0:
            menu_dict[item.id_elem_menu] = [item]
            continue
        menu_dict[item.parent].append(item)
    print(menu_dict)
    return menu_dict


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


def rend(url, title, page, **kwargs):
    return render_template(url, title=title, page=page, main_menu=main_menu(), **kwargs)


@app.route('/')
@app.route('/index')
def index():
    return rend('index.html', 'Главная', 'index', categories=categories())


@app.route('/calendar')
def calendar():
    return rend('index.html', 'Запись', 'calendar')


@app.route('/contacts')
def contacts():
    return rend('index.html', 'Контакты', 'contacts')


@app.route('/profile')
def profile():
    form = RegisterForm()
    return rend('index.html', 'Профиль', 'profile', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email_user == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return rend('login.html', 'Авторизация', 'login', message="Неправильный логин или пароль", form=form)
    return rend('login.html', 'Авторизация', 'login', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return rend('register.html', 'Регистрация', 'register', form=form, message="Пароли не совпадают",
                        error_pass='border-color: red;')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email_user == form.email.data).first():
            return rend('register.html', 'Регистрация', 'register', form=form, message="Такой пользователь уже есть",
                        error_email='border-color: red;')
        user = User(
            email_user=form.email.data,
            login_user=form.login.data,
            first_name_user=form.first_name.data,
            last_name_user=form.last_name.data,
            gender_user=form.genders.data,
            age_user=form.age.data,
            phone_number=form.phone_number.data,
            city_user=form.city.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return rend('register.html', 'Регистрация', 'register', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/gallery')
def gallery():
    con = sqlite3.connect('static/database/database.db')
    cur = con.cursor()
    query = 'SELECT path_im FROM gallery'
    res = cur.execute(query).fetchall()
    return rend('index.html', 'Галлерея', 'gallery', gallery=res)


def main():
    db_session.global_init("static/database/database.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
