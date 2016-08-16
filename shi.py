#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, httplib
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



if __name__ == '__main__':
    app.run('0.0.0.0',port=4492)