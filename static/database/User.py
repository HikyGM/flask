import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id_user = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # unique=True,
    password_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email_user = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    first_name_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    last_name_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age_user = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    gender_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    path_im_user = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='up.png')
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city_user = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id = id_user

    def set_password(self, password):
        self.password_user = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_user, password)
