'''Calculadora de Propinas
Escribe un programa que calcule la cantidad de propina que se debe dejar en un restaurante. El programa debe:
Solicitar el monto total de la cuenta.
Preguntar qué porcentaje de propina se desea dejar (por ejemplo, 10%, 15%, 20%).
Calcular y mostrar el monto de la propina y el total a pagar (cuenta + propina).
Ejemplo: Ingrese el monto total de la cuenta: 100
Ingrese el porcentaje de propina que desea dejar: 15
La propina es: 15
El total a pagar es: 115'''

#solicitar el monto total de la cuenta
total_cuenta = int(input("por favor ingrese el total del valor de la cuenta "))

#solicitar porcentaje de propina
propina = int(input("ingrese el porcentaje de la propina que decea incluir en el total de la cuenta "))

#muestra la propina
print("la propina es: ", propina, "%")

#operación para el porcentaje
porcentje = total_cuenta/100*propina

#impprime el total de la cuenta con el porcentaje de la propina
print("el total a pagar es: $", int((total_cuenta + porcentje)))