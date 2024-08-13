from googletrans import Translator

def traducir_espanol_ingles(mensaje):
    
    traductor = Translator()
    
    traduccion = traductor.translate(mensaje, src='es', dest='en')
    
    return print(traduccion.text)


print("Mensaje: \n")
mensaje = input()
traducir_espanol_ingles(mensaje)
