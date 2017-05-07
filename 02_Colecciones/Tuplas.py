#!/usr/bin/env python
# Los valores una tupla son inmutables, pero a cambio ocupan menos espacio
# en memoria que una lista.

tupla1 = (1, 2, True, "python")
tupla2 = ("un solo elemento",)  # Se agrega una coma para diferenciar entre
# tuplas y enteros

print(type(tupla1))
print(tupla1)
print(tupla2)
print(tupla1[1:3])
print(tupla1[::2])

c = "hola mundo"
print(c[3])
print(c[2:])
print(c[:7])
print(c[::3])
