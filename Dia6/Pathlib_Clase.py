from pathlib import Path, PureWindowsPath
#PureWindowsPath transforma cualquier ruta a una ruta de windows
#ruta_windows = PureWindowsPath(String o directorio mac) convierte el directorio a directorio Windows
#importamos Path para no tenemos que poner los \\  Se pone con mayusculas porque es un objeto
carpeta = Path('C:\\Users\\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy\\Dia6\\prueba.txt')
#Ahora carpeta es un objeto Path y tiene métodos nuevos
print(carpeta.read_text())#Mostrar el contenido del archivo
#Con pathlib no tenemos que abrir ni cerrar la ejecucion
print(carpeta.name)#El nombre del archivo
print(carpeta.suffix)#La terminación del archivo .txt
print(carpeta.stem)#El nombre de la terminación prueba

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print('Genial, existe mi archivo')
