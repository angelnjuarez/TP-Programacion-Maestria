from abc import ABC, abstractmethod


class Materia(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self._notas_estudiante = dict()

    def agregar_nota(self, legajo, nota):
        if legajo in self._notas_estudiante:
            self._notas_estudiante[legajo].append(nota)
        else:
            notas = [nota]
            self._notas_estudiante[legajo] = notas

    @abstractmethod
    def calcular_nota(self, legajo):
        pass

    def get_nombre(self):
        return self.nombre

    def get_notas(self):
        return self._notas_estudiante.values()
