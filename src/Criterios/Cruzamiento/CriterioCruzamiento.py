from pandas import DataFrame, Series
import pandas

# TODO Definir un tipo de CriterioCruzamiento

# Simple
# Multi Punto
# Binomial
# Mascara
# Azar


class CriterioCruzamiento:
    def cruzar(self, individuo_1: Series, individuo_2: Series, dataset: DataFrame) -> Series:
        return individuo_1


class CruzaSimple(CriterioCruzamiento):
    def cruzar(self, individuo_1: Series, individuo_2: Series, dataset: DataFrame) -> Series:
        return individuo_1


class CruzaModular(CriterioCruzamiento):
    def cruzar(self, individuo_1: Series, individuo_2: Series, dataset: DataFrame) -> Series:
        # retornar iloc del dataset donde el indice sea el promedio entero entre los dos individuos
        return dataset.iloc[int((individuo_1.name + individuo_2.name) / 2)]
