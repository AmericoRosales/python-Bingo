nombres = "Karina", "Leonardo", "Americo"

print("Los participantes de este curso son: ",nombres)
print(nombres[0].upper())

lista_clientes = [1, "C0001", "Pepito", True, 100]

print(lista_clientes[4])

consola = ["PS5", "xbox", "nintendo"]

print(consola[0].lower())
print(consola[1].capitalize())
print(len(consola[2]))

alumnos = ["Luis", "Mariana", "Carlos", "Fabiola", "Enrique", "Valeria", "Sara", "Juan"]

print(alumnos[-3])
print(alumnos[-6])

colores = ["Verde", "Rojo", "Azul", "Amarillo", "Celeste"]
notas = [16, 20, 14, 18]

print("El color elegido es el "+colores[2].upper()+".")
print("El promedio final es de ",(notas[0]+notas[1]+notas[2]+notas[3])/4)

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

dias[0] = "Lunes 05"
dias[1] = "Martes 06"

print(dias)

dias.append("Sabado")
dias.append("Domingo")

print(dias)


canciones = []

canciones.append("505")
canciones.append("R u mine")
canciones.append("Next Semester")

print("canciones: ",canciones)
