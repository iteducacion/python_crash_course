
# Ejercicio 5
# Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
# número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.

number = 1
cant_input_numbers = 0
total = 0
while number != 0:
    number = float(input("Introduce un número: "))
    if number == 0:
        break
    cant_input_numbers += 1
    total += number
print("La media aritmética de los números introducidos es de {}".format(total / cant_input_numbers))


