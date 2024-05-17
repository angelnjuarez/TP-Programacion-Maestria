from Promocionable import Promocionable
from FinalObligatorio import FinalObligatorio


class MateriaFactory:
    @staticmethod
    def crear_materia(nombre, promediable):
        if promediable:
            return Promocionable(nombre)
        else:
            return FinalObligatorio(nombre)
