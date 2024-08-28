from googletrans import Translator
import requests
import json

#consumo API

url = "http://localhost:3000/mensaje"

response = requests.get(url)
data = response.json()

def traducir_espanol_frances(mensaje):
    
    traductor = Translator()
    
    traduccion = traductor.translate(mensaje, src='es', dest='fr')

    print(traduccion.text)
    
    return traduccion



traducir_espanol_frances(data['mensaje'])

#envio de mensaje traducido a la api

# data = {
#    "mensaje":traduccion.text
# }

# data_json = json.dumps(data)

# headers = {
#     'Content-Type': 'application/json'
# }

# response = requests.post(url, data=data_json, headers=headers)

# if response.status_code == 200:

#     respuesta = response.json()

#     print(respuesta)

# else:

#     print("Error:", response.status_code)

# #opcion 2
# from azure.ai.textanalytics import TextAnalyticsClient
# from azure.core.credentials import AzureKeyCredential

# def traducir_azure(texto, destino='en', subscription_key="", endpoint=""):
#   """Traduce un texto utilizando Azure Text Translator.

#   Args:
#     texto: El texto a traducir.
#     destino: El código del idioma de destino (por defecto: 'fr' para francé).
#     subscription_key: Tu clave de suscripción de Azure.
#     endpoint: El punto de conexión de tu recurso de Azure Text Analytics.

#   Returns:
#     La traducción del texto.
#   """

#   client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(subscription_key))
#   documents = [{"id": "1", "language": "es", "text": texto}]
#   result = client.translate_document(documents, to="en")
#   return result[0].translations[0].text

# # Ejemplo de uso:
# texto_espanol = "Hola, ¿cómo estás?"
# traduccion_frances = traducir_azure(texto_espanol, subscription_key="tu_clave", endpoint="tu_endpoint")
# print(traduccion_frances)

# # opcion 3

# from deepl import Translator

# def traducir_deepl(texto, destino='EN-US'):
#   """Traduce un texto utilizando DeepL Translator.

#   Args:
#     texto: El texto a traducir.
#     destino: El código del idioma de destino (por defecto: 'EN-US' para inglés estadounidense).

#   Returns:
#     La traducción del texto.
#   """

#   translator = Translator(auth_key="tu_clave_api")
#   result = translator.translate_text(text=texto, target_lang=destino)
#   return result.text

# # Ejemplo de uso:
# texto_espanol = "Hola, ¿cómo estás?"
# traduccion_frances = traducir_deepl(texto_espanol)
# print(traduccion_frances)