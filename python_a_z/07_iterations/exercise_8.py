# Ejercicio 8
# Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.

count_numbers = int(input("Introduce cuántos números vas a introducir: "))
total = 0
for i in range(count_numbers):
    number = int(input("Introduce un número: "))
    if i == 0:
        total = number
    else:
        total *= number

print("El producto de los números introducidos es de {}".format(total))