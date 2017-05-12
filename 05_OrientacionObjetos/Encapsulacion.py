#!/usr/bin/python


class Ejemplo:

    def publico(self):
        print('Publico')

    def __privado(self):
        print('Privado')


class Fecha:

    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
            print('Dia configurado: ' + str(dia))
        else:
            print('error')


class Fecha2(object):

    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
            print('Dia configurado: ' + str(dia))
        else:
            print('error')

    dia = property(getDia, setDia)


ej = Ejemplo()
ej.publico()

mi_fecha = Fecha()
mi_fecha.setDia(18)

mi_fecha2 = Fecha2()
mi_fecha2.dia = 33
