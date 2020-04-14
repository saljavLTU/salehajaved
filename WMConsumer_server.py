from flask import Flask, jsonify
from http.server import CGIHTTPRequestHandler, HTTPServer
#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import ssl
import socket
import os
#from flask_restful import Api, Resource, reqparse
import random
import csv
import xlrd
import xlsxwriter
import http.client
import sys
import requests

app = Flask(__name__)

serviceRegisteryURL = "http://localhost:8443/"
authorizationURL = "http://localhost:8445/"
orchestratorURL = "http://localhost:8441/"


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Consumer</h1>'''

@app.route('/register', methods=['GET'])
def api_sr(): 
   data = {
   "serviceDefinition": "MLConsumer8", 
   "providerSystem": 
   {
      "systemName": "MLConsumer", 
      "address": "localhost", 
      "port": 5001
   },
   "serviceUri": "mlconsumerservice",
   "secure":"NOT_SECURE",
   "interfaces": [
      "HTTPS-INSECURE-JSON" 
      ]
   }
   print(data) 
   # sending post request and saving response as response object 
   print(serviceRegisteryURL+'serviceregistry/register')
   r = requests.post(url = serviceRegisteryURL+'serviceregistry/register', json= data) 
   print(r.status_code)
   print(r.json)
   status=""
   if r.status_code != 201:
      print('Service Registration Failed')
      status="failed"
   else:
      print('Service Got Registered Successful')
      status="success"
   return (r.content)

@app.route('/authenticate', methods=['GET'])
def api_auth():
  body = {
            "consumerId": 16,
            "interfaceIds": [
                2
            ],
            "providerIds": [
                16
            ],
            "serviceDefinitionIds": [
                34
            ]
        }
  print(body) 
  print(authorizationURL+'authorization/mgmt/intracloud')
  r = requests.post(url = authorizationURL+'authorization/mgmt/intracloud', json= body) 
  print(r.status_code)
  print(r.json)
  status=""
  if r.status_code != 201:
    print('Service Authorization Failed')
    status="failed"
  else:
    print('Service Got Authorized Successfully')
    status="success"
  return (r.content)

@app.route('/orchestrate', methods=['GET'])
def api_orch():
   r = requests.get(url = orchestratorURL+'orchestrator/orchestration/16') 
   print(r.status_code)
   print(r.json)
   status=""
   if r.status_code != 200:
      print('Service orchestration Failed')
      status="failed"
   else:
      print('Service Got orchestration Started')
      status="Orchestration is started"
   return (status)

app.run(debug=True, port=5001)
