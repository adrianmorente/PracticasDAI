#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request, render_template, session
import jinja2
import shelve, queue
from mandelbrot import *

app = Flask(__name__)
last_visited = queue.Queue(3)

# remembering the last visited pages
@app.after_request
def remember_three_pages(response):
    if last_visited.qsize() == 3:
        last_visited.get()
    last_visited.put(request.url)
    return response

# showing the whole website (plus login form)
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    # we'll authenticate the user and initialize the urls dictionary
    if request.method == 'POST':
        s = shelve.open('users.db')
        user = s.get(request.form['username'], None)
        if user is not None and request.form['password']==user['password']:
            session['username'] = user['username']
            s.close()

    if 'username' in session:
        return render_template('index.html', loggedIn=True)
    else:
        return render_template('index.html', loggedIn=False)

    return render_template('index.html')

# register form
@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        s = shelve.open('users.db')
        try:
            username = request.form['username']
            password = request.form['password']
            user = { 'username' : username, 'password' : password }
            s[username] = user
            s.close()
        finally:
            s.close()
    return render_template('register.html')

# popping the username out of the session
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# showing a link to my personal github page
@app.route('/github', methods=['GET', 'POST'])
def github():
    return render_template('github.html')

# showing a link to my personal twitter page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

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
