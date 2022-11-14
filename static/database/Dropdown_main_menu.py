import sqlalchemy
from .db_session import SqlAlchemyBase


class Dropdown_main_menu(SqlAlchemyBase):
    __tablename__ = 'dropdown_main_menu'

    id_elem_menu = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    url_page = sqlalchemy.Column(sqlalchemy.String, nullable=True)
