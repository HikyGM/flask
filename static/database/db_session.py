import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()
__factory = None


def global_init():
    global __factory
    if __factory:
        return
    conn_str = "mysql+pymysql://u1835076_default:Ng6ULk3tM1lwYpw8@localhost/u1835076_flask_db"
    engine = sa.create_engine(conn_str)
    __factory = orm.sessionmaker(bind=engine)
    # noinspection PyUnresolvedReferences
    from . import __all_models
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
