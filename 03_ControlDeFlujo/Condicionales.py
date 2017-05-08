#!/usr/bin/env python

fav = "The Beatles"

if fav == "The Beatles":
    print("Tienes buen gusto!")
    print("The Beatles es una excelente banda")
else:
    print('Vaya, que lastima')
    print('No hay problema')

var = 2
if var > 3:
    print('var es mayor que 3')
elif var > 2:
    print('var es mayor que 2')
elif var > 1:
    print('var es mayor que 1')
else:
    print('var es igual o menor que 1')

num = 11
variable = 'Par' if (num % 2 == 0) else 'Impar'
print(variable)
