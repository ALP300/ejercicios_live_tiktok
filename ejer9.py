



'''
Escribir un programa que pida 
al usuario un número entero 
y muestre por pantalla un triángulo
rectángulo como el de más abajo,
de altura el número introducido.

*
**
***
****
*****

'''
n= int(input("Por favor ingresa la altura: "))
for i in range(n):
    for j in range(i+1):
        print ("*", end= " ")
    print ("")