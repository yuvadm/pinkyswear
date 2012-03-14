import random
import string

from bottle import route, run

@route('/')
def index(name='home'):
    return '<p><b>Homepage</b></p><p>Insert widget here</p>'

@route('/s/:id')
def sig(id='home'):
    return '<p><b>Signature</b></p><p>%s</p>' % id

@post('/s')
def sig(id='home'):
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
    return id

run(host='localhost', port=8000)
