import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Products(SqlAlchemyBase):
    __tablename__ = 'products'

    id_products = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_products = sqlalchemy.Column(sqlalchemy.String(100), unique=True, nullable=True)
    text_products = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    cost_products = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    path_im = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, default='placeholder.jpg')

