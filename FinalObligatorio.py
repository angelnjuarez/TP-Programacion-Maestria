from Materia import Materia


class FinalObligatorio(Materia):
    def __init__(self, nombre):
        super().__init__(nombre)

    def calcular_nota(self, legajo):
        if legajo not in self._notas_estudiante:
            raise ValueError(f"El alumno con legajo {legajo} no tiene notas cargadas")
        if len(self._notas_estudiante[legajo]) != 3:
            raise ValueError(
                f"El alumno con legajo {legajo} debe tener tres notas cargadas"
            )

        notas = self._notas_estudiante[legajo]
        if notas[0] + notas[1] < 8:
            return 0
        return notas[2]
