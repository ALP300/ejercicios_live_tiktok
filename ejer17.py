




'''


 Juego de Piedra, Papel o Tijera
Descripción: Crea un juego simple de piedra,
papel o tijera donde el usuario juega 
contra la computadora.


'''
import random

def piedra_papel_tijera():
    opciones=["piedra", "papel", "tijera"]
    computadora= random.choice(opciones)
    
    print("¡Bienvido al juego de Piedra, Papel o Tijera")
    jugador= input("Elige piedra / papel / tijera: ").lower()
    
    if jugador not in opciones:
        print("OPCIÓN INVÁLIDA")
        return 

    print(f"La computadora ha elegido: {computadora}")
    
    if jugador == computadora:
        print("Es un empate")
    
    elif(jugador== "piedra" and computadora=="tijera") or \
        (jugador== "papel" and computadora=="piedra") or \
        (jugador== "tijera" and computadora=="papel"):
        
        print("Ganaste")
    
    
    else:
        print("Perdiste! ")
    
   
piedra_papel_tijera()