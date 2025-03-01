'''







Conversor de Monedas
Crea un programa que convierta una 
cantidad de dinero de una moneda a 
otra usando tasas de cambio
'''
def conversor_monedas():
    tasas={
        "USD": 1.0,
        "EUR": 0.85
    }
    moneda_origen= input("ELIGE LA MONEDA DE ORIGEN : (USD, EUR): ").upper() #USD
    moneda_destino= input("ELIGE LA MONEDA DE DESTINO: (USD, EUR): ").upper() #EUR
    cantidad= float(input("Por favor, introduce la cantidad: "))
    
    if moneda_destino in tasas and moneda_origen in tasas:
        cantidad_convertida=  cantidad*(tasas[moneda_destino]/tasas[moneda_origen])
        print(f"{cantidad}{moneda_origen} son {cantidad_convertida}{moneda_destino}")
    else:
        print("MONEDA NO VÁLIDA")
    
conversor_monedas()