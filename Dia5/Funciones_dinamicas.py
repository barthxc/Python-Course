def chequear_3_cifras(numero):
    return numero in range(100,1000) #retorna si el numero que ponga tiene 3 cifras
resultado=chequear_3_cifras(345)
print(resultado)


###con lista

def chequear_3_lista(lista):
    for n in lista:
        if n in range(100,1000):
            return True  #cuando da un valor True deja de iterar en el bucle. Es como un Pass
        else:
            pass
    return False #False funciona igual que True corta el bucle, por eso se pone FUERA del bucle


print(chequear_3_lista([33,99,500])) #devuelve un NONE porque no hay nada falso que retornar y además no hay un true dentro

print(chequear_3_lista([444,1,3]))

print("----------------------------------------------------------------------")
#DESEMPAQUETA TUPLAS

precios_cafe=[('capuchino',1.5),('Expresso',1.2),('Moka',1.9)]
for cafe,precio in precios_cafe:
    print(precio*0.45)

#precio mas caro en funcion

def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=''
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return(cafe_mas_caro,precio_mayor)

cafe,precio = cafe_mas_caro(precio,cafe)#saca las variables de retorno en 2 variables.
print(cafe_mas_caro(precios_cafe))