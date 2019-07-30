#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

'''os nos permite acceder a funcionalidades dependientes del Sistema Operativo.
Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular 
la estructura de directorios (para leer y escribir archivos)'''

import sqlite3 as sql #es la librería del lenguaje de la base de datos
from flask import Flask, render_template, request


app = Flask(__name__)

#Esta ruta permite poder ingresar al menu principal que es el archivo index.html
@app.route('/')
def home():
   return render_template('index.html')

#Esta ruta es para el formulario que permite ingresar nuevos estudiantes que es el archivo student.html
#TODA ruta que manipule datos de la base de datos, tiene que tener un post o get
@app.route('/enternew') #esta no la tiene porque esta en el archivo student.html <form action = "{{ url_for('addrec') }}" method = "POST">
#A su vez el archivo student.html esta ligado a la route addrec @app.route('/addrec',methods = ['POST', 'GET']) que se encuentra más abajo 
def new_student():
   return render_template('student.html')

#Esta es la ruta addrec que se menciono arriba
@app.route('/addrec',methods = ['POST', 'GET']) #post es para escribir el dato. GET es para ver el dato.
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm'] #nm es el nombre de la variable nombre
         addr = request.form['add'] #add es el nombre de la variable direcion
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con: #databse.db es el nombre de la base de datos que estamos utilizando y nos estamos conectando
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (nm,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) ) #esta insertando en la base de datos, en la tabla students, los campos nm, addr,city, pin
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

#esta ruta muestra todos los datos guardados en la base de datos, ver el archivo list.html
@app.route('/list') #no utiliza el metodo GET, porque se esta conectando directamente mediante el codigo dentro de la función, esto no se recomienda, porque es escribir más código
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)