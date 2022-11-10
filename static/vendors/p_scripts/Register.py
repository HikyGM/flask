from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, RadioField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    first_name = StringField('Логин', validators=[DataRequired()])
    last_name = StringField('Логин', validators=[DataRequired()])
    gender = RadioField('Логин', validators=[DataRequired()])
    submit = SubmitField('Войти')