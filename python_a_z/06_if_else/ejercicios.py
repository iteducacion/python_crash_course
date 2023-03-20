

# Ejercicio 1

number = int(input("Por favor, introduce un número: "))

if ( number == 0 ):
    print("El número es cero")
elif ( number > 0 ):
    print("El número es positivo")
else:
    print("El número es negativo")

# Ejercicio 2


name = input("Por favor, introduce tu nombre: ")
if ( len(name) > 10 ):
    print("Tu nombre es mayor a 10 caracteres")
else:
    print("Tu nombre es menor a 10 caracteres")



# Ejercicio 3

name = input("Por favor, introduce tu nombre: ")

text_long_nombre = "Tu nombre es mayor a 10 caracteres" if len(name) > 10 else "Tu nombre es menor a 10 caracteres"
print(text_long_nombre)


# Ejercicio 4

x = int(input("Por favor, introduce un número entero positivo: "))
if ( x < 0 ):
    print("El número introducido no es positivo")
    exit()
y = int(input("Por favor, introduce un número entero positivo: "))
if ( y < 0 ):
    print("El número introducido no es positivo")
    exit()
if ( x >= y ):
    print("El primer número es mayor o igual que el segundo")
else:
    print("El primer número es menor que el segundo")


# Ejercicio 5


x = int(input("Por favor, introduce un número entero positivo: "))
if ( x < 0 ):
    print("El número introducido no es positivo")
    exit()
y = int(input("Por favor, introduce un número entero positivo: "))
if ( y < 0 ):
    print("El número introducido no es positivo")
    exit()
if ( x >= y ):
    if ( x % y == 0 ):
        print("La división es exacta y el cociente es: ", x // y)
    else:
        print("La división no es exacta y el cociente es: ", x // y, " y el resto es: ", x % y)


# Ejercicio 6

x = int(input("Por favor, introduce un número entero positivo: "))
if ( x < 0 ):
    print("El número introducido no es positivo")
    exit()
y = int(input("Por favor, introduce un número entero positivo: "))
if ( y < 0 ):
    print("El número introducido no es positivo")
    exit()
if ( x >= y ):
    if ( x % y == 0 ):
        print("La división es exacta y el cociente es: ", x // y)
    else:
        print("La división no es exacta y el cociente es: ", x // y, " y el resto es: ", x % y)


# Ejercicio 7

# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
# Devuelve por pantalla el resultado en cada caso.

X = int(input("Por favor, introduce un número entero positivo: "))
if ( X < 0 ):
    print("El número introducido no es positivo")
    exit()
Y = int(input("Por favor, introduce un número entero positivo: "))
if ( Y < 0 ):
    print("El número introducido no es positivo")
    exit()
if ( X >= Y ):
    if ( X % Y == 0 ):
        print("El mayor es múltiplo del menor")
    else:
        print("El mayor no es múltiplo del menor")

# Ejercicio 8

# Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
# por pantalla el resultado en cada caso.

word = input("Por favor, introduce una palabra: ")
if ( word[0].isupper() ):
    print("La palabra empieza por mayúscula")
else:
    print("La palabra NO empieza por mayúscula")


# Ejercicio 9

# Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
# de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño
# PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones


letter = input("Por favor, introduce una letra: ")
if ( len(letter) > 1 ):
    print("No se puede procesar el dato, pues debe tener como máximo tamaño 1")
    exit()
if ( letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u" ):
    print("Es una vocal")
else:
    print("No es una vocal")

# Ejercicio 10




# ax2 + bx + c = 0
# haz que el usuario introduzca los valores de los coeficientes a, b, c. Con ello,
# 1. Comprueba que el coeficiente a es distinto de 0
# 2. En función del discriminante, calcula cuántas soluciones va a tener la ecuación de segundo grado
# ax2 + bx + c = 0.
# 3. Devuelve por pantalla el resultado en cada caso (tanto el número de soluciones en los números reales
# como el valor de éstas).
# PISTA: Para calcular la raíz cuadrada, vas a necesitar la función math.sqrt() de la librería math

import math

a = int(input("Por favor, introduce el valor del coeficiente a: "))
if ( a == 0 ):
    print("El coeficiente a no puede ser 0")
    exit()
b = int(input("Por favor, introduce el valor del coeficiente b: "))
c = int(input("Por favor, introduce el valor del coeficiente c: "))

discriminante = b**2 - 4*a*c
if ( discriminante < 0 ):
    print("No tiene soluciones reales")
elif ( discriminante == 0 ):
    print("Tiene una solución real")
    print("x = ", -b / (2*a))
else:
    print("Tiene dos soluciones reales")
    print("x1 = ", (-b + math.sqrt(discriminante)) / (2*a))
    print("x2 = ", (-b - math.sqrt(discriminante)) / (2*a))













