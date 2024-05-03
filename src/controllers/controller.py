from flask.views import MethodView
from flask import request, render_template, redirect

class IndexController(MethodView):
    def get(self):
        return render_template('public/index.html');

    def post(self):
        codigoPaciente = request.form['codigoPaciente'],
        CPF = request.form['CPF'],
        nome = request.form['nome'],
        dataNascimento = request.form['dataNascimento'],
        idade = request.form['idade'],
        codigoColetaPaciente = request.form['codigoColetaPaciente']

        print(codigoPaciente, CPF, nome, dataNascimento, idade, codigoColetaPaciente)
        return "Paciente cadastrado com sucesso!"

