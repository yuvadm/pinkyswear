import json
import os
import random
import requests
import string

from bottle import post, route, request, run, static_file

@route('/')
def index(name='home'):
    return static_file('index.html', root=os.path.dirname(__file__), mimetype='text/html')

@route('/s/:id')
def sig(id='home'):
    url = 'https://pinkyswear.cloudant.com/pinkyswear/%s' % id
    r = requests.get(url, auth=('pinkyswear', 'abc123'))
    return r.content

@post('/s')
def sig(id='home'):
    data = json.dumps({ 's' : request.POST['output'] })
    url = 'https://pinkyswear.cloudant.com/pinkyswear/'
    headers = { 'content-type' : 'application/json' }
    r = requests.post(url, auth=('pinkyswear', 'abc123'), data=data, headers=headers)
    return r.content

run(host='localhost', port=8000)
