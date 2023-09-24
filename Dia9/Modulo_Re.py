import re
#expresiones regulares
#ejemplo: numero de móvil / teléfono
#patron = r'\d\d\d-\d\d\d-\d\d\d'
#patron = r'\d{3}-\d{3}-\d{3}'

#Carácteres especiales:
#/d digito numerico
#/w caracteres alfanumérico
#/s espacio en planco
#/D NO es numerico
#/W NO es alfanumerico (signos) ??
#/S NO es un espacio en blanco

#Carácteres cuantificadores:
#+ 1 o mas veces se repide
#{n} se repetirá N veces
#{n,m} se repetirá entre N y M
#{n,} se repetir'a entre n a infinito
#* o o mas veces
#? 1 o 0 veces

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'
palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'
busqueda =re.search(patron, texto)
busqueda =re.findall(patron, texto)
print(len(busqueda))

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())



texto = 'llama al 564-525-6588 ya mismo'
patron= r'\d\d\d-\d\d\d-\d\d\d\d'
patron= re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron,texto)
print(resultado)
print(resultado.group())

clave= input('Clave: ')
patron= r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear)


texto = "No atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes', texto)
print(buscar)

buscar = re.search(r'\D$', texto)
print(buscar)