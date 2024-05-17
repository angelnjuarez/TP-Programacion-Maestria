import numpy as np
from Estudiante import Estudiante
from MateriaFactory import MateriaFactory


class Universidad:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = dict()
        self.__materias = dict()

    def ingresar_estudiante(self, nombre, apellido, legajo):
        self.__estudiantes[legajo] = Estudiante(nombre, apellido, legajo)

    def ingresar_materia(self, nombre, promediable):
        self.__materias[nombre] = MateriaFactory.crear_materia(nombre, promediable)

    def ingresar_nota(self, legajo, nombre_materia, nota):
        if legajo in self.__estudiantes or nombre_materia in self.__materias:
            self.__materias[nombre_materia].agregar_nota(legajo, nota)
        else:
            raise ValueError("Legajo o materia no encontrados")

    def promedio_general(self):
        for materia in self.__materias.values():
            for estudiante in self.__estudiantes.values():
                nota = materia.calcular_nota(estudiante.get_legajo())
                estudiante.agregar_nota(materia.get_nombre, nota)
        if len(self.__estudiantes) != 0:
            promedios = np.array([])
            for estudiante in self.__estudiantes.values():
                promedios = np.append(promedios, estudiante.calcular_promedio())
            print(promedios)
            return np.mean(promedios)
        else:
            raise ValueError("No hay estudiantes ingresados")

    def get_nombre(self):
        return self.__nombre


if __name__ == "__main__":
    universidad = Universidad("UTN")
    universidad.ingresar_estudiante("Juan", "Perez", 1234)
    universidad.ingresar_estudiante("Pedro", "Gomez", 1235)
    universidad.ingresar_materia("Algebra", True)
    universidad.ingresar_materia("Analisis", True)
    universidad.ingresar_materia("Quimica", False)
    universidad.ingresar_nota(1234, "Algebra", 8)
    universidad.ingresar_nota(1234, "Algebra", 8)
    universidad.ingresar_nota(1234, "Analisis", 6)
    universidad.ingresar_nota(1234, "Analisis", 4)
    universidad.ingresar_nota(1234, "Quimica", 9)
    universidad.ingresar_nota(1234, "Quimica", 7)
    universidad.ingresar_nota(1234, "Quimica", 7)
    universidad.ingresar_nota(1235, "Algebra", 9)
    universidad.ingresar_nota(1235, "Algebra", 1)
    universidad.ingresar_nota(1235, "Analisis", 9)
    universidad.ingresar_nota(1235, "Analisis", 8)
    universidad.ingresar_nota(1235, "Quimica", 6)
    universidad.ingresar_nota(1235, "Quimica", 6)
    universidad.ingresar_nota(1235, "Quimica", 6)

    print(universidad.promedio_general())
