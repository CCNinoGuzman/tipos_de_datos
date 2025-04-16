# Esto es un comentario

'''
Es un comentario basicamente
de varias lineas
'''

#La variable edad hace referencia a la edad de una mascota
edad = 27

'''Una variable de tipo entero'''
ejemplo = 20
numero = 2

'''Una variable de tipo decimal'''
decimal = 3.141516

'''Una variable de tipo string o cadena de texto'''
nombre = "\"nicolas\"" 
apellido = "Sabogal"

'''Una variable de tipo booleana'''
verdadero = True
falso = False

'''Una variabla vacía'''
vacia = None

'''Como mostar o imprimr un datos en consola, 
usamos la función global print()'''
#print(vacia)
#print(edad)

'''Para solicitar datos al usuario,
usamos la función global input(), esta funcion recibe un texto'''
#nombre = input("Ingresa tu nombre:\t")

'''Concatenar string con el simbolo  +'''
#print("Tu nombre es: "+nombre)

'''Concatenar string mas número con simbolo ,'''
#edad = input("Ingresa tu edad:\t") 
#print("Tu edad es: ", edad)
#print("Vas a cumplir el otro año:\t")

#numero_uno = int( input("Ingrese un número:\t") )
#numero_dos = int( input("Ingrese otro número:\t") )
#resultado = numero_uno + numero_dos 
#print("La suma es: ", resultado)

'''Operaciones '''

numero_uno = 2
numero_dos = 5


#suma
numero_uno + numero_dos

#resta
numero_uno - numero_dos

#Multiplicación
numero_uno * numero_dos

#Dividir
numero_uno / numero_dos

#Modulo
numero_uno % numero_dos
#print("Modulo: ",(3 % 3))

#Elevar al cuadrado
numero_uno**2
#print("El cuadro de 3 es:\t", (3**2))

'''Incrementar una variable por uno, 
esto sirve para todas las operaciones'''
numero_uno += 1



'''Condicionales'''

#par
numero = int(input("ingrese un número: "))
modulo = numero % 2
#Palabra reservada if + condición + :
if modulo == 0:
    variable_creada = "Hola, me crearon desde el if"
    print("El número es par")
else:
    print("El número no es par")

#print(variable_creada)

numero = 10
numero_usuario = int(input("Ingrese un número:\t"))

if numero_usuario == numero:
    print("Los números son iguales")
elif numero_usuario < numero:
    print("El número del usuario es menor")
else:
    print("El número del usuario es mayor")
    print("Hola")
print("Sss")


print('+++')

'''
    range(3) = Lista de 3 = [0,1,2]
    range(5) = Lista de 5 = [0,1,2,3,4]
'''

for x in range(3):
    for y in range(3):
        #print(y+1+(3*x), end="")
        if x != 0:
            print(y+1+(3*x), end="")
        else:
            print((y+1), end="")
    print()
print()

for x in range(3):
    print(x+1+(3*x),x+2+(3*x),x+3+(3*x))











#Camel case java c php ruby go
tipoDeDiagnostico = 1
holaMundo = 2
estoEsUnaVariable = 2

tipo_de_diagnostico = 2
hola_mundo = 3
esto_es_una_variable = 4