#Dividir el texto en oraciones

import nltk

# Cargar el texto
nombre_archivo = "nlp.txt"
archivo = open(nombre_archivo, "r", encoding="utf-8")
text = archivo.read()

print(text)

# Tokenizar el texto en oraciones

tokenizador = nltk.data.load('tokenizers/punkt/english.pickle')
oraciones = tokenizador.tokenize(text)

# Imprimir las oraciones

for oracion in oraciones:
    print(oracion)
    print("")

    #buenas