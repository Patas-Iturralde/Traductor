from googletrans import Translator
import requests
import json

#consumo API

url = "http://localhost:3000/mensaje_es"

response = requests.get(url)
data = response.json()

def traducir_espanol_frances(mensaje):
    
    traductor = Translator()
    
    traduccion = traductor.translate(mensaje, src='es', dest='fr')

    print(traduccion.text)
    
    return traduccion



for mensaje in data:

    mensaje_traducido = traducir_espanol_frances(mensaje['mensaje'])
    
    url_post = "http://localhost:3000/mensaje_fr"  
 
    headers = {'Content-Type': 'application/json'}
 
    data_post = {'mensaje': mensaje_traducido.text}
 
    response_post = requests.post(url_post, headers=headers, json=data_post)
 
 
    if response_post.status_code == 200:
 
        print("Mensaje traducido y enviado correctamente")
 
    else:
 
        print("Error al enviar el mensaje traducido")
        print(response_post.status_code)