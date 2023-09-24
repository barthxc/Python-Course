#Vamos a acceder a archivos
mi_archivo = open('Prueba.txt')
print(mi_archivo) #Accedemos a la información del archivo NO al contenido
#print(mi_archivo.read()) #Leer y abrir. Mostrar todas las lineas
print('****************************')
#print(mi_archivo.readline()) #Mostrar la primera linea
#print(mi_archivo.readline()) #Muestra la segunda linea usando readLine
#print(mi_archivo.readline().rstrip()) #Muestra la segunda linea usando readLine RSTRIP() elimina el salto de linea
#print(mi_archivo.readline().upper()) #Puedes usar métodos Strigns

'''for l in mi_archivo:
    print('Aquí dice: ' +l)
'''
print(mi_archivo.readlines()) #Muestra todas las lineas en una lista

mi_archivo.close() #Debemos cerrar el archivo por el espacio de memoria
