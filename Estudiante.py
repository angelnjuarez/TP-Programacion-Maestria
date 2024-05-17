import numpy as np


class Estudiante:

    def __init__(self, nom, apel, leg):
        self.__legajo = leg
        self.__nombre = nom
        self.__apellido = apel
        self.__libreta = dict()

    def agregar_nota(self, materia, nota):
        self.__libreta[materia] = nota

    def calcular_promedio(self):
        return np.mean(list(self.__libreta.values()))

    def get_legajo(self):
        return self.__legajo

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_libreta(self):
        return self.__libreta

    def __str__(self):
        return f"{self.__legajo} {self.__nombre} {self.__apellido}"
