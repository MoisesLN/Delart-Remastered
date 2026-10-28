from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass


engine = create_engine('sqlite:///database.db')

def inicializar_banco():
    Base.metadata.create_all(bind=engine)

def criar_sessao():
    return Session(bind=engine)
