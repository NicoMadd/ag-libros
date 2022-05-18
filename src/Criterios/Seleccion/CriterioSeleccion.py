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

    # subgrupo_minimo: int es el numero minimo de individuos que debe tener un subgrupo
    # fraccionamiento: float es la fraccion de individuos que se eligen del subgrupo final
    def __init__(self, subgrupo_minimo=2, fraccionamiento=0.1) -> None:
        self.subgrupo_minimo: int = subgrupo_minimo
        self.fraccionamiento: float = fraccionamiento

    @abstractmethod
    def seleccionar(self, poblacion: DataFrame) -> DataFrame:
        return poblacion


class Torneo(CriterioSeleccion):

    def __init__(self, subgrupo_minimo=2, fraccionamiento=0.1) -> None:
        super().__init__(subgrupo_minimo, fraccionamiento)

    def seleccionar(self, poblacion: DataFrame) -> DataFrame:
        return poblacion.sample(frac=self.fraccionamiento)


class Ranking(CriterioSeleccion):

    def __init__(self, subgrupo_minimo=2, fraccionamiento=0.1) -> None:
        super().__init__(subgrupo_minimo, fraccionamiento)

    def seleccionar(self, poblacion: DataFrame) -> DataFrame:
        # Separa la poblacion en subgrupos
        subgrupos = poblacion.groupby(
            np.arange(len(poblacion)) // self.subgrupo_minimo)
        df = DataFrame()
        for name, subgrupo in subgrupos:
            # Ordena los subgrupos por el valor de la funcion aptitud
            subgrupo["aptitud"] = FuncionAptitud().evaluar(subgrupo)
            subgrupo.sort_values(by=['aptitud'], ascending=False, inplace=True)
            # Selecciona el subgrupo final priorizando los mejores
            tamanio = math.ceil(len(subgrupo)*self.fraccionamiento)
            df = df.append(subgrupo.iloc[:tamanio])
        # une todos los subgrupos del pandas groupby
        return df
