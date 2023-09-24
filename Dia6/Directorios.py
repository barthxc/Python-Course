import os #instalamos OS
from pathlib import Path
#importamos Path para no tenemos que poner los \\  Se pone con mayusculas porque es un objeto
ruta = os.getcwd() #getCurrentWorkingDirectory
#Las rutas por ahora en windows debe ser con coble barra \\
ruta = os.chdir('C:\\Users\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy\\Dia6\\EjemploDirectorio') #Cambiar directorio de trabajo
archivo = open('otro_archivo.txt')

#ruta = os.makedirs('C:\\Users\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy\\Dia6\\EjemploDirectorio\\EjemploEjemplo')#Crear una capeta nueva
print(archivo)

ruta = 'C:\\Users\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy\\Dia6\\EjemploDirectorio\\EjemploEjemplo\\archivo2.txt'
elemento = os.path.dirname(ruta) #Es la ruta aunque pongas un archivo . Te muestra la ruta
elemento = os.path.split(ruta) #Devuelve una tupla con el elemento de la ruta y el nombre del archivo

#Eliminar directorio, debe estar vacio
#os.rmdir('C:\\Users\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy\\Dia6\\EjemploDirectorio\\EjemploEjemplo')

print(elemento)

otro_archivo = 'prueba.txt'

carpeta = Path('C:/Users/Bart/Desktop/Python TOTAL/PythonTotalUdemy/Dia6/EjemploDirectorio')
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())