#è una libreria che permette di creare un server web, rapido, performante e minimale
import flask


app = flask.Flask(__name__) #dentro la libreria c'è un oggetto di tipo name



@app.route('/')
def hello_world():
        risposta = "" 
        for i in range(10):
            risposta += f"<h{i}>{i}<h{i}>"
        return risposta
    
@app.route('/pagina1')
def pagina1():
    content = ""
    with open("code/pagina1.html") as file:
        content =  file.read()
    return content

@app.route('/pagina2')
def pagina2():
    return flask.render_template("pagina2.html")#fa direttamente un fopen e apre il file
   
app.run("0.0.0.0", 8080)