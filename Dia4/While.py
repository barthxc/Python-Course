#while puede tambien encadenarse con un else:
monedas = 5
while monedas > 0: #Esta condicion se cumple, entrará al while
    print(f"Tengo {monedas} monedas")
    monedas-=1       #monedas -1
else:
    print("No tengo mas dinero")


respuesta = 's'
while respuesta == 's':
    respuesta=input("¿Quieres seguir? (s/n)")
else:
    print("Gracias")

while respuesta =='s':
    pass  #hace que pase el código para usarlo mas tarde. como no hay nada que ejecutarse. PASA del bucle

numero = 10
while numero > 0:
    print(numero)
    numero -=1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

while lista_numeros > 0:
    print(lista_numeros)