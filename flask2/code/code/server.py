import flask
import json

app = flask.Flask(__name__)
#questo è un decorator che aggiunge una funzionalità, in particolare
@app.route("/")
#la funzione index() viene eseguita quando si va all'indirizzo http://localhost:8080/ e renderizza il template index.html
def index():
    return flask.render_template("index.html")
#il primo argomento è l'url, il secondo è il metodo che viene eseguito quando si va all'url
@app.route("/paga", methods=["POST"])
def paga():
    #prende il json che arriva dal client
    carrello = flask.request.get_json()
    for item in carrello:
        print(item)
    #questo serve per dire al client che la richiesta è andata a buon fine, compare nella console del client
    return json.dumps({"success": True})
    
@app.route("/static/<path:path>")
#questo serve per dire al server dove prendere i file statici
def static_files(path):
    flask.send_from_directory("static", path)

app.run("0.0.0.0", 8080, True)