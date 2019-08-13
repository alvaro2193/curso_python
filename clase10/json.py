import requests #importar libreria, protocolos de comunicacion http get,post,pull, delete
import json #importar libreria, excel, word, csv, para BD no relacional


token = "Bearer<TOKEN>" #token para autentificar 
headers= {"Authorization":token}
r=requests.get ('http://google.com', headers = headers) 

print (r.status_code)
#json_body = r.json

archivo = open ("hola.txt", "w")
archivo.write ("hola greencore")
archivo.close ()