import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences  

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Cargar y preprocesar los datos (suponiendo que tienes un archivo con pares de oraciones)
datos_esp = []
datos_ing = []
longitud_maxima_esp = []
longitud_maxima_ing = []
vocab_size_esp = []
vocab_size_ing = []
embedding_dim  = []

# Crear los tokenizadores
tokenizer_esp = Tokenizer()
tokenizer_ing = Tokenizer()

# Ajustar los tokenizadores a los datos
tokenizer_esp.fit_on_texts(datos_esp)
tokenizer_ing.fit_on_texts(datos_ing)

# Codificar las secuencias
secuencias_esp = tokenizer_esp.texts_to_sequences(datos_esp)
secuencias_ing = tokenizer_ing.texts_to_sequences(datos_ing)

# Pad las secuencias
secuencias_esp = pad_sequences(secuencias_esp, maxlen=longitud_maxima_esp)
secuencias_ing = pad_sequences(secuencias_ing, maxlen=longitud_maxima_ing, padding='post')

# Crear el modelo (ejemplo con LSTM)
model = Sequential()
model.add(Embedding(vocab_size_esp, embedding_dim, input_length=longitud_maxima_esp))
model.add(LSTM(units=128))
model.add(Dense(vocab_size_ing, activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(secuencias_esp,  
 secuencias_ing, epochs=10, batch_size=64)

#Opcion 2

import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Transformer
from tensorflow.keras.models import Model


maxlen_esp = 2

inputs = Input(shape=(maxlen_esp,))
x = Embedding(vocab_size_esp, embedding_dim)(inputs)


# Encoder
#encoder = TransformerEncoder(num_layers=2, num_heads=4, ff_dim=32)
encoder_output = encoder(x) # type: ignore

# Decoder
maxlen_ing = 5
decoder_inputs = Input(shape=(maxlen_ing,))
decoder_embeddings = Embedding(vocab_size_ing, embedding_dim)(decoder_inputs)
#decoder = TransformerDecoder(num_layers=2, num_heads=4, ff_dim=32)
decoder_outputs = decoder(decoder_embeddings, encoder_output) # type: ignore


outputs = Dense(vocab_size_ing, activation='softmax')(decoder_outputs)

model = Model(inputs=[inputs, decoder_inputs], outputs=outputs)


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit([secuencias_esp, secuencias_ing[:, :-1]], secuencias_ing[:, 1:], epochs=10, batch_size=64)