from django.http import HttpResponse
from django.utils import simplejson as json
from django.views.generic.list import BaseListView

def json_render_to_response(context):
    "Returns a JSON response containing 'context' as payload"
    payload = json.dumps(context)
    json_response = HttpResponse(payload,content_type="application/json")
    return json_response

#TODO, turn this into util to be used by both implementations
def get_json():
    with open("provincias.json") as f:
        data = json.loads(f.read())
    return data

def get_anything(params):
    #TODO: add error handling
    data = get_json()
    for level in params:
        data = data[level]
    return data

def provincias(request):
    c = request.path.split('/')
    c = filter(None,c) #eliminate the first and last empty path items
    c = get_anything(c)
    return json_render_to_response(c)

import pprint
def doc(request):
    header = request.path.split('/')
    header = filter(None,header) #eliminate the first and last empty path items
    header.remove('doc')
    body = get_anything(header)
    body =pprint.pformat(body)
    out = "{}{}<hr><hr>{}{}".format("<pre>",header,body,"</pre>")
    return HttpResponse(out)


