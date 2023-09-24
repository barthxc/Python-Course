import os
import shutil #para mover archivo usando move
#import send2trash
print(os.getcwd())
#archivo = open('curso.txt', 'w')
#archivo.write('texto de prueba')
#archivo.close()

#print(os.listdir()) #Mover el archivo

#elimina una carpeta vacia os.rmdir()
#shutil.move('curso.txt','C:\\Users\\Bart\\Desktop')
#MEJOR NO UTILIZAR
#shutil.rmtree() elimina la carpeta completa, no van a la papelera y no pregunta

#elimina y lo mueve en la papelera
#send2trash.send2trash('curso.txt')

#da el resltado de espacio de memoria
print(os.walk('C:\\Users\\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy'))

ruta = 'C:\\Users\\Bart\\Desktop\\Python TOTAL\\PytholTotalUdemy'
#para poder usar walk iteramos

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta {carpeta} :")
    print("Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t {sub}")
    print('Los archivos son: ')
    for arch in archivo:
        if arch.endswith('.py'):
            print(f"\t {arch}")
    print('\n')

