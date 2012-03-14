import json
import os
import random
import requests
import string

from bottle import post, route, request, run, static_file, template

@route('/')
def index(name='home'):
    return template('index.html', sig=None)

@route('/s/:id')
def sig(id='home'):
    url = 'https://pinkyswear.cloudant.com/pinkyswear/%s' % id
    r = requests.get(url, auth=('pinkyswear', 'abc123'))
    sig = json.loads(r.content)['s']
    return template('index.html', sig=sig)

@post('/s')
def sig(id='home'):
    data = json.dumps({ 's' : request.POST['output'] })
    url = 'https://pinkyswear.cloudant.com/pinkyswear/'
    headers = { 'content-type' : 'application/json' }
    r = requests.post(url, auth=('pinkyswear', 'abc123'), data=data, headers=headers)
    return r.content

run(host='localhost', port=8000)
