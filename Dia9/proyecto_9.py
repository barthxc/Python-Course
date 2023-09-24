import re
import os
import time
import datetime
from pathlib import Path
import math
ruta = 'C:\\Users\\Bart\\Desktop\\Python TOTAL\\PythonTotalUdemy\\Dia9\\Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados=[]
inicio = time.time()
def buscar_numero(archivo,patron):
    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-'*50)
    print(f"Fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print('\n')
    print('ARCHIVO\t\t\tNRO.SERIE')
    print('--------\t\t--------')
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice +=1
    print('\n')
    print(f'Números encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la busqueda: {math.ceil(duracion)} segundos")





crear_listas()
mostrar_todo()
