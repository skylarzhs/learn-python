#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_from():
    return render_template(r'form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    if username == 'admin' and request.form['password'] == 'password':
        return render_template(r'sign-ok.html', username=username)
    return render_template(r'form.html', message="Bad username or password", username=username)


if __name__ == '__main__':
    app.run()
