#Acepta 2 datos en el método que será el principio y el final de index para agarrar ese dato seleccionado
mi_variable="esta palabra será extraida"
#El primer número es donde empieza a coger el dato
#El segundo dato hasta donde EXCLUYENDO DEL DATO
#El tercer parámetro es el salto que da ignorando index

texto="ABCDEFGHIJKLM"
fragmento=texto[2:5] #No incluye el index 5
print(fragmento)
fragmento=texto[2:] #Desde el indice hasta el final
print(fragmento)
fragmento=texto[:5] #Desde el comienzo hasta el índice 5
print(fragmento)
fragmento=texto[2:10:2] #Desde el 2 hasta el 10, saltando el siguiente
print(fragmento)
fragmento=texto[::3] #todo el string pero saltando de 3 en 3
print(fragmento)
fragmento=texto[::-1] #Muestra la cadena alreves
print(fragmento)
fragmento=texto[::-2] #Orden inverso, pero saltando de 1 en 1





