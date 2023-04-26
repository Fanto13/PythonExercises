#è una libreria che permette di creare un server web, rapido, performante e minimale
import flask
import json

app = flask.Flask(__name__) #dentro la libreria c'è un oggetto di tipo name

@app.route('/')
def hello_world():
        risposta = "" 
        for i in range(10):
            risposta += f"<h{i}>{i}<h{i}>"
        return risposta
    
# con @ definisco un decorator che aggiunge una funzionalità ad una funzione
@app.route("/pagina0")
def pagina0():
    return "Ciao"
    
# con @ definisco un decorator che aggiunge una funzionalità ad una funzione   
@app.route('/pagina1')
def pagina1():
    content = ""
    with open("code/pagina1.html") as file:
        content =  file.read()
    return content

@app.route('/pagina2')
def pagina2():
    return flask.render_template("pagina2.html")#fa direttamente un fopen e apre il file

@app.route('/calcolatrice', methods =["POST","GET"])
def calcolatrice():
    return flask.render_template("calcolatrice.html")#fa direttamente un fopen e apre il file

@app.route('/calcolatriceAPI', methods =["POST","GET"])#deve poter accettare anche parametri POST
def calcolatriceAPI():
    GET = flask.request.args #per leggere i parametri GET
    POST = flask.request.get_json() #per leggere i parametri post
    numero1 = float(POST["numero1"])
    numero2 = float(POST["numero2"])
    operazione = POST["operazione"]
    
    if operazione == "+":
        risultato = numero1 + numero2
    if  operazione == "-":
        risultato = numero1 - numero2
    if  operazione == "*":
        risultato = numero1 * numero2
    if  operazione == "/":
        risultato = numero1 / numero2
    
    if  operazione == "power":
        risultato = numero1 ** numero2
    
    if  operazione == "root":
        risultato = numero1 ** (1/numero2)
        
    return json.dumps(risultato) #converte un dizionario in una stringa json

@app.route('/static/<path:path>')
def send_static(path):
    #possiamo avere dei path dinamici
    return flask.send_from_directory('static', path)
    #return flask.send_from_directory('static', path)
app.run("0.0.0.0", 8080, True)