from sqlalchemy.testing import db

class ColetaPaciente(db.Model):
    __tablename__ = 'TAB_COLETA_PACIENTE'

    codigoColetaPaciente = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    coletaAnos = db.Column(db.JSON, nullable=False)
    ultimaColeta = db.Column(db.Date)
    proximaColeta = db.Column(db.Date)

    pacientes = db.relationship('Paciente', back_populates='coleta_paciente')

    def __repr__(self):
        return f"<ColetaPaciente {self.codigoColetaPaciente}>"
