import flask
import os
import json
from flask import send_from_directory

app = flask.Flask(__name__)

# Homepage, mostra il form per l'upload dei file
@app.route("/")
def index():
    return flask.render_template("upload.html")

# Pagina di destinazione del form di upload, salva i file nella cartella uploads
@app.route("/uploader", methods=["POST"])
def uploader():
    # uploaded = flask.request.files["file"] 
    uploaded = flask.request.files.getlist("file")
    upload_folder = "uploads"  # Cartella di destinazione dei file
    # print(uploaded.save(f"uploaded/{uploaded.filename}"))
    # Questo supporta anche l'upload di più files
    # Verifica se la cartella "uploads" esiste, altrimenti creala
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    for file in uploaded:
        file.save(os.path.join(upload_folder, file.filename))
    return "Caricamento avvenuto con successo"
# Endpoint per la creazione di una nuova cartella
# Viene chiamato con AJAX quando si crea una nuova cartella nella pagina folders.html
# La cartella viene creata nella cartella uploads
@app.route("/create_folder/<path:path>", methods=["POST"])
def create_folder(path):
    print(path)
    if os.path.exists(f"uploads/{path}"):
        return json.dumps({"success": False, "error": "folder already existing"})
    else:
        os.mkdir(f"uploads/{path}")
        return json.dumps({"success": True, "folder": path})

# Pagina che mostra le cartelle e i file presenti nella cartella uploads
@app.route("/folders/")
def folders():
    return flask.render_template("folders.html")

#  per la lettura del contenuto di una cartella
# Viene chiamato con AJAX quando si clicca su una cartella nella pagina folders.html
# Restituisce una lista con i file e le cartelle contenute nella cartella passata come parametro
@app.route("/read_folder", methods=["POST"])
def read_folder():
    folder = flask.request.get_json()["folder"]
    folder_path = f"uploads/{folder}"
    if os.path.exists(folder_path):
        folder_content = os.listdir(folder_path)
        folders_to_show = []
        files_to_show = []
        for item in folder_content:
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                folders_to_show.append(item)
            if os.path.isfile(item_path):
                files_to_show.append(item)
        return json.dumps({"success": True, "folders": folders_to_show, "files": files_to_show})
    else:
        return json.dumps({"success": False, "error": "La cartella non esiste"})

# Endpoint per il download di un file
# Viene chiamato con AJAX quando si clicca su un file nella pagina folders.html
# Restituisce il file richiesto come download
@app.route("/get_file/<path:path>")
def get_file(path):
    file_path = os.path.normpath(os.path.join("uploads", path))
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path, as_attachment=True)
    else:
        return "File non trovato"
    
@app.route("/delete_file/<path:path>", methods=["POST"])
def delete_file(path):
    file_path = f"uploads/{path}"
    if os.path.exists(file_path):
        os.remove(file_path)
        return json.dumps({"success": True})
    else:
        return json.dumps({"success": False, "error": "Il file non esiste"})
    
# Configura la cartella degli upload come cartella statica
@app.route('/uploads/<path:filename>')
def serve_file(filename):
    return flask.send_from_directory('uploads', filename)


@app.route("/delete_folder/<path:path>", methods=["POST"])
def delete_folder(path):
    folder_path = f"uploads/{path}"
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        return json.dumps({"success": True})
    else:
        return json.dumps({"success": False, "error": "La cartella non esiste"})

app.static_folder = 'static'
# Avvia il server sulla porta 8080 in ascolto su tutte le interfacce
if __name__ == '__main__':
    app.run("0.0.0.0", 8080, True)