


import cmath


z = 1 + 2j


radians = cmath.phase(z) # angle in radians
polar   = cmath.polar(z) # (abs, angle) Pasamos a forma polar
b = cmath.rect(1, 2) # (abs, angle)
c = cmath.exp(z) # e^z


print(radians)
print(polar)
print(b)
print(c)




z.conjugate()
z.real
z.imag
# z.abs()


# format
name    = 'Juan Pablo'
lastname= 'Gonzalez'
age     = 30
# format
print('My name is {} {} and I am {} years old'.format(name, lastname, age))
# f-strings
print(f'My name is {name} {lastname} and I am {age} years old')
# tabulaciones 
print('My name is \t {} {} and I am {} years old'.format(name, lastname, age))
# new line
print('My name is \n {} {} and I am {} years old'.format(name, lastname, age))


frase_futbol = 'El Barcelona es el mejor equipo del mundo'
equipo = frase_futbol[3:12]
print(equipo)
de_donde = frase_futbol[-5:]
print(de_donde)
# slicing
print(frase_futbol[3:12])


# funciones del string
frase_futbol.upper()
frase_futbol.lower()
frase_futbol.capitalize()
frase_futbol.title()
frase_futbol.count('e')
frase_futbol.find('e')
frase_futbol.replace('e', 'a')
frase_futbol.split(' ')
frase_futbol.split(' ')[0]
frase_futbol.swapcase()
frase_futbol.isalpha()
frase_futbol.isalnum()
frase_futbol.isnumeric()
frase_futbol.islower()
frase_futbol.isupper()
frase_futbol.isspace()
frase_futbol.istitle()
frase_futbol.startswith('e')
frase_futbol.endswith('e')
frase_futbol.strip()
frase_futbol.lstrip()
frase_futbol.rstrip()
frase_futbol.center(50, '*')
frase_futbol.ljust(50, '*')
frase_futbol.rjust(50, '*')
frase_futbol.zfill(50)
frase_futbol.partition('e')
frase_futbol.rpartition('e')
frase_futbol.splitlines()
frase_futbol.join('***')
frase_futbol.encode()
frase_futbol.encode().decode()
frase_futbol.casefold()
frase_futbol.rsplit(' ')
frase_futbol.rsplit(' ', 1)
frase_futbol.index('e')
frase_futbol.rindex('e')
frase_futbol.expandtabs(10)
len(frase_futbol)

