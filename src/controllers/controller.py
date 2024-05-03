from flask.views import MethodView
from flask import request, render_template, redirect

from src.db import mysql


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM sys.TAB_PACIENTES")
            data = cur.fetchall()
        return render_template('public/index.html', data=data);

    def post(self):
        codigoPaciente = request.form['codigoPaciente'],
        CPF = request.form['CPF'],
        nome = request.form['nome'],
        dataNascimento = request.form['dataNascimento'],
        idade = request.form['idade'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        with mysql.cursor()as cur:
            cur.execute("INSERT INTO sys.TAB_PACIENTES(codigoPaciente, CPF,nome,dataNascimento,idade,codigoColetaPaciente) VALUES(%s, %s, %s, %s, %s, %s)",(codigoPaciente, CPF,nome,dataNascimento,idade,codigoColetaPaciente))
            cur.connection.commit()
            return redirect('/')

class DeletePacienteController(MethodView):
    def get(self, code):
        with mysql.cursor()as cur:
            cur.execute("DELETE FROM sys.TAB_PACIENTES WHERE codigoPaciente=%s)", code)
            cur.connection.commit()
        return redirect('/')

class UpdatePacienteController(MethodView):
    def get(self, code):
        with mysql.cursor()as cur:
        #    cur.execute("UPDATE FROM TAB_PACIENTES SET CPF = %s, nome = %s, dataNascimento = %s, idade = %s, codigoColetaPaciente = %s WHERE codigoPaciente = %s", (CPF, nome, dataNascimento, idade, codigoPaciente))
            cur.connection.commit()
        return redirect('/')

