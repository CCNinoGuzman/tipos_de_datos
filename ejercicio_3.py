'''Patrón de Estrellas
Solicita al usuario un número y genera un triángulo de estrellas con esa cantidad de filas.
Ejemplo: Si el usuario ingresa 4, el programa imprime:
*
**
***
****'''

range_value = int(input("por favor ingresa un numero \t"))
for x in range(range_value):
    print("\n", "*", end="")
    if x>0:
        for y in range(x):
            print("*", end="")
        
