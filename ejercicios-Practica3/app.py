#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request, render_template, session
import jinja2
import shelve
from mandelbrot import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'

# showing the whole website (plus login form)
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    content = {
        'title' : 'Adrián Morente',
        'subtitle': 'My personal webpage',
        'logo': 'user-icon.png',
        'nav_links' : [
            ("home", "--> Home"),
            ("github", "Github Account"),
            ("contact", "Contact")
        ],
        'body_section' : 'Homepage',
        'body_image' : 'home.png',
        'body_image_link' : 'home',
        'body_text' : 'This is my personal webpage. You might find it a little boring but who cares to be honest.'
    }

    if request.method == 'POST':
        s = shelve.open('users.db')
        user = s.get(request.form['username'], None)
        if user is not None and request.form['password']==user['password']:
            session['username'] = user['username']

    if 'username' in session:
        return render_template('index.html', content=content, loggedIn=True)
    else:
        return render_template('index.html', content=content, loggedIn=False)

    return render_template('index.html', content=content)

# showing a link to my personal github page
@app.route('/github', methods=['GET', 'POST'])
def github():
    content = {
        'title' : 'Adrián Morente',
        'subtitle': 'My personal webpage',
        'logo': 'user-icon.png',
        'nav_links' : [
            ("home", "Home"),
            ("github", "--> Github Account"),
            ("contact", "Contact")
        ],
        'body_section' : 'Github page',
        'body_image' : 'github.png',
        'body_image_link' : 'https://github.com/adrianmorente',
        'body_text' : 'This is my Github site. There you\'ll find a bunch of repos with open source code from me and my mates.'
    }
    return render_template('index.html', content=content)

# showing a link to my personal twitter page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    content = {
        'title' : 'Adrián Morente',
        'subtitle': 'My personal webpage',
        'logo': 'user-icon.png',
        'nav_links' : [
            ("home", "Home"),
            ("github", "Github Account"),
            ("contact", "--> Contact")
        ],
        'body_section' : 'Twitter account',
        'body_image' : 'contact.png',
        'body_image_link' : 'https://twitter.com/81adrianmorente',
        'body_text' : 'That\'s my Twitter account. I swear that you don\'t wanna follow me if you don\'t like basketball.'
    }
    return render_template('index.html', content=content)

# register form
@app.route('/register', methods=['GET', 'POST'])
def signup():
    registered = False
    if request.method == 'POST':
        s = shelve.open('users.db')
        try:
            username = request.form['username']
            password = request.form['password']
            user = { 'username' : username, 'password' : password }
            s[username] = user
            s.close()
            registered = True
        finally:
            s.close()
    return render_template('register.html', value=registered)

# popping the username out of the session
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

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

@app.route('/data')
def data():
    content = {
        'title' : 'Adrián Morente',
        'subtitle': 'My personal webpage',
        'logo': 'user-icon.png',
        'nav_links' : [
            ("home", "Home"),
            ("github", "Github Account"),
            ("contact", "--> Contact")
        ],
        'body_logged' : ''
    }
    return render_template('index.html', content=content)

# just when you forget the URL...
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# enabled debug mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
