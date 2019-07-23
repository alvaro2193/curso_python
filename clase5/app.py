import sqlite3  #base de datos ligera
from flask import Flask  #jala flask
from flask import render_template #convierte python en html y viceversa
import os #ayuda a mejorar la comunicacion entre archivos en la app 
from flask_sqlalchemy import SQLAlchemy #ejecutar codigo SQL
from flask import request

app= Flask (__name__) #archivo que va a controlar los demas scripts, es una variable “app”

direccion = "sqlite:///" + os.path.abspath(os.getcwd())+"database.db" #se da la direccion de la BD

app.config ["SQLALCHEMY_DATABASE_URI"] = direccion #configura la variable app y la direccion de la BD


def get_db ():    #funcion de base de datos
    db = getattr(g,'_database',None) #variable local, crea una BD si esta None
    if db is None:
        db = g._database = sqlite3.connect(direccion) #conecto a la base de datos
        db.row_factory = sqlite3.Row #agrega fila
    return db



@app.route('/agregar',methods=['GET','POST']) #app asi se llama el programa, @app route para poner la direccion, 


def agregar():
    if request.methods == "GET":
        return  render_template("paginaagregar.html", comida=None)

    if request.methods == "POST":
        comida = request.form.to_dict()
        values = [comida ['fecha'], comida ['lugar'], comida ['tipo'] comida ['monto']] 
        change_db ("INSERT INTO comida (fecha, lugar, tipo, monto) VALUES (?,?,?,?)",values) #lo que esta dentro de "" es lenguaje es SQL
    return render_template ('exito.html')





