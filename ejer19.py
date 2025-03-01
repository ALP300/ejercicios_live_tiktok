'''





Simulador de Dados
Descripción: Crea un programa que simule el
lanzamiento de uno o más dados. El usuario
puede elegir cuántos dados lanzar.
'''

import random

def lanzar_dados():
    print("¡Bienvenido al simulador de dados! :D")
    cantidad= int(input("¿Cuántos dados quieres lanzar? ")) 
    resultados= [random.randint(1,6) for _ in range(cantidad)]
    print(f"Suma total: {sum(resultados)}")
    
lanzar_dados()
       