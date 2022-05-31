from pandas import DataFrame, Series
import pandas

# TODO Definir un tipo de CriterioCruzamiento

# Simple
# Multi Punto
# Binomial
# Mascara
# Azar


class CriterioCruzamiento:
    def cruzar(self, individuo_1: Series, individuo_2: Series) -> Series:
        return individuo_1


class CruzaSimple(CriterioCruzamiento):
    def cruzar(self, individuo_1: Series, individuo_2: Series) -> Series:
        return individuo_1
