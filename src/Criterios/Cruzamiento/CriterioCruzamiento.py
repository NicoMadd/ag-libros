from pandas import DataFrame, Series
import pandas

# TODO Definir un tipo de CriterioCruzamiento

# Simple
# Multi Punto
# Binomial
# Mascara
# Azar
from src import dataset


class CriterioCruzamiento:
    def cruzar(self, individuo_1: Series, individuo_2: Series, dataset: DataFrame) -> Series:
        return individuo_1


class CruzaSimple(CriterioCruzamiento):
    def cruzar(self, individuo_1: Series, individuo_2: Series, dataset: DataFrame) -> Series:
        # retornar iloc del dataset donde el indice sea el promedio entero entre los dosindividuos
        return dataset.iloc[int((individuo_1.name + individuo_2.name) / 2)]
