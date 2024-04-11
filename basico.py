from flask import Flask , render_template

app = Flask("Pagina")

@app.route('/')

def pagina():
    return render_template ("pagina.html")