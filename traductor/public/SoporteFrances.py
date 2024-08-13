from googletrans import Translator

def traducir_espanol_a_frances(mensaje):
    # Crear una instancia del traductor
    traductor = Translator()
    
    # Traducir el mensaje de español a francés
    traduccion = traductor.translate(mensaje, src='es', dest='fr')
    
    # Devolver el texto traducido
    return traduccion.text

# Mensaje en español
mensaje_espanol = "Hola, ¿cómo estás?"

# Traducir el mensaje
mensaje_frances = traducir_espanol_a_frances(mensaje_espanol)

# Imprimir el mensaje traducido
print(f"Mensaje en francés: {mensaje_frances}")
