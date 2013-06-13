from provinciasapp import app as application
from provinciasapp import get_provincias

from webtest import TestApp
app = TestApp(application)

import json

def validate_package(url):
  resp = app.get(url)
  assert resp.status == '200 OK', resp.status
  assert resp.status_int == 200, resp.status_int
  assert resp.content_type == 'application/json'
  return json.loads(resp.body)


def test_json():
  payload = validate_package('/provincias')
  assert len(payload)==32,len(payload)
  assert "Distrito Nacional" in str(payload)

