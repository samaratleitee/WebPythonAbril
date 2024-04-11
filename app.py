from flask import Flask

app = Flask ("ola")

@app.route("/")
def ola():
    return ("Olá, Mundo!")

@app.route("/aluno")
def aluno():
    return "Eduardo, Samara, Vanessa, Paulo"