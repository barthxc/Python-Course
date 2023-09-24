#Las funciones indefinidas args sirve para crear funciones con infinitos argumentos ejemplo:
#def sumar(*gato):  sumará todos los gatos que pongas

def suma_normal (a,b):
    return a+b
print(suma_normal(5,6))#No puedes añadir mas argumentos


#Como hacerlo con *Args

def suma(*args): #Lo importante es el asterisco * no es necesroi usr args
    total=0

    for arg in args:
        total +=arg
    return total

print(suma(5,6,7,3,4,5,6,7,56,4))



def numero_persona(nombre,*args):
    lista=[]
    for arg in args:
        lista.append(arg)
    return f"{nombre}, la suma de tus números es {lista}"