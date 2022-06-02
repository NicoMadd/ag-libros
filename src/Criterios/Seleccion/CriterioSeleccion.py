from abc import abstractmethod
import math
import numpy as np
from pandas import DataFrame
import pandas as pd

from FuncionAptitud import FuncionAptitud

# TODO Definir un tipo de CriterioSeleccion

## Metodos ##
## Torneo, Ranking, Ruleta, Control sobre numero esperado ##


class CriterioSeleccion:

    # fraccionamiento: float es la fraccion de individuos que se eligen del subgrupo final
    def __init__(self,  fraccionamiento=0.1) -> None:
        self.fraccionamiento: float = fraccionamiento

    @abstractmethod
    def seleccionar(self, poblacion: DataFrame) -> DataFrame:
        return poblacion

    def setFuncionAptitud(self, funcionAptitud: FuncionAptitud) -> None:
        self.funcionAptitud = funcionAptitud


class Torneo(CriterioSeleccion):

    def __init__(self,  fraccionamiento=0.5) -> None:
        super().__init__(fraccionamiento)

    def seleccionar(self, poblacion: DataFrame) -> DataFrame:
        # Separa la poblacion en subgrupos de a 2 individuos
        subgrupos = poblacion.groupby(
            np.arange(len(poblacion)) // 2)

        # Selecciona el mejor individuo de cada subgrupo
        df = DataFrame()
        for _, subgrupo in subgrupos:
            if subgrupo.shape[0] == 1:
                df = pd.concat([df, subgrupo.iloc[0:1]])
            subgrupo = subgrupo.sort_values(by="aptitud", ascending=False)
            df = pd.concat([df, subgrupo.iloc[0:1]])
        return df


class Ranking(CriterioSeleccion):

    def __init__(self, fraccionamiento=0.5) -> None:
        super().__init__(fraccionamiento)

    def seleccionar(self, subgrupo: DataFrame) -> DataFrame:
        # Ordena al subgrupo por el valor de la funcion aptitud
        subgrupo.sort_values(by=['aptitud'], ascending=False, inplace=True)
        # Selecciona el subgrupo final priorizando los mejores
        tamanio = math.floor(len(subgrupo)*self.fraccionamiento)
        return subgrupo.iloc[:tamanio]
