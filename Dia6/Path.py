from pathlib import Path
#contruccion de rutas

#Podemos obtener una ruta absoluta
base = Path.home()
#contruye acceso pero no son directorios reales.
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia")) #Ruta relativa, puede ser en varios lugares
print(base)#Instancia Path con una ruta absoluta principal al usuario actual
print(guia) #si le pasamos la base a nuestra GUIA se crea una ruta absoluta
#Linea 7 ruta absoluta + la ruta relativa que la convierte absoluta.
#Podemos pasarle mas objetos Path para crear las rutas como necesitamos
guia2=guia.with_name("La_predrera.txt") #Copia la misma ruta pero cambiando el archivo
print(guia2)

print(guia.parent) #Apunto al padre del directorio
guia = Path(Path.home(),"Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)


guia= Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa= guia.relative_to(Path("Europa"))
en_espania=guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)

