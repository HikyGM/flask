from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from static.database.Gallery import Gallery
from static.database.Main_menu import Main_menu
from static.database.User import User
from static.database import db_session
from static.database.Blog import Blog
from static.database.Products import Products
from static.database.Shopping_cart import Shopping_card

from static.vendors.forms.Login import LoginForm
from static.vendors.forms.Register import RegisterForm

application = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(application)
application.config['SECRET_KEY'] = 'bfy45ue7iuyilutgbkwycu4b7e46ytwu4etriuw34yiuitwyeiut54'


def posts():
    db_sess = db_session.create_session()
    return db_sess.query(Blog).order_by(Blog.id_post.desc())


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


def rend(url, title, page, **kwargs):
    return render_template(url, title=title, page=page, main_menu=main_menu(), **kwargs)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@application.errorhandler(404)
def http_404_handler(error):
    return render_template('error_pages/404.html'), 404


@application.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@application.route('/')
@application.route('/index')
def index():
    main()
    return rend('index.html', 'Главная', 'index', posts=posts())


@application.route('/calendar')
def calendar():
    return rend('index.html', 'Запись', 'calendar')


@application.route('/pricing')
def pricing():
    return rend('index.html', 'Цены', 'pricing')


@application.route('/contacts')
def contacts():
    return rend('index.html', 'Контакты', 'contacts')


@application.route('/profile')
def profile():
    form = RegisterForm()
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    return rend('index.html', 'Профиль', 'profile', form=form)


@application.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email_user == form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/")
            else:
                return rend('login.html', 'Авторизация', 'login', message=f"Неправильный пароль '{form.password.data}'",
                            form=form)
        else:
            return rend('login.html', 'Авторизация', 'login', message="Неправильный логин", form=form)
    return rend('login.html', 'Авторизация', 'login', form=form)


@application.route('/register', methods=['POST', 'GET'])
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


@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@application.route('/gallery')
def gallery():
    db_sess = db_session.create_session()
    res = db_sess.query(Gallery).all()
    return rend('index.html', 'Галлерея', 'gallery', gallery=res)


@application.route('/products')
def get_all_products():
    db_sess = db_session.create_session()
    res = db_sess.query(Products).all()
    for elem in res:
        print(elem)
    return rend('index.html', 'Меню', 'products', products=res)


@application.route('/products/<int:id_product>', methods=['GET'])
def get_product(id_product):
    db_sess = db_session.create_session()
    res = db_sess.query(Products).filter(Products.id_products == id_product).first()
    print(res)

    return rend('index.html', 'Меню', 'product_info', product=res)


@application.route('/products/<int:id_product>', methods=['POST'])
def post_product(id_product):
    db_sess = db_session.create_session()
    add_card = Shopping_card(
        id_user_card=1,
        id_product=id_product
    )
    db_sess.add(add_card)
    db_sess.commit()
    return redirect('/products')


@application.route('/shopping_card')
def shopping_card():
    db_sess = db_session.create_session()
    res = db_sess.query(Shopping_card).filter(Shopping_card.id_user_card == 1)
    r = db_sess.query(Products).filter(
        Products.id_products.in_(db_sess.query(Shopping_card.id_product).filter(Shopping_card.id_user_card == 1))).all()
    return rend('index.html', 'Корзина', 'shopping_card', products=r)


def main():
    db_session.global_init()


if __name__ == "__main__":
    application.run(host='0.0.0.0')
