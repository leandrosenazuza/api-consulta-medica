from flask.views import MethodView
from flask import request, render_template, redirect, flash

from src import db
from src.model.ColetaPaciente import ColetaPaciente
from src.model.paciente import Paciente


class IndexController(MethodView):
    def get(self):
        data = Paciente.query.all()  # Consulta todos os pacientes
        dataColeta = ColetaPaciente.query.all()  # Consulta todas as coletas de pacientes
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
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM sys.TAB_PACIENTES WHERE codigoPaciente=%s", code)
            cur.connection.commit()
        return redirect('/')


class UpdatePacienteController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM sys.TAB_PACIENTES WHERE codigoPaciente=%s", code)
            paciente = cur.fetchone()
        return render_template('public/update.html', paciente=paciente)

    def post(self, code):
        CPF = request.form['CPF'],
        nome = request.form['nome'],
        dataNascimento = request.form['dataNascimento'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        with mysql.cursor() as cur:
            cur.execute(
                "UPDATE sys.TAB_PACIENTES SET CPF=%s, nome=%s, dataNascimento=%s,codigoColetaPaciente=%s WHERE codigoPaciente =%s",
                (CPF, nome, dataNascimento, codigoColetaPaciente, code))
            cur.connection.commit()
            return redirect('/')


class CreatePacienteController(MethodView):
    def post(self):
        codigoPaciente = request.form['codigoPaciente'],
        CPF = request.form['CPF'],
        nome = request.form['nome'],
        dataNascimento = request.form['dataNascimento'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO sys.TAB_PACIENTES(codigoPaciente, CPF,nome,dataNascimento,codigoColetaPaciente) VALUES(%s, %s, %s, %s, %s, %s)",
                    (codigoPaciente, CPF, nome, dataNascimento, codigoColetaPaciente))
                cur.connection.commit()
                flash('Paciente cadastrado com sucesso!', 'sucess')
            except:
                flash('Este paciente não foi cadastrado!', 'error')
            return redirect('/')


class ColetaPacienteController(MethodView):
    def get(self):
        return render_template("public/coleta.html")


class GetPacienteController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            parteNomeBuscado = request.args.get('nomePaciente')
            cur.execute("SELECT * FROM sys.TAB_PACIENTES WHERE nome LIKE %s", ('%' + parteNomeBuscado + '%',))
            pacientesFiltrados = cur.fetchall()
            return render_template('public/index.html', pacientesFiltrados=pacientesFiltrados)


"""
    def get(self):
        with mysql.cursor() as cur:
        cur.execute("SELECT * FROM sys.TAB_PACIENTES")
        data = cur.fetchall()
        cur.execute("SELECT * FROM sys.TAB_COLETA_PACIENTE")
        dataColeta = cur.fetchall()
        return render_template('public/index.html', data=data, dataColeta=dataColeta);
        
     def post(self):
        codigoPaciente = request.form['codigoPaciente'],
        CPF = request.form['CPF'],
        nome = request.form['nome'],
        dataNascimento = request.form['dataNascimento'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO sys.TAB_PACIENTES(codigoPaciente, CPF,nome,dataNascimento,codigoColetaPaciente) VALUES(%s, %s, %s, %s, %s, %s)",
                    (codigoPaciente, CPF, nome, dataNascimento
                    , codigoColetaPaciente))
                cur.connection.commit()
                flash('Paciente cadastrado com sucesso!', 'sucess')
            except:
                flash('Este paciente não foi cadastrado!', 'error')
            return redirect('/')    
"""