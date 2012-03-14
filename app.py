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
    data = request.POST.output
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
    url = 'https://pinkyswear.cloudant.com/pinkyswear/%s' % id
    requests.post(url, auth=('pinkyswear', 'abc123'), data=data)
    return id

run(host='localhost', port=8000)
