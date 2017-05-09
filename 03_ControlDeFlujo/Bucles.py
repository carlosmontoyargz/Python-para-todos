#!/usr/bin/python

edad = 0
while edad < 18:
    edad += 1
    print('Felicidades, tienes ' + str(edad))

edad = 0
while edad < 18:
    edad += 1
    if edad % 2 == 0:
        continue

    print('Felicidades, tienes ' + str(edad))

while True:
    entrada = raw_input("> ")
    if entrada == 'adios':
        break
    else:
        print(entrada)

salir = False
while not salir:
    entrada = raw_input(">> ")
    if entrada == 'adios':
        salir = True
    else:
        print(entrada)

# Ciclo for
secuencia = ['uno', 'dos', 'tres']
for elemento in secuencia:
    print(elemento)
