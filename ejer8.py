'''
Crea un chatbot que 
siempre responda cosas 
sin sentido o haga 
chistes malos.
'''
import random
respuesta=[
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Cómo se llama el primo vegano de Bruce Lee? Broco Lee.",
    "Si en krypton las piedras se llaman kryptionistas, ¿en la tierra se llaman tierritas?",
    "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
    "¿Cuál es la fruta que toma té? el TOMATE",
    "¿Cómo se llama hacer dieta en chino? Kita Kilito.",
    "Un pollito respiraba por la cola, se sentó y murió"
]
def chatbot():
    print("¡HOLA, BIENVENIDO A CHACALITOBOT, PIDE UN CHISTE!")
    while True:
        entrada= input("Por favor ingresa tu solicitud: ")
        if entrada.lower() in ["adiós","chau","chao","bay"]:
            print(" Hasta luego :,( ")
            break
        print(random.choice(respuesta))
        
chatbot()