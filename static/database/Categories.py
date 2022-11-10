import sqlalchemy
from .db_session import SqlAlchemyBase


class Categories(SqlAlchemyBase):
    __tablename__ = 'categories'

    id_category = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_category = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    url_category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    path_im_category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    comm_category = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)

