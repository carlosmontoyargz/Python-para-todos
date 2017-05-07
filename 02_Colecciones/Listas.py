#!/usr/bin/env python

lista = [22, True, "una lista", [1, 2]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3][0])
print(lista[3][1])
print(lista[-1])
print(lista[-2])
print("\n")

# Sublistas
lista1 = lista[0:2]
lista2 = lista[1:3]
lista3 = lista[0:4:2]
lista4 = lista[:2]
lista5 = lista[1:]
lista6 = lista[::2]
print(lista)
print(lista1)
print(lista4)
print(lista2)
print(lista3)
print(lista6)
print(lista5)
print("\n")

# Modificacion
lista[0:2] = [23, False]
print(lista)

lista[0:2] = ["hola :)"]
print(lista)
