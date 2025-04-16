'''Número Mayor
Solicita tres números y muestra cuál es el mayor. Si son iguales, indica que todos los números son iguales.
Ejemplo:
1,6,2
El mayor el es número 5
111
Todos los números son iguales'''

numero1 = int(input("ingresa el numero 1\t"))
numero2 = int(input("ingresa el numero 2\t"))
numero3 = int(input("ingresa el numero 3\t"))

if numero1 > numero2 and numero1 > numero3:
    print("el numero mayor es", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("el numero mayor es", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("el numero mayor es", numero3)
else:
    print("Todos los números son iguales")

