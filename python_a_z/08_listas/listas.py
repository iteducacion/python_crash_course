




nombres = ["Juan", "Karla", "Ricardo", "Maria"]

print(nombres[2:3])



A = []
for i in range(4):
    A.append([])
    for j in range(4):
        A[i].append(float(input("Introduce el elemento ({},{}): ".format(i,j))))

print(A)

