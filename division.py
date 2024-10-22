#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

usuario_numero1 = 0
usuario_numero2 = 0

usuario_numero1 = float(input("Dime un número: "))

usuario_numero2 = float(input("Dime otro número: "))

print("La división de ambos números es:  ")
print(usuario_numero1 / usuario_numero2)

if usuario_numero2 == 0:
    print("error, no se puede dividir por 0")