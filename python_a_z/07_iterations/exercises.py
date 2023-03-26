


# Ejercicio 1
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, muestra
# si el número introducido es par o impar.

num = 1
while num != 0:
    num = int(input("Introduce un número entero: "))
    if num == 0:
        break
    if num % 2 == 0:
        print("El número", num, "es par")
    else:
        print("El número", num, "es impar")


# Ejercicio 2
# Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
# letra o no e indícaselo al usuario por pantalla.

word        = input("Introduce una palabra: ")
user_letter = input("Introduce una letra: ")
dont_have_letter = True
for letter in word:
    if (letter == user_letter):
        dont_have_letter = False
        print("La palabra", word, "contiene la letra", user_letter)
        break
if dont_have_letter:
    print("La palabra", word, "no contiene la letra", user_letter)






# Ejercicio 3
# Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
# pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
# sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.

price = float(input("Introduce un precio: "))
if price == 0:
    print("No se ha introducido ningún precio")
    exit()
total_price = price
while price != 0:
    price = float(input("Introduce un precio: "))
    total_price += price
    if price == 0:
        break
    if total_price > 200:
        print("Se ha pasado de presupuesto de 200")
        break
print("El precio total es de ${}".format(total_price))




# Ejercicio 4
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
# cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.

positive_numbers = 0
negative_numbers = 0
number = 1
while number != 0:
    number = int(input("Introduce un número entero: "))
    if number == 0:
        break
    if number > 0:
        positive_numbers += 1
    else:
        negative_numbers += 1

print("Se han introducido {} números positivos y {} números negativos".format(positive_numbers, negative_numbers))













