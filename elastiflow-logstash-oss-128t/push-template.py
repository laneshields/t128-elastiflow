#!/bin/python
import requests

with open('elastiflow.template.json') as fd:
  template = fd.read()

headers = {'Content-Type':'application/json'}
resp = requests.put('http://localhost:9200/_template/elastiflow', headers=headers, data=template)
