import pickle

from flask import Flask


app = Flask(__name__)

#import model
model = open('./classifier.pkl', 'rb')
clf = pickle.load(model)


@app.route("/ping")
def hello_world():
    return "<h1>Pinging the model file</h1>"