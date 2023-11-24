import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Shopping_card(SqlAlchemyBase):
    __tablename__ = 'shopping_card'

    id_shopping_card = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_user_card = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id_user'))
    id_user = orm.relationship('User')

    id_product = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id_products'))
    id_prod = orm.relationship('Products')
