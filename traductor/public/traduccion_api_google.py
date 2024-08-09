from google.cloud import translate_v2 as translate

def traducir(texto, idioma_origen, idioma_destino):
    #Traduce un texto utilizando la API de Google Cloud Translation.

    """Args:
        texto: "El texto a traducir".
        idioma_origen: español
        idioma_destino: ingles.

    Returns:
        El texto traducido."""


    # Crear un cliente de traducción
    translate_client = translate.Client()

    # Construir la solicitud de traducción
    result = translate_client.translate(
        texts=[texto],
        source_language=idioma_origen,
        target_language=idioma_destino
    )

    # Obtener el texto traducido
    return result['translations'][0]['translatedText']