import numpy as np
from Materia import Materia


class Promocionable(Materia):
    def __init__(self, nombre):
        super().__init__(nombre)

    def calcular_nota(self, legajo):
        if legajo not in self._notas_estudiante:
            raise ValueError(f"El alumno con legajo {legajo} no tiene notas cargadas")
        elif len(self._notas_estudiante[legajo]) != 2:
            raise ValueError(
                f"El alumno con legajo {legajo} debe tener 2 notas cargadas"
            )
        else:
            return np.mean(self._notas_estudiante[legajo])
