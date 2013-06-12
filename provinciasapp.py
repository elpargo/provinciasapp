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

def get_provincias():
    soup = get_soup()
    #this crap is in a table full of arrgssss luckily for us is the only strong in the whole page :D
    res = soup.find_all('strong')
    res = [item.text for item in res] #get the actual text not the tag
    return json.dumps(res)#json go!

class ProvinciasResource:
    def on_get(self, req, resp):
        resp.body = get_provincias()

app = api = falcon.API()
provs = ProvinciasResource()
api.add_route('/provincias', provs)
