

# Ejercicio 1

s1 = "Había una vez, "
s2 = "un barco chiquito, "
s3 = "que no podía, "
s4 = "que no podía navegar."

print (s1 + s2[:-2] + " " + s1 + s2 +s3*2 + s4)


# Ejercicio 2

s1 = "Érase un hombre a una nariz pegado,"
s2 = "Érase una nariz superlativa,"
s3 = "Érase una alquitara medio viva,"
s4 = "Érase un peje espada mal barbado;"

print( s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n")


# Ejercicio 3

s1 = "me encantan las matemáticas"
print(s1.upper())




s = "Pablito clava un clavito"
print(s[2:10])

exit()




# Ejercicio 4

s1 = "Mi pasión por el chocolate es superior a mis fuerzas"
print(len(s1))

# Ejercicio 5

s1              = "Mi pasión por el chocolate es superior a mis fuerzas"
index_chocolate = s1.find("chocolate")
s_sub           = s1[index_chocolate:index_chocolate + len("chocolate")]
print(s_sub)

# Ejercicio 6

nombre = input("Por favor, introduce tu nombre: ")


# Ejercicio 7

lastname = input("Por favor, introduce tu apellido: ")

# Ejercicio 8

age = int(input("Por favor, introduce tu edad: "))

# Ejercicio 9

city = input("Por favor, introduce tu ciudad: ")

# Ejercicio 10

print( "Su nombre es " + nombre + " " + lastname + ", tiene " + str(age) + " años y vive en " + city + ".")




