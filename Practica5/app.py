#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request, render_template, session, jsonify
from pymongo import *
import shelve

app = Flask(__name__)
app.secret_key = 'random key for me by myself'

# testing current session
@app.before_request
def try_logged():
    session['logged_in'] = 'username' in session

# showing the whole website (plus login form)
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    if(request.method=='POST'):
        db = shelve.open('users.db')
        user = db.get(request.form['username'], None)
        if user is not None:
            user = user['username']
        password = request.form['password']

        if password == db[user]['password']:
            session['logged_in'] = True
            session['username'] = user
            session['urls'] = []
        else:
            session['logged_in'] = False
        db.close()
    elif not 'username' in session:
        session['logged_in'] = False

    return render_template('index.html', loggedIn=session['logged_in'])

# register form
@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = shelve.open('users.db')
        username = request.form['username']
        password = request.form['password']
        db[username] = { 'username' : username, 'password' : password }
        db.close()
        return redirect(url_for('index'))

    return render_template('register.html')

# popping the username out of the session
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# showing a search form and a table full of restaurants (after searching for them)
@app.route('/restaurants', methods=['GET', 'POST'])
def restaurants():
    return render_template('restaurants.html', loggedIn=session['logged_in'])

@app.route('/search', methods=['GET'])
def search():
    # inicialización de la base de datos y la colección
    client = MongoClient('localhost', 27017)
    db = client['test']
    restaurants = db.restaurants

    # nos quedamos con los parámetros get
    option = request.args.get('field_name', '')
    if(option == 'zipcode'):
        option = 'address.zipcode'
    parameter = request.args.get('parameter', '')

    # en la primera carga, no recibimos número de página
    if(request.args.get('pagina_py', '')):
        page = int(request.args.get('pagina_py', ''))
        query = restaurants.find({ option : parameter }).skip(page*10).limit(10)
        return query
    else:
        query = restaurants.find({ option : parameter }).limit(10)

    return render_template('restaurants.html', loggedIn=session['logged_in'], value=query)

# showing a link to my personal twitter page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', loggedIn=session['logged_in'])

# now you can edit your attributes of logged user
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    db = shelve.open('users.db')
    content = db.get(session['username'], None)
    db.close()
    return render_template('edit.html', loggedIn=session['logged_in'], value=content)

# just a walkthrough to ease the modification of my own data
@app.route('/editing', methods=['POST'])
def editing():
    db = shelve.open('users.db')
    del db[session['username']]
    tmp_username = request.form['username']
    tmp_password = request.form['password']
    db[tmp_username] = { 'username' : tmp_username, 'password' : tmp_password }
    session['username'] = tmp_username
    content = db[tmp_username]
    db.close()

    return render_template('edit.html', loggedIn=session['logged_in'], value=content)

# just when you forget the URL...
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# enabled debug mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
