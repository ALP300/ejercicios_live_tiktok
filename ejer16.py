










'''
¿Cuánto es en Dólares? 💰
Los espectadores deben convertir 
una cantidad de soles (PEN) a dólares (USD).
'''
tasas_cambio={
    "pen": 3.80,
    "mxn": 20.00,
    "eur":0.92
}
moneda= input("Ingresa la moneda (pen,mxn,eur): ").lower()
cantidad= float(input("Por favor ingresa la cantidad: "))

if moneda in tasas_cambio:
    dolares= cantidad/ tasas_cambio[moneda]
    print(f"{cantidad} {moneda.upper()} equivale a {dolares}")
else:
    print(" X - No existe la moneda ")