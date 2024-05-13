from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Base


class Paciente(Base):
    __tablename__ = 'TAB_PACIENTES'

    codigoPaciente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    CPF = Column(String(11), nullable=False)
    nome = Column(String(90), nullable=False)
    dataNascimento = Column(Date)
    codigoColetaPaciente = Column(Integer, ForeignKey('TAB_COLETA_PACIENTE.codigoColetaPaciente'), nullable=True)

    # Relacionamento com a tabela TAB_COLETA_PACIENTE
    coleta_paciente = relationship('ColetaPaciente', back_populates='paciente')

    def __repr__(self):
        return f"<Paciente {self.nome}>"
