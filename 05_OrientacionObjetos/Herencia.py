#!/usr/bin/python
"""Herencia en Python."""


class Instrumento:
    """Abstraccion de un instrumento musical."""

    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print('Se ha tocado el instrumento')

    def romper(self):
        print('Has roto el instrumento. Son $' + str(self.precio))


class Guitarra(Instrumento):
    """Clase que representa una guitarra."""

    def __init__(self, precio, numCuerdas):
        Instrumento.__init__(self, precio)
        self.NumeroCuerdas = numCuerdas

    def tocar(self):
        print('Se ha tocado la guitarra con ' + str(self.NumeroCuerdas)
              + ' cuerdas')

    def romper(self):
        print('Has roto la guitarra. Son $' + str(self.precio))


class Bateria(Instrumento):
    pass


guitarra = Guitarra(1000, 6)
bateria = Bateria(3500)

guitarra.tocar()
bateria.tocar()
guitarra.romper()
bateria.romper()
