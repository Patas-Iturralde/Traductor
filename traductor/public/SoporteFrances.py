import requests
from googletrans import Translator

# URL de la API para obtener el mensaje en español
url_get_message = "https://api.tu-dominio.com/obtener-mensaje"
# URL de la API para enviar el mensaje traducido
url_send_message = "https://api.tu-dominio.com/enviar-mensaje"

def obtener_mensaje():
    # Realizar la solicitud GET para obtener el mensaje
    respuesta = requests.get(url_get_message)
    
    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        return respuesta.json().get('mensaje', '')
    else:
        print(f"Error al obtener el mensaje: {respuesta.status_code}")
        return ''

def enviar_mensaje_traducido(mensaje_traducido):
    # Realizar la solicitud POST para enviar el mensaje traducido
    data = {'mensaje': mensaje_traducido}
    respuesta = requests.post(url_send_message, json=data)
    
    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        print("Mensaje traducido enviado correctamente.")
    else:
        print(f"Error al enviar el mensaje: {respuesta.status_code}")

def traducir_espanol_a_frances(mensaje):
    # Crear una instancia del traductor
    traductor = Translator()
    
    # Traducir el mensaje de español a francés
    traduccion = traductor.translate(mensaje, src='es', dest='fr')
    
    # Devolver el texto traducido
    return traduccion.text

# Obtener el mensaje en español desde la API
mensaje_espanol = obtener_mensaje()

if mensaje_espanol:
    # Traducir el mensaje al francés
    mensaje_frances = traducir_espanol_a_frances(mensaje_espanol)
    
    # Enviar el mensaje traducido a través de la API
    enviar_mensaje_traducido(mensaje_frances)
