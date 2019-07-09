""" from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world ():
    return 'Hola amigos de GeeKy Theory'

if __name__ == '__main__':
    app.run (host='0.0.0.0') """

    from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
return "Hello World!"