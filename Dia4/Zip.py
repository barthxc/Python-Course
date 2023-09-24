#Suma o mezcla listas para convertirlas en una tupla ejemplo:
#lista_nombres['Pablo','Sol','Botella']
#edades[1,2,3]
#mi_tupla_zip[(1,'Pablo'),(2,'Sol'),(3,'Botella')]

nombres=['Ana','Hugo','Valeria']
edades=[65,29,42]
ciudades=['Lima','Madrid','Mexio']
combinado=zip(nombres,edades)

print(combinado) #No muestra nuesta tupla combinada. Muestra donde está (en la memoria)

combinado=list(zip(nombres,edades,ciudades))
print(combinado)

#SI HAY UN DATO MAS NO SE ROMPE, SOLO CORRESPONDE HASTA LA LISTA MAS CORTA
#NO HACE UN OUT OF BOUND

for nombre,edad,ciudad in combinado:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")


capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
mi_zip=list(zip(capitales,paises))
for capital,pais in mi_zip:
    print(f"La capital de {pais} es {capital}")




español=['uno','dos','tre','cuatro','cinco']
portugues=['um','dois','três','quatro','cinco']
ingles=['one','two','three','four','five']

tupla_idioma=list(zip(español,portugues,ingles))
print(tupla_idioma)