'''










Juego de Adivinanzas
Crea un juego en el que el programa elija
un número aleatorio 
y el usuario tenga que adivinarlo. El programa
debe dar pistas
como "más alto" o "más bajo" hasta que 
el usuario 
adivine el número correcto.
'''
import random

def adivina_el_numero():
    numero_secreto= random.randint(1,100)
    intentos=0
    max_intentos= 3
    print("¡Bienvenido al juego!")
    print("He elegido un número del 1 al 100 , ¡ADIVÍNALO!")
    
    while intentos<max_intentos:
        intento= int(input("Por favor introduce un número: "))
        intentos+=1
        
        if intento<numero_secreto:
            print("Más alto")
        elif intento>numero_secreto:
            print("Más bajo")
        else:
            print(f"¡FELICIDADES!, Advinaste el número en {intentos} intentos")
            break
    
    if intentos== max_intentos:
        print(f"Agotaste tus intentos, el número era: {numero_secreto}")
        
adivina_el_numero()