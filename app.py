#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-

import urllib, httplib,random,time
from flask import Flask
from flask import request
from flask import Response




app = Flask(__name__)

arraym = ['��������������˵�ǲ���',
'������ԣ���Ը��һ�Ŵ��������ǰ���ٳԺ��档',
'���ڽ��ܱ��˵����������ÿ��Ե����Լ���ȱ�㡣',
'���ϳ�������������С�¡�',
'Ŭ�����󣬲�֪��������飬��ּ�֣��͹����ˡ�',
'���������ú�����������£��úú�Ŭ���ˣ�',
'����ǰ��һ�䱣�أ�������û�ݣ�',
'��������������Ҳû�ù����ӡ�',
'������վ�ڱ��˵ĽǶ�Ϊ�������룬������Ǵȱ���']



@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'
@app.route('/rtxim', methods=['GET'])
def rtxim():
    print request.values.get('ss')
    return '<h1>rtxim</h1>'
@app.route('/rtxim', methods=['POST'])
def rtxim_post():
    if not request.json:
       return '404';
    data = request.json.get('commits', "")
    commit_url = data[0]["url"].encode("gbk")
    message    = data[0]["message"].encode("gbk")
    name    = data[0]["author"]["name"].encode("gbk")
    num = random.randrange(0,len(arraym))
    print type(data[0])
    print commit_url
    print message
    print name
    if name != 'abby':
       return '404';
    httpClient = None
    helloMsg = '''С�����!,������
    Abby �Ĳ�Ʒ���������
    ������������\n'''
    commit_info = '\n �������ϸ�� %s' % commit_url
    giturl_info = '\n �ֿ��ַ http://github.panli.com/abby/PanliByAbby'
    robotM = '''\n  ����������ά�Ŷӵ�R2�����˵���Ϣ֪ͨ
    ���ղ��������������ӣ�
    %s
    ''' % arraym[num]
    devs = 'julian,wilson,jason,jessica,yoko,lewis,manu,abby,yang,jean,aaron'
    sessionid = '{45E974F3-B242-486b-8487-56C23D37FF91}'
    try:
        params = urllib.urlencode({'sender': 'robot', 'pwd': 'robot', 'receivers': devs, 'msg': helloMsg+message+commit_info+giturl_info+robotM, 'sessionid': sessionid})
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
        httpClient = httplib.HTTPConnection('172.20.7.29', 8012, timeout=10)
        httpClient.request('POST', '/SendIM.cgi', params, headers)
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    return '200'
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