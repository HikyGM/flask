import sqlalchemy
from .db_session import SqlAlchemyBase


class Main_menu(SqlAlchemyBase):
    __tablename__ = 'menu'

    id_elem_menu = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    url_page = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    icon = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    dropdown = sqlalchemy.Column(sqlalchemy.String, default='')
    parent = sqlalchemy.Column(sqlalchemy.Integer, default=0)
