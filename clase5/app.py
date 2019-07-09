import sqlite3  #base de datos ligera
from flask import Flask  #jala flask
from flask import render__template #convierte python en html y viceversa
import os #ayuda a mejorar la comunicacion entre archivos en la app 
from flask_sqlalchemy import SQLAlchemy #ejecutar codigo SQL

app= Flask (__name__) #archivo que va a controlar los demas scripts, es una variable “app”

direccion = "sqlite:///" + os.path.abspath(os.getcwd())+"databe.db" #se da la direccion de la BD

app.config ["SQLALCHEMY_DATABASE_URI"] = direccion #configura la variable app y la direccion de la BD

@app.route('/')
def introduccion():
    return  render_template("index.html")

if  __name__ == '__main__':
    app.run(debug=True)