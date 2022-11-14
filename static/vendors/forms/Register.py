from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,SubmitField, EmailField, RadioField, DateField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    genders = RadioField('Пол', validators=[DataRequired()],
                        choices=[('male', 'МУЖ'), ('female', 'ЖЕН')])
    age = DateField('Возраст', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    phone_number = IntegerField('Номер телефона', validators=[DataRequired()])
    submit = SubmitField('Войти')
