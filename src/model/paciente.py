from flask_sqlalchemy import SQLAlchemy
from app import db  # Importa o objeto db configurado na sua aplicação Flask

class Paciente(db.Model):
    __tablename__ = 'TAB_PACIENTES'

    codigoPaciente = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    CPF = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(90), nullable=False)
    dataNascimento = db.Column(db.Date)
    codigoColetaPaciente = db.Column(db.Integer, db.ForeignKey('TAB_COLETA_PACIENTE.codigoColetaPaciente'), nullable=True)

    # Relacionamento com a tabela TAB_COLETA_PACIENTE
    coleta_paciente = db.relationship('ColetaPaciente', back_populates='pacientes')

    def __repr__(self):
        return f"<Paciente {self.nome}>"
