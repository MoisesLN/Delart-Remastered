from typing import List

from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(120), nullable=False)
    lavagens: Mapped[List["Lavagem"]] = relationship("Lavagem", back_populates="cliente")

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(120), nullable=False)
    lavagens: Mapped[List["Lavagem"]] = relationship("Lavagem", back_populates="funcionario")

class Lavagem(Base):
    __tablename__ = "lavagens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    nome_veiculo: Mapped[str] = mapped_column(String(40))
    data: Mapped[DateTime] = mapped_column(DateTime)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False)
    funcionario_id: Mapped[int] = mapped_column(ForeignKey("funcionarios.id"), nullable=False)
    cliente: Mapped['Cliente'] = relationship('Cliente', back_populates='lavagens')
    funcionario: Mapped['Funcionario'] = relationship('Funcionario', back_populates='lavagens')