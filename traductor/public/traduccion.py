import os
import tensorflow as tf
from google.cloud import translate_v2 as translate

# Configuración de la API de Google Cloud Translation
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ruta_a_tu_credencial_json.json'
translate_client = translate.Client()

# Función para traducir un mensaje
def traducir_mensaje(mensaje, idioma_destino):
    # Utilizamos la API de Google Cloud Translation para traducir el mensaje
    resultado = translate_client.translate(mensaje, target_language=idioma_destino)
    return resultado['translatedText']

# Creación de la aplicación Flask para el microservicio
from flask import Flask, request, jsonify
app = Flask(__name__)

# Ruta para recibir los mensajes a traducir
@app.route('/traducir', methods=['POST'])
def traducir():
    mensaje = request.json['mensaje']
    idioma_destino = request.json['idioma_destino']
    traduccion = traducir_mensaje(mensaje, idioma_destino)
    return jsonify({'traduccion': traduccion})

if __name__ == '__main__':
    app.run(debug=True)
