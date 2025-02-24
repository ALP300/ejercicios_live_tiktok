'''
Escribir un programa que permita 
gestionar la base de datos de 
clientes de una empresa.
Los clientes se guardarán en un 
diccionario en el que la clave
de cada cliente será su NIF,
y el valor será otro diccionario con 
los datos del cliente (nombre, 
dirección, teléfono, 
correo, preferente), donde preferente
tendrá el valor True si se trata de un
cliente preferente.
El programa debe preguntar al usuario 
por una opción del siguiente menú: 
(1) Añadir cliente, 
(2) Eliminar cliente, (3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes 
preferentes, (6) Terminar. En función
de la opción elegida el programa 
tendrá que hacer lo siguiente:

2 Preguntar por el NIF del cliente y 
eliminar sus datos de la base de datos.
3 Preguntar por el NIF del cliente y mostrar sus datos.
5 Mostrar la lista de clientes preferentes
de la base de datos con su NIF y nombre.
6 Terminar el programa.

'''
clientes={}
opcion=''
while opcion!='6':
    if opcion=='1':
        nif=input("Introduce el NIF del cliente: ")
        nombre=input("Introduce el nombre del cliente: ")
        direccion=input("Introduce la dirección del cliente: ")
        telefono=input("Introduce el teléfono del cliente: ")
        correo=input("Introduce el correo del cliente: ")
        preferente=input("Introduce el cliente preferente (S/N): ")
        cliente={'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'correo':correo, 'preferente':preferente=='S'}
        clientes[nif]=cliente
    
    if opcion=='2':
        nif=input("Introduce el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("No existe el cliente con el NIF", nif)
            
    if opcion=='3':
        nif=input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print("NIF:", nif)
            for clave, valor in clientes[nif].items():
                print(clave.title()+":", valor)
        else:
            print("No existe el cliente con el NIF", nif)
            
    if opcion=='4':
        for nif, cliente in clientes.items():
            print(nif, cliente['nombre'])
        
    if opcion=='5':
        for nif, cliente in clientes.items():
            if cliente['preferente']:
                print(nif, cliente['nombre'])
    
    
        
    opcion= input("Por favor elige una opción del siguiente menú: \n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\n")
