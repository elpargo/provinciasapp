import falcon #webframework
import json #json duh!
import requests #sane http get/post/etc.
from bs4 import BeautifulSoup #sane htmlparser

def get_soup():
    #Link u guys provided.... get me the .json !!!!
    html_doc = requests.get("http://www.jmarcano.com/mipais/geografia/province/municipios/").text
    if not html_doc:
         #lame sanity check. TODO: make proper
         raise ValueError
    soup = BeautifulSoup(html_doc)
    return soup

def get_json():
    with open("provincias.json") as f:
        data = json.loads(f.read())
    return data

def get_provincias():
        data = get_json()
        res = []
        return json.dumps(res)#json go!

def get_anything(params):
    #TODO: add error handling
    data = get_json()
    for level in params:
        data = data[level]
    return data

class ProvinciasResource:
    def on_get(self, req, resp, query=None):
        base_query = ['1','Provincia']
        if query:
            base_query.append(query)
        data = get_anything(base_query)
        resp.body = json.dumps(data)

app = api = falcon.API()
provs = ProvinciasResource()
api.add_route('/provincias/', provs)
api.add_route('/provincias/{query}', provs)
