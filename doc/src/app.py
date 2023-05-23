from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

if __name__ == "__main__":
    app.run('host' == 'localhost', debug = True)

