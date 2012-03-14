from bottle import route, run

@route('/')
def index(name='home'):
    return '<p><b>Homepage</b></p><p>Insert widget here</p>'

@route('/s/:id')
def sig(id='home'):
    return '<p><b>Signature</b></p><p>%s</p>' % id

run(host='localhost', port=8000)
