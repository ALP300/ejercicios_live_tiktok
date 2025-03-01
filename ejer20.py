'''








Contador de Palabras
Crea un programa que cuente la cantidad 
de palabras en un texto ingresado por el usuario.
'''

def contador_de_palabras():
    texto= input("Introduce un texto: ")
    palabras= texto.split()
    print(f"EL texto contiene {len(palabras)} palabras")
    
contador_de_palabras()