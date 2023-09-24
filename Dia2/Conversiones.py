#Conversiones implicitas - Esto es un comentario
num1=20
num2=30.5
num1=num1+num2

print(type(num1))
print(type(num2))


#Conversiones explicitas
num1=5.8
print(num1)
print(type(num1))

num2=int(num1)
print(num2)
print(type(num2))

#Probaremos ahora

edad=input("Dime tu edad:")
print(type(edad))
edad=int(edad)
print(type(edad))
nueva_edad=1+edad

print("Vas a cumplir "+nueva_edad)



