#!/usr/bin/python
"""Python orientado a objetos."""


class Coche:
    """Abstraccion de coche."""

    def __init__(self, gasolina):
        """Constructor de la clase."""
        self.gasolina = gasolina
        print('Tenemos ' + str(gasolina) + ' litros')

    def arrancar(self):
        """Comprueba si hay gasolina."""
        if self.gasolina > 0:
            print('Arranca')
        else:
            print('No arranca')

    def conducir(self):
        """Gasta una unidad de gasolina."""
        if self.gasolina > 0:
            self.gasolina -= 1
            print('Quedan ' + str(self.gasolina) + ' litros')
        else:
            print('No se mueve')


mi_coche = Coche(4)
print(mi_coche.gasolina)
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
