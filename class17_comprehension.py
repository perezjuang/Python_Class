#Dictionary comprehension - list comprehension
#Dictionary comprehension y list comprehension nos permite escribir listas o diccionarios de forma más sencilla.

#Números pares

pares = []

for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)
#Esto mismo lo podemos expresar con una list comprehension

pares = [num for num in range(1,31) if num % 2 == 0]

#==============================================================
cuadrados = {}
for num in range(1,11):
    cuadrados[num] = num**2

squares = {num: num**2 for num in range(1,11)}