for x in ["Lapiz", "Cuaderno", "Borrador"]:
    print("Tijeras")

'''
range(10) = 0,1,2,3,4,5,6,7,8,9

range(1,10) = 1,2,3,4,5,6,7,8,9

range(1,10,3) = 1,4,7                

'''

for x in range(10,16): #10,11,12,13,14,15
    print(x)


'''whilecondicion:'''
'''ejecuta el codigo siempre y cuando la condicion sea verdadera'''


'''while True:
print("Bienvenidos") '''

contraseña = 123

ing_contra = int(input("Ingresa la contraseña correcta: "))

if contraseña != ing_contra:
    for x in range(5):
        print("Contraseña incorrecta, vuelva a escribir")
else:
     print("Contraseña correcta")


'''
if contraseña == ing_contra:
    print("Contraseña correcta")
while contraseña != ing_contra:
    print("Contraseña incorrecta")'''


n = int(input("Ingrese un número: "))
x = 1

while x<=n:
    print(x)
    x += 1

print("Fin")



