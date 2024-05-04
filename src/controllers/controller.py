from flask.views import MethodView
from flask import request, render_template, redirect, flash

from src.db import mysql


class IndexController(MethodView):
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
        idade = request.form['idade'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        with mysql.cursor()as cur:
            try:
                cur.execute("INSERT INTO sys.TAB_PACIENTES(codigoPaciente, CPF,nome,dataNascimento,idade,codigoColetaPaciente) VALUES(%s, %s, %s, %s, %s, %s)",(codigoPaciente, CPF,nome,dataNascimento,idade,codigoColetaPaciente))
                cur.connection.commit()
                flash('Paciente cadastrado com sucesso!', 'sucess')
            except:
                flash('Este paciente não foi cadastrado!', 'error')
            return redirect('/')

class DeletePacienteController(MethodView):
    def post(self, code):
        with mysql.cursor()as cur:
            cur.execute("DELETE FROM sys.TAB_PACIENTES WHERE codigoPaciente=%s", code)
            cur.connection.commit()
        return redirect('/')

class UpdatePacienteController(MethodView):
    def get(self, code):
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM sys.TAB_PACIENTES WHERE codigoPaciente=%s", code)
            paciente = cur.fetchone()
        return render_template('public/update.html', paciente=paciente)

    def post(self,code):
        CPF = request.form['CPF'],
        nome = request.form['nome'],
        dataNascimento = request.form['dataNascimento'],
        idade = request.form['idade'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        with mysql.cursor() as cur:
            cur.execute("UPDATE sys.TAB_PACIENTES SET CPF=%s, nome=%s, dataNascimento=%s, idade=%s,codigoColetaPaciente=%s WHERE codigoPaciente =%s", (CPF, nome, dataNascimento, idade, codigoColetaPaciente, code))
            cur.connection.commit()
            return redirect('/')


class ColetaPacienteController(MethodView):
    def get(self):
        return render_template("public/coleta.html")
