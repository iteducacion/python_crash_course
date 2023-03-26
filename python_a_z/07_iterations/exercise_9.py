
# Ejercicio 9
# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).

age = int(input("Introduce tu edad: "))
current_year = int(input("Introduce el año actual: "))
birth_year = current_year - age
for i in range(birth_year, current_year + 1):
    print(i)

