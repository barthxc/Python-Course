#min(cantidad de valores o iterable:lista, etc)
#max()
lista=[58,96,72,64,35]
menor=min(lista)
mayor=max(lista)
print(menor)
print(mayor)
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

#TAMBIEN PODEMOS TRABAJAR CON STRINGS DE FORMA ALFABÉTICA

nombres=['Juan','Pablo','Alicia','Carlos']
print(min(nombres))

nombre="Carlos"
print(min(nombre)) #EL RESULTADO ES C, PORQUE BUSCA PRIMERO EN LAS LETRAS MAYUSCULAS Y DESPUÉS EN MINUSCULAS

nombre="carlos"
print(min(nombre)) #El resultado es 'a' porque todo es minuscula
#podemos pasarlo todo a minuscula con lower

#podemos hacerlo también condiccionarios

dic={'C1':45,'C2':11}
print(min(dic)) #Se fija por DEFECTO en la clave mas bajo
print(min(dic.values())) #Aquí me da el valor mas bajo del diccionaro

