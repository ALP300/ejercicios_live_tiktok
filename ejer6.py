'''



## Ejercicio

Escribir un programa que almacene en una
lista los siguientes precios, 
50, 75, 46, 22, 80, 65, 8, 
y muestre por pantalla el menor 
y el mayor de los precios.
'''
precios=[50, 75, 46, 22, 80, 65, 8]
max= min= precios[0] 
for precio in precios:
    if precio < min:
        min= precio
    elif precio > max:
        max= precio

print("El precio mínimo es: "+str(min))
print("El precio máximo es: "+str(max))
