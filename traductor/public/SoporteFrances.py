import requests
from googletrans import Translator

# URLs de la API para obtener y enviar mensajes
url_get_message = "API-RECIBIR MENSAJES"
url_send_message = "API-ENVIARM MENSAJES"

def obtener_mensaje():
    try:
        # Realizar la solicitud GET para obtener el mensaje
        respuesta = requests.get(url_get_message, timeout=5)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        
        # Extraer el mensaje del JSON recibido
        mensaje = respuesta.json().get('mensaje')
        
        if mensaje:
            return mensaje
        else:
            print("El mensaje no se encontró en la respuesta.")
            return ''
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el mensaje: {e}")
        return ''

def enviar_mensaje_traducido(mensaje_traducido):
    try:
        # Realizar la solicitud POST para enviar el mensaje traducido
        data = {'mensaje': mensaje_traducido}
        respuesta = requests.post(url_send_message, json=data, timeout=5)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        
        print("Mensaje traducido enviado correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar el mensaje: {e}")

def traducir_espanol_a_frances(mensaje):
    try:
        # Crear una instancia del traductor
        traductor = Translator()
        
        # Traducir el mensaje de español a francés
        traduccion = traductor.translate(mensaje, src='es', dest='fr')
        
        # Devolver el texto traducido
        return traduccion.text
    except Exception as e:
        print(f"Error al traducir el mensaje: {e}")
        return ''

def main():
    # Obtener el mensaje en español desde la API
    mensaje_espanol = obtener_mensaje()

    if mensaje_espanol:
        # Traducir el mensaje al francés
        mensaje_frances = traducir_espanol_a_frances(mensaje_espanol)
        
        if mensaje_frances:
            # Enviar el mensaje traducido a través de la API
            enviar_mensaje_traducido(mensaje_frances)

if __name__ == "__main__":
    main()
