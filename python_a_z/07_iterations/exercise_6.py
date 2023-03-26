# Ejercicio 6
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
# números introducidos por el usuario (los extremos incluidos).

extremo_izquierdo   = int(input("Introduce el extremo izquierdo del intervalo: "))
extremo_derecho     = int(input("Introduce el extremo derecho del intervalo: "))
if extremo_izquierdo > extremo_derecho:
    print("El extremo izquierdo no puede ser mayor que el extremo derecho")
    exit()

for i in range(extremo_izquierdo, extremo_derecho + 1):
    print(i)
