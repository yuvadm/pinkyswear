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
    return '<p><b>Signature</b></p><p>%s</p>' % id

@post('/s')
def sig(id='home'):
    data = json.dumps(request.POST['output'])
    url = 'https://pinkyswear.cloudant.com/pinkyswear/'
    headers = { 'content-type' : 'application/json' }
    r = requests.post(url, auth=('pinkyswear', 'abc123'), data=data, headers=headers)
    return r.content

run(host='localhost', port=8000)
