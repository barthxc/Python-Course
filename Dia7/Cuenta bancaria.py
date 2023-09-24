import random
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    #Metodo 1
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Nº: {self.numero_cuenta}\n Saldo: {self.balance} €"

    #Metod 2
    def depositar(self, ingreso):
        self.balance += ingreso
        print(f"Ingreso aceptado {ingreso}")

    def retirar(self,retiro):
        if self.balance >= retiro:
            self.balance-=retiro
            print("Retiro acepatdo")
        else:
            print("Dinero insuficiente")

def crea_cliente():
    nombre_cliente = input("Dime tu nombre: ")
    apellido_cliente = input("Dime tu apellido: ")
    numero_cuenta = random.randint(10000000, 99999999)
    cliente = Cliente(nombre_cliente,apellido_cliente,numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crea_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()
        if opcion == 'D':
            ingreso = int(input("Cantidad de dinero para ingresar: "))
            mi_cliente.depositar(ingreso)
        elif opcion == 'R':
            retiro = int(input("Cantidad que desea retirar: "))
            mi_cliente.retirar(retiro)
        print(mi_cliente)

    print('Gracias por operar en BancoPython')

inicio()
