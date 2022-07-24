import pprint
import json
from urllib import response
import requests
import csv
import os
from pprint import pp

## Definimos la cabecera para la API de Meraki##

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

#####Funcion para listar todas las organizaciones a la cuales tenemos acceso#####
url='https://api.meraki.com/api/v1/organizations'
def get_Organizations():
    response = requests.request('GET', url, headers=headers, data = None)
    ##r = requests.get(url, headers=headers, data = None) #Solicitud a traves de Header
    response_json = json.loads(response.text)
    return response_json
response_json=get_Organizations()

