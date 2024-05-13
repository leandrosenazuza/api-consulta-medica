from uuid import uuid4

from flask.views import MethodView
from flask import request, render_template, redirect, flash

from src import db
from src.db import session
from src.model.ColetaPaciente import ColetaPaciente
from src.model.Paciente import Paciente

class IndexController(MethodView):
    def get(self):
        data = session.query(Paciente).all()
        dataColeta = session.query(ColetaPaciente).all()
        return render_template('public/index.html', data=data, dataColeta=dataColeta)

    def post(self):
        codigoPaciente = request.form.get('codigoPaciente')
        CPF = request.form.get('CPF')
        nome = request.form.get('nome')
        dataNascimento = request.form.get('dataNascimento')
        codigoColetaPaciente = request.form.get('codigoColetaPaciente')

        # Criar um novo objeto Paciente com os dados do formulário
        novo_paciente = Paciente(
            codigoPaciente=codigoPaciente,
            CPF=CPF,
            nome=nome,
            dataNascimento=dataNascimento,
            codigoColetaPaciente=codigoColetaPaciente
        )

        try:
            # Adicionar o novo paciente ao banco de dados
            db.session.add(novo_paciente)
            db.session.commit()

            flash('Paciente cadastrado com sucesso!', 'success')
        except Exception as e:
            # Reverter a transação em caso de erro
            db.session.rollback()
            flash('Este paciente não foi cadastrado!', 'error')
            print(f"Erro ao cadastrar paciente: {e}")

        # Redirecionar para a página inicial
        return redirect('/')

class DeletePacienteController(MethodView):
    def post(self, code):
        paciente = session.query(Paciente).get(code)
        if paciente:
            db.session.delete(paciente)
            db.session.commit()
        return redirect('/')

class UpdatePacienteController(MethodView):
    def get(self, code):
        paciente = session.query(Paciente).get(code)
        return render_template('public/update.html', paciente=paciente)

    def post(self, code):
        paciente = session.query(Paciente).get(code)
        if paciente:
            paciente.CPF = request.form['CPF']
            paciente.nome = request.form['nome']
            paciente.dataNascimento = request.form['dataNascimento']
            paciente.codigoColetaPaciente = request.form['codigoColetaPaciente']
            db.session.commit()
        return redirect('/')

class CreatePacienteController(MethodView):
    def post(self):
        CPF = request.form['CPF']
        nome = request.form['nome']
        dataNascimento = request.form['dataNascimento']

        try:
            # Cria um novo paciente
            novo_paciente = Paciente(
                CPF=CPF,
                nome=nome,
                dataNascimento=dataNascimento
            )

            # Adiciona o novo paciente ao banco de dados
            db.session.add(novo_paciente)
            db.session.commit()

            flash('Paciente cadastrado com sucesso!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Este paciente não foi cadastrado!', 'error')
            print(f"Erro ao cadastrar paciente: {e}")

        return redirect('/')

class ColetaPacienteController(MethodView):
    def get(self):
        return render_template("public/coleta.html")

class GetPacienteController(MethodView):
    def get(self):
        parteNomeBuscado = request.args.get('nomePaciente')
        pacientesFiltrados = session.query(Paciente).filter(Paciente.nome.like(f'%{parteNomeBuscado}%')).all()

        for paciente in pacientesFiltrados:
            paciente.coleta = session.query(ColetaPaciente).filter_by(codigoColetaPaciente=paciente.codigoColetaPaciente).first()


        return render_template('public/index.html', pacientesFiltrados=pacientesFiltrados)


class AtualizarColetaController(MethodView):
    def get(self, code):
        coleta = session.query(ColetaPaciente).get(code)
        return render_template('public/update.html', coleta=coleta)

    def post(self, code):
        coleta = session.query(ColetaPaciente).get(code)
        if coleta:
            coleta.coletaAnos = request.form['coletaAnos']
            coleta.ultimaColeta = request.form['ultimaColeta']
            coleta.proximaColeta = request.form['proximaColeta']
            db.session.commit()
        return redirect('/')


