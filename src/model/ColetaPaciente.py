from sqlalchemy import Column, Integer, JSON, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Base


class ColetaPaciente(Base):
    __tablename__ = 'TAB_COLETA_PACIENTE'

    codigoColetaPaciente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    coletaAnos = Column(JSON, nullable=False)
    ultimaColeta = Column(Date)
    proximaColeta = Column(Date)


    def __repr__(self):
        return f"<ColetaPaciente {self.codigoColetaPaciente}>"
