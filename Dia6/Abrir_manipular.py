#Para manipular proyectos debemos abrir el archivo con un modo NO por defecto en el método OPEN
#mi_archivo=open('archivo.txt','r') SOLO LECTURA por defecto
#mi_archivo=open('archivo.txt','w') SOLO ESCRITURA (si existe el archivo lo resetea y escribe, sino. Lo crea)
#mi_archivo=open('archivo.txt','a') SOLO ESCRITURA AL FINAL DEL ARCHIVO (escribirá sin resetear el archivo)

archivo = open('Prueba.txt', 'w')
archivo.write('''Soy el nuevo texto
os mataré a todos''')# Las ''' son para los saltos de lineas
#archivo.write() puedes introductir listas
archivo.close()