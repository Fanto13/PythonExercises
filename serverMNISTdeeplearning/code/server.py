import flask
import torch
import os
# model = torch.jit.load("traced_linear.pt")

model_path = os.path.join(os.path.dirname(__file__), "traced_conv.pt")
model = torch.jit.load(model_path)

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("mnist.html")

@app.route("/predict", methods=["POST", "OPTIONS"])

def predict():
    image = flask.request.get_json()["image"]
    image = torch.tensor(image)

    y = model(image)
    print(y.argmax())

    return "ciao"


app.run("0.0.0.0", 5000, True)