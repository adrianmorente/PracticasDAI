#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hola.html')

####################################################################
# Ejercicio 2 - Sirviendo contenido estático
####################################################################

# Puedo acceder a la imagen a través de la URL:
#       http://localhost:8080/static/images/Logo_Python.png
# El siguiente método solo imprime la URL...
@app.route('/image')
def show_image():
    return url_for('static', filename='images/Logo_Python.png')

####################################################################
# Ejercicio 3 - Manejo de URLs
####################################################################

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/user/pepe')
def show_pepe_user():
    return 'Hombre, ¡pepe! Me alegro de verte'

@app.route('/user/zerjillo')
def show_teacher_user():
    return 'Uy, me pongo serio, que viene el profe...\nBuenas tardes, caballero'

@app.route('/user/<username>')
def show_known_user(username):
    return 'Bienvenido, %s' % username

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada... ¿Te has inventado el enlace?", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
