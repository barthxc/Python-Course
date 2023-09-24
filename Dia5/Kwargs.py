#KeyWord args
#Trabaja con diccionarios

def suma(**kwargs):
    total=0 #Vamos a sumar los valores
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total+=valor
    return total
print(suma(x=3,y=5, z=2)) #Para esto como un diccionario


#MEZCLA DE FUNCIONES

def prueba(num1,num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")
    for arg in args:
        print(f"Arg = {arg}")
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
#Le paso los 2 ptimeros parámetros num1,num2
prueba(15,34,100,200,300,400, x='uno',y='dos',z='tres') #Después le paso los KWARGS que deben ser K + valor
#Después le paso los args infinitamente

#se pueden pasar lista de numeros y diccionarios dentro de mi función
