'''
Escribir un programa que pida al 
usuario una palabra y 
muestre por pantalla el número de 
'''
palabra= input("Introduce una palabra: ")
vocales=['a','e','i','o','u']
for vocal in vocales:
    contador=0
    for letra in palabra:
        if letra==vocal:
            contador+=1
    print("La vocal "+vocal)