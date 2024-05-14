from sqlalchemy import Column, Integer, JSON, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Base
from src.model.Paciente import Paciente


class ColetaPaciente(Base):
    __tablename__ = 'TAB_COLETA_PACIENTE'

    codigoColetaPaciente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    coletaAnos = Column(JSON, default=[])
    ultimaColeta = Column(Date)
    proximaColeta = Column(Date)

    coleta_pacientes = relationship(Paciente, backref="coletaPaciente")


    def __repr__(self):
        return f"<ColetaPaciente {self.codigoColetaPaciente}>"
