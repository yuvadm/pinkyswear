import os
import random
import string

from bottle import post, route, run, static_file

@route('/')
def index(name='home'):
    return static_file('index.html', root=os.path.dirname(__file__), mimetype='text/html')

@route('/s/:id')
def sig(id='home'):
    return '<p><b>Signature</b></p><p>%s</p>' % id

@post('/s')
def sig(id='home'):
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
    return id

run(host='localhost', port=8000)
