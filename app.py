try:
    import json
except ImportError:
    import simplejson as json
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
def index_js(filename=None):
    root = os.path.join(os.path.dirname(__file__), 'js')
    return static_file(filename, root=root, mimetype='text/javascript')


@route('/css/:filename')
def index_css(filename=None):
    root = os.path.join(os.path.dirname(__file__), 'css')
    return static_file(filename, root=root, mimetype='text/css')


@route('/favicon.ico')
def index_favicon(filename=None):
    root = os.path.join(os.path.dirname(__file__))
    return static_file('favicon.ico', root=root, mimetype='text/javascript')


@route('/s/:id')
def sig(id='home'):
    url = CLOUDANT_BASE + id
    r = requests.get(url, auth=CLOUDANT_AUTH)
    sig = json.loads(r.content)['s']
    name = json.loads(r.content)['name']
    swear = json.loads(r.content)['swear']

    return template('index.html', sig=sig, name=name, swear=swear)


@post('/s')
def sig_post():
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
    data = {}
    data["name"] = request.POST['name']
    data["swear"] = request.POST['swear']
    data["s"] = request.POST['output']

    url = CLOUDANT_BASE + id
    headers = {'content-type': 'application/json'}
    r = requests.put(url, auth=CLOUDANT_AUTH, data=json.dumps(data), headers=headers)
    redirect('/s/%s' % json.loads(r.content)['id'])

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
