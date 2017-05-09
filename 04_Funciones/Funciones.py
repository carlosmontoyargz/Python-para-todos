#!/usr/bin/python


def funcion(param1, param2):
    """Esta funcion imprime los valores pasados como parametros."""
    print(param1)
    print(param2)


def funcion2(texto, veces=1):
    """Esta funcion imprime el texto el numero especificado de veces."""
    print(texto * veces)


def varios(param1, param2, *otros):
    """Funcion que muestra el paso variable de argumentos."""
    print(otros)
    for elemento in otros:
        print(elemento)


def varios2(param1, **otros):
    """Funcion que muestra el paso variable de argumentos y un diccionario."""
    for i in otros.items():
        print(i)


def sumar(sum1, sum2):
    """Funcion que suma dos numeros."""
    return sum1 + sum2


def tupla(x, y):
    """Funcion que retorna una tupla."""
    return x * 2, y + 1


funcion("hola", 2)
funcion2("adios ", 3)
funcion2('prueba')
varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)
varios2(1, segundo=2, tercero=3)
print(sumar(2, 4))
a, b = tupla(4, 10)
print(str(a) + " " + str(b))
