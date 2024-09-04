
import requests
import json
import asyncio
import aiohttp

from translate import Translator
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "*"}})


@app.route('/translate', methods=['POST'])

def translate_message():

    url = "http://localhost:3001/mensaje_es"

    response = requests.get(url)
    data = response.json()

    try:

        translator = Translator(to_lang="en", from_lang="es", azure_region="eastus", azure_text_translation_key="0058597293a34918921bc409de57d2b8")

        asyncio.run(translate_messages_async(data, translator))


        return jsonify({'translated_message': 'Traducción realizada correctamente'})
    
    except Exception as e:

        print(f"Error al traducir el mensaje: {e}")

        return jsonify({'error': 'Error al traducir el mensaje'}), 500
    
async def translate_messages_async(data, translator):

    translations = []

    for mensaje in data:

        translation = translator.translate(mensaje['mensaje'])

        translations.append({'mensaje': translation})


    await asyncio.gather(*[translate_message_post(translation) for translation in translations])

async def translate_message_post(translation):

    url_post = "http://localhost:3001/mensaje_en"

    headers = {'Content-Type': 'application/json'}

    data_post = {'mensaje': translation['mensaje']}

    print("ASD: ",translation['mensaje'])

    async with aiohttp.ClientSession() as session:

        async with session.post(url_post, headers=headers, json=data_post) as response:

            if response.status == 200:

                print("Mensaje traducido y enviado correctamente")

            else:

                print("Error al enviar el mensaje traducido")

                print(response.status)
    
    

@app.route('/translate_fr', methods=['POST'])

def translate_messagefr():

    url = "http://localhost:3001/mensaje_es"

    response = requests.get(url)
    data = response.json()

    try:

        translator = Translator(to_lang="fr", from_lang="es", azure_region="eastus", azure_text_translation_key="0058597293a34918921bc409de57d2b8")

        asyncio.run(translate_messagesfr_async(data, translator))


        return jsonify({'translated_message': 'Traducción realizada correctamente'})
    
    except Exception as e:

        print(f"Error al traducir el mensaje: {e}")

        return jsonify({'error': 'Error al traducir el mensaje'}), 500
    
async def translate_messagesfr_async(data, translator):

    translations = []

    for mensaje in data:

        translation = translator.translate(mensaje['mensaje'])

        translations.append({'mensaje': translation})


    await asyncio.gather(*[translate_messagefr_post(translation) for translation in translations])

async def translate_messagefr_post(translation):

    url_post = "http://localhost:3001/mensaje_fr"

    headers = {'Content-Type': 'application/json'}

    data_post = {'mensaje': translation['mensaje']}

    print("ASD: ",translation['mensaje'])

    async with aiohttp.ClientSession() as session:

        async with session.post(url_post, headers=headers, json=data_post) as response:

            if response.status == 200:

                print("Mensaje traducido y enviado correctamente")

            else:

                print("Error al enviar el mensaje traducido")

                print(response.status)
    

if __name__ == '__main__':

    app.run(debug=True, port=5000)