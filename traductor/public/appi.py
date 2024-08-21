from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
TRANSLATE_API_URL = "https://api.cualquiera.com/translate"
API_KEY = "YOUR_API_KEY"
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language')
    source_language = data.get('source_language', 'es')  # Default source language is Spanish

    if not text or not target_language:
        return jsonify({"error": "Missing 'text' or 'target_language' in request"}), 400

    # Translate text to the target language
    translated_text = translate_text(text, source_language, target_language)

    if translated_text is None:
        return jsonify({"error": "Translation failed"}), 500
    return jsonify({"translated_text": translated_text})
@app.route('/reverse_translate', methods=['POST'])
def reverse_translate():
    data = request.json
    text = data.get('text')
    original_language = data.get('original_language', 'es')  # Default original language is Spanish
    current_language = data.get('current_language')

    if not text or not current_language:
        return jsonify({"error": "Missing 'text' or 'current_language' in request"}), 400

    # Translate text back to the original language
    translated_text = translate_text(text, current_language, original_language)

    if translated_text is None:
        return jsonify({"error": "Translation failed"}), 500

    return jsonify({"translated_text": translated_text})
def translate_text(text, source_language, target_language):
    payload = {
        'q': text,
        'source': source_language,
        'target': target_language,
        'format': 'text'
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(TRANSLATE_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get('translatedText')
    else:
        return None

