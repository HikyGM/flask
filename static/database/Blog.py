import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Blog(SqlAlchemyBase):
    __tablename__ = 'blog'

    id_post = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_post = sqlalchemy.Column(sqlalchemy.String(100), unique=True, nullable=True)
    author_post = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id_user'))
    data_time_post = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    url_post = sqlalchemy.Column(sqlalchemy.String(150), nullable=True)
    path_im_post = sqlalchemy.Column(sqlalchemy.String(150), nullable=True)
    text_post = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    author = orm.relationship('User')
