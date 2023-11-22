import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Shopping_cart(SqlAlchemyBase):
    __tablename__ = 'shopping_cart'

    id_shopping_cart = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
