import sqlalchemy
from .db_session import SqlAlchemyBase


class Gallery(SqlAlchemyBase):
    __tablename__ = 'gallery'

    id_gallery = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    path_im = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
