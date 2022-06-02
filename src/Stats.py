from pickle import NONE
from pandas import DataFrame, Series
from FuncionAptitud import FuncionAptitud

from utils import stats_poblacion
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class Stats:
    def __init__(self):
        self.corridas = []
        self.mejor = None
        self.peor = None
        self.funcionAptitud = None

    def setFunctionAptitud(self, funcionAptitud: FuncionAptitud):
        self.funcionAptitud = funcionAptitud

    def saveStats(self, poblacion: DataFrame):

        # Calculo funcion de aptitud
        poblacion["aptitud"] = self.funcionAptitud.evaluar(poblacion)

        # Ordena la poblacion por aptitud
        poblacion.sort_values(by="aptitud", ascending=False, inplace=True)

        # Obtiene al mejor, peor y un promedio de los valores de aptitud
        mejor = poblacion.head(
            1)[["ID", "titulo", "aptitud", "genero", "subgenero", "precio", "idioma", "numero_paginas", "fechaPublicacion"]].iloc[0].to_dict()
        peor = poblacion.tail(1)[["ID", "titulo", "aptitud", "genero", "subgenero",
                                  "precio", "idioma", "numero_paginas", "fechaPublicacion"]].iloc[0].to_dict()

        promedio = poblacion.aptitud.mean()
        varianza = poblacion.aptitud.var()

        lowerQuartile = poblacion.aptitud.quantile(0.25)
        upperQuartile = poblacion.aptitud.quantile(0.75)

        # print("Mejor:", mejor)
        # print("Peor:", peor)
        # print("Percentil 25:", lowerQuartile)
        # print("Percentil 75:", upperQuartile)

        promedio = {"aptitud": promedio}
        lowerQuartile = {"aptitud": lowerQuartile}
        upperQuartile = {"aptitud": upperQuartile}

        # Guardar al mejor y al peor
        self.mejor = self.mejor if self.mejor is not None and self.mejor[
            "aptitud"] >= mejor["aptitud"] else mejor
        self.peor = self.peor if self.peor is not None and self.peor[
            "aptitud"] <= peor["aptitud"] else peor

        corrida = {"mejor": mejor, "peor": peor, "promedio": promedio,
                   "lowerQuartile": lowerQuartile, "upperQuartile": upperQuartile, "varianza": varianza}
        self.corridas.append(corrida)
        print("Corrida guardada", corrida)

    def getStats(self):
        return self.corridas

    def showPlot(self):
        # Graficar corridas con Mejor ,Peor y Promedio por cada una de ellas
        promedios = [corrida["promedio"]["aptitud"]
                     for corrida in self.corridas]
        mejores = [corrida["mejor"]["aptitud"] for corrida in self.corridas]
        peores = [corrida["peor"]["aptitud"] for corrida in self.corridas]
        lowerQuartiles = [corrida["lowerQuartile"]["aptitud"]
                          for corrida in self.corridas]
        upperQuartiles = [corrida["upperQuartile"]["aptitud"]
                          for corrida in self.corridas]

        varianzas = [corrida["varianza"] for corrida in self.corridas]

        # selecciona los indices de las generaciones para el grafico
        if len(promedios) < 5:
            x = np.arange(len(promedios))
        else:
            x = np.arange(0, len(promedios) + 1, len(promedios) // 5)

        plt.title('Aptitud por Generacion')
        plt.xlabel("Generaciones")
        plt.ylabel("Aptitud")
        plt.xticks(x, x)
        plt.plot(promedios, label="Promedio")
        plt.plot(mejores, label="Mejor")
        plt.plot(peores, label="Peor")
        plt.plot(lowerQuartiles, label="Cuantil Inferior")
        plt.plot(upperQuartiles, label="Cuantil Superior")
        # plt.plot(varianzas, label="Varianza")
        plt.legend()
        plt.show()

    def showStats(self):
        # for corrida in self.corridas:
        #     print("Mejor:", corrida["mejor"])
        #     print("Peor:", corrida["peor"])
        #     print("Promedio:", corrida["promedio"])
        #     print("---------------------------------")
        print("Mejor:", self.mejor)
        print("Peor:", self.peor)
        print("Funcion de Aptitud:", self.funcionAptitud)

    def showStatsPoblacion(self, poblacion: DataFrame):
        stats_poblacion(poblacion)


if __name__ == "__main__":

    s = Series([1, 2,  4, 5, 6, 8, 9])
    print(s.quantile(0.75, interpolation="midpoint"))
