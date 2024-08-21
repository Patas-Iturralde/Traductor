import requests
from googletrans import Translator

# URLs de la API para obtener y enviar mensajes
url_get_message = "Api"
url_send_message = "Api"

def obtener_mensaje(url):
    """Obtiene un mensaje en español desde la API especificada."""
    try:
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()
        mensaje = respuesta.json().get('mensaje')
        
        if mensaje:
            return mensaje
        else:
            print("El mensaje no se encontró en la respuesta.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el mensaje: {e}")
        return None

def enviar_mensaje_traducido(url, mensaje_traducido):
    """Envía el mensaje traducido a la API especificada."""
    try:
        data = {'mensaje': mensaje_traducido}
        respuesta = requests.post(url, json=data, timeout=5)
        respuesta.raise_for_status()
        print("Mensaje traducido enviado correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar el mensaje: {e}")

def traducir_espanol_a_frances(mensaje):
    """Traduce un mensaje de español a francés utilizando Google Translate."""
    traductor = Translator()
    try:
        traduccion = traductor.translate(mensaje, src='es', dest='fr')
        return traduccion.text
    except Exception as e:
        print(f"Error al traducir el mensaje: {e}")
        return None

def main():
    """Función principal para coordinar la obtención, traducción y envío de mensajes."""
    mensaje_espanol = obtener_mensaje(url_get_message)

    if mensaje_espanol:
        mensaje_frances = traducir_espanol_a_frances(mensaje_espanol)
        
        if mensaje_frances:
            enviar_mensaje_traducido(url_send_message, mensaje_frances)

if __name__ == "__main__":
    main()
