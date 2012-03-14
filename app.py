import json
import os
import random
import requests
import string

from bottle import post, route, redirect, request, run, static_file, template

CLOUDANT_BASE = 'https://pinkyswear.cloudant.com/pinkyswear/'
CLOUDANT_AUTH = ('pinkyswear', 'abc123')

@route('/')
def index():
    return template('index.html', sig=None)

@route('/js/:filename')
def index(filename=None):
    root = os.path.join(os.path.dirname(__file__), 'js')
    return static_file(filename, root=root, mimetype='text/javascript')

@route('/s/:id')
def sig(id='home'):
    url = CLOUDANT_BASE + id
    r = requests.get(url, auth=CLOUDANT_AUTH)
    sig = json.loads(r.content)['s']
    return template('index.html', sig=sig)

@post('/s')
def sig():
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
    data = json.dumps({ 's' : request.POST['output'] })
    url = CLOUDANT_BASE + id
    headers = { 'content-type' : 'application/json' }
    r = requests.put(url, auth=CLOUDANT_AUTH, data=data, headers=headers)
    redirect('/s/%s' % json.loads(r.content)['id'])

run(host='localhost', port=8000)
