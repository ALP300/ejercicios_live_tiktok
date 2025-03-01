



'''

Adivina el Emoji 🎭
Los espectadores deben 
adivinar qué emoji 
representa una palabra o frase.

'''
emojis= [
    ("😈 modo diablo", "diablo"),
    ("🤡 el risas", "payaso"),
    ("😎 carita facherita: ", "chiconais"),
    ("🔥 algo muy caliente: ", "fuego"),
]
for pista, respuesta in emojis:
    print(f"Adivinanza: {pista}")
    intento= input("Escribe la respuesta: ")
    
    if intento.lower()==respuesta:
        print("CORRECTO")
    else:
        print("INCORRECTO")
