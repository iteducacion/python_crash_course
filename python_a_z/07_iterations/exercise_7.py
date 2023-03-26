# Ejercicio 7
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.

extremo_izquierdo   = int(input("Introduce el extremo izquierdo del intervalo: "))
extremo_derecho     = int(input("Introduce el extremo derecho del intervalo: "))
total               = 0
if extremo_izquierdo > extremo_derecho:
    print("El extremo izquierdo no puede ser mayor que el extremo derecho")
    exit()

for i in range(extremo_izquierdo, extremo_derecho + 1):
    if i % 3 == 0:
        print(i)
        total += i
print("La suma de todos los múltiplos de 3 es de {}".format(total))


