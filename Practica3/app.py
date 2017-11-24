#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request, render_template, session
import shelve
from mandelbrot import *

app = Flask(__name__)
app.secret_key = 'random key for me by myself'

# counting the last visited pages
@app.before_request
def store_visted_urls():
    session['logged_in'] = 'username' in session
    last_one = request.url
    if request.url is not "http://127.0.0.1:5000/favicon.ico":
        if 'last_visited_1' in session:
            session['last_visited_2'] = session['last_visited_1']
        if 'last_visited_3' in session:
            session['last_visited_1'] = session['last_visited_3']
        session['last_visited_3'] = last_one

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

# showing a link to my personal github page
@app.route('/github', methods=['GET', 'POST'])
def github():
    return render_template('github.html', loggedIn=session['logged_in'])

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

# simple page which shows you a new mandelbrot fractal. it takes the args by GET
#method on the url of the browser
@app.route('/mandelbrot')
def mandelbrot():
    x1 = int(request.args.get('x1'))
    y1 = int(request.args.get('y1'))
    x2 = int(request.args.get('x2'))
    y2 = int(request.args.get('y2'))
    width = int(request.args.get('width'))
    iters = int(request.args.get('iters'))
    filename = "static/mandelbrot.png"
    renderizaMandelbrot(x1, y1, x2, y2, width, iters, filename)
    return render_template('mandelbrot.html')

# just when you forget the URL...
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# enabled debug mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
