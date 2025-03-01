'''







Contador de Palabras en una Frase
Descripción: Crea un programa que cuente
cuántas veces aparece cada
palabra en una frase dada.
'''

def contador_de_palabras():
    frase= input("Por favor ingresa la frase: ")
    palabras= frase.split()
    conteo={}
    
    for palabra in palabras:
        palabra= palabra.lower().strip(".,!?")
        
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra]=1
    
    print("Conteo de palabras: ")
    for palabra,cantidad in conteo.items():
        print(f"{palabra}:{cantidad}")
    
contador_de_palabras()
    