nombre=input("Dime tu nombre: ")
ventas=input("¿Cuánto has vendido este mes? ")

#13% de las ventas es el resultado de las ventas

print(f"Hola {nombre} tus ventas han sido {ventas} y la comisión por ellas \n es un total de {round(float(ventas)*0.13,2)} $")