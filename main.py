words_dict = {
            "APORRAR": "Quedarse sin poder responder ni hablar.",
            "CAMON": "Trono en el que asisten los reyes a misa.",
            "DISOSMIA": "Dificultad en la percepción de los olores.",
            "ESPLIN": "Humor sombrío, aburrimiento profundo."
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in words_dict.keys():
    print(words_dict[word])
else:
    print("La palabra no está en el diccionario")
