# TODO Definir un tipo de CriterioPoblacionInicial
from abc import abstractmethod
from pandas import DataFrame

# Al Azar
# Ad-Hoc


class CriterioPoblacionInicial:
    @abstractmethod
    def samplear(self, poblacion: DataFrame) -> DataFrame:
        return poblacion


# Se samplean cantidad de individuos fija y varianza constante

class AlAzar (CriterioPoblacionInicial):

    def __init__(self, tamano_poblacion: int = 10):
        self.tamanio_poblacion = tamano_poblacion

    def samplear(self, poblacion: DataFrame) -> DataFrame:
        return poblacion.sample(n=self.tamanio_poblacion)
