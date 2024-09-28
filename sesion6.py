'''
nota = 15

if nota >= 11:
    print("Aprobado")
elif nota >= 13:
    print("Regular")
elif nota >= 16:
    print("Buena nota")
print("Fin del programa")

#Problema 1

cantidad = 0
n = int(input("¿Cuántos valores ingresará?: "))
for f in range(n):
    valor = int(input("Ingrese el valor: "))
    if valor >= 1000:
        cantidad += 1
print("La cantidad de valores ingresados son mayores o iguales a 1000")
print(cantidad)

#Problema 2

mul3 = 0
mul5 = 0
n = int(input("Ingrese la cantidad de multiplos a consultar: "))
for f in range(n):
    valor = int(input("Ingrese su multiplo: "))
    if valor%3 == 0:
        mul3 += 1 #mul3 = mul3 + 1
    if valor%5 == 0:
        mul5 += 1
print("Cantidad de valores ingresados multiplos de 3")
print(mul3)
print("Cantidad de valores ingresados multiplos de 5")
print(mul5)
'''
#Problema 3

n1 = int(input("Ingrese nota1: "))
n2 = int(input("Ingrese nota2: "))
n3 = int(input("Ingrese nota3: "))

promedio = (n1+n2+n3)/3

if n1 > 20 or n2 > 20 and n3 > 20:
    print("Agregue las notas correctas")
else:
    if promedio <= 10.5:
        print("Desaprobado")
    elif promedio <= 13:
        print("En proceso")
    elif promedio <= 16:
        print("Buena nota")
    elif promedio <=20:
        print("Aprobado")
    else:
        print("Agregue las notas correctas")