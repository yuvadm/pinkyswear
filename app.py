import json
import os
import random
import requests
import string

from bottle import post, route, request, run, static_file, template

CLOUDANT_BASE = 'https://pinkyswear.cloudant.com/pinkyswear/'
CLOUDANT_AUTH = ('pinkyswear', 'abc123')

@route('/')
def index(name='home'):
    return template('index.html', sig=None)

@route('/s/:id')
def sig(id='home'):
    url = CLOUDANT_BASE + id
    r = requests.get(url, auth=CLOUDANT_AUTH)
    sig = json.loads(r.content)['s']
    return template('index.html', sig=sig)

@post('/s')
def sig(id='home'):
    data = json.dumps({ 's' : request.POST['output'] })
    url = CLOUDANT_BASE
    headers = { 'content-type' : 'application/json' }
    r = requests.post(url, auth=CLOUDANT_AUTH, data=data, headers=headers)
    return r.content

run(host='localhost', port=8000)
