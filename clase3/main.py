from  flask import flask

app = Flask (__name__)
@app.route(‘/’)
def inicio ():
    return (“hola”)
app.run (host=’0.0.0.0’)
