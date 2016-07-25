#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'
@app.route('/rtxim', methods=['GET'])
def rtxim():
    print request.values.get('ss')
    return '<h1>rtxim</h1>'
@app.route('/rtxim', methods=['POST'])
def rtxim_post(charset='utf-8'):

    data = request.get_data()
    print request.data
    print data.decode(charset)
    print '你好'.decode(charset)
    return data.decode(charset)
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run('0.0.0.0',port=4492)