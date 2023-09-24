mi_bool=4<5<6 #Esto dará verdadero y se puede hacer pero no hay operador lógico
mi_bool= 4<5 and 5<6 #Esto si está bien definido usando operadores lógicos

mi_bool= 10== 10 or 3==3

mi_bool= 'a' == 'a'
mi_bool= not 'a'=='a'



frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool= not palabra1 in frase and not palabra2 in frase