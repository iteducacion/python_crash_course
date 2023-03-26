# Ejercicio 10
# Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar:
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *



square = int(input("Introduce un número entero para el cuadrado y base del triangulo: "))
for i in range(1, square + 1):
    print(("* " * i), "  " * (square - i) , "* " * square)
