





'''
¿Cuál es el Número Correcto? 🔢
Damos una pista matemática y 
los espectadores deben adivinar el número.
'''

numeros= [
    ("El dorsal que utiliza Messi", "10"),
    ("El dorsal que utiliza Cristiano", "7"),
    ("¿Cuál es la mitad de 100: ", "50"),
    ("El resultado de sumar 9+6: ", "15"),
]

for pista, respuesta in numeros:
    print(f"Pregunta: {pista}")
    intento= input("Tu respuesta: ")

    if intento == respuesta:
        print("CORRECTO")
    else:
        print("INCORRECTO")
