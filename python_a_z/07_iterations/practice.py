




s = "Predecir el futuro es muy dificil, especialmente cuando se trata del futuro".lower()
print(s)


# letter_delete = input("Introduce la letra que desea eliminar del string original: ").lower()
letter_delete = ['a','e']



for letter in s:
    if letter in letter_delete:
        continue
    print(letter, end="")
print(s)





############################################################################################################


s = "La vaca hace muuuu"

i       = 0
vocales = 0
while i < len(s):
    if ( s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" ):
        vocales += 1
    i += 1

print("Hay", vocales, "vocales")



string = "Mi mama me mima, esa es mi mama"
s_inv = ""

for caracter in string:
    s_inv = caracter + s_inv

print(s_inv)



numeros = range(0, 100, 10)

for num in numeros:
    print(num)



volver_a_contar = True
while volver_a_contar:
    progresion = int(input("Por favor, introduce un número entero positivo, que va a ser la progresión de conteo hasta 1000: "))
    if ( progresion < 0 ):
        print("El número introducido no es positivo")
        exit()

    for number in range(0, 1000, progresion):
        print(number)

    volver_a_contar = input("¿Quieres volver a contar? (s/n): ") == "s"

print("Hasta luego")







