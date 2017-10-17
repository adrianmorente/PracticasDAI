#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the index!'

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/css')
def get_image():
    return ('static', filename='style.css')
