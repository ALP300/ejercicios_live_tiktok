





'''
Generador de Excusas Aleatorias
Escribe un programa que genere excusas
aleatorias para justificar por qué no
hiciste la tarea o por qué llegaste tarde.
'''
import random 

sujetos= ["Mi perro","Un hermano", " Mi mamá", "Mi abuela", "Mi vecina"]
verbos=["se comió", "destruyó", "quemó","vendió", "botó"]
objetos=["la tarea", "mi computadora","mi mochila","mis apuntes"]
lugares=["en el parque","en la escuela","en la calle","en la universidad"]

excusa= f"{random.choice(sujetos)} {random.choice(verbos)} {random.choice(objetos)} {random.choice(lugares)}"
print("Lo siento profe, pero ....",excusa)