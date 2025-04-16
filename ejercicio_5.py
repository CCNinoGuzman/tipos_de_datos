'''
Calculadora Básica
Crea un programa que funcione como calculadora simple. Debe permitir sumar, restar,
multiplicar o dividir dos números. El usuario elige la operación y luego ingresa los
números.
'''

print("por favor seleccione la operacion que desea hacer: ")
print("1. SUMAR ")
print("2. RESTAR ")
print("3. MULTIPLICAR ")
print("4. DIVIR ")

option = int(input("por favor seleccione el numero de la operacion que desea hacer: "))

#ingresar datos
numero1 = int(input("ingresa el  primer valor: "))
numero2 = int(input("ingresa el segundo valor: "))

if option == 1:
    resultado = numero1 + numero2
    print ("el suma es: ", resultado)
elif option == 2:
    resultado = numero1 - numero2
    print ("el resta es: ", resultado)
elif option == 3:
    resultado = numero1 * numero2
    print ("la multiplcacion es: ", resultado)
elif option == 4:
    resultado = numero1 / numero2
    print ("la divición es: ", resultado)
else:
    print ("valor incorrecto")
