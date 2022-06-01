from pandas import DataFrame
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

    def saveStats(self, poblacion: DataFrame):

        # Calculo funcion de aptitud
        poblacion["aptitud"] = FuncionAptitud().evaluar(poblacion)

        # Ordena la poblacion por aptitud
        poblacion.sort_values(by="aptitud", ascending=False, inplace=True)

        # Obtiene al mejor, peor y un promedio de los valores de aptitud
        mejor = poblacion.head(
            1)[["ID", "titulo", "aptitud"]].iloc[0].to_dict()
        peor = poblacion.tail(1)[["ID", "titulo", "aptitud"]].iloc[0].to_dict()
        promedio = poblacion.aptitud.mean()
        print("Mejor:", mejor)
        print("Peor:", peor)

        promedio = {"aptitud": promedio}

        # Guardar al mejor y al peor
        self.mejor = self.mejor if self.mejor is not None and self.mejor[
            "aptitud"] >= mejor["aptitud"] else mejor
        self.peor = self.peor if self.peor is not None and self.peor[
            "aptitud"] <= peor["aptitud"] else peor

        corrida = {"mejor": mejor, "peor": peor, "promedio": promedio}
        self.corridas.append(corrida)

    def getStats(self):
        return self.corridas

    def showPlot(self):
        # Graficar corridas con Mejor ,Peor y Promedio por cada una de ellas
        promedios = [corrida["promedio"]["aptitud"]
                     for corrida in self.corridas]
        mejores = [corrida["mejor"]["aptitud"] for corrida in self.corridas]
        peores = [corrida["peor"]["aptitud"] for corrida in self.corridas]

        # selecciona los indices de las generaciones para el grafico
        x = np.arange(0, len(promedios) + 1, len(promedios) // 5)

        plt.title('Aptitud por Generacion')
        plt.xlabel("Generaciones")
        plt.ylabel("Aptitud")
        plt.xticks(x, x)
        plt.plot(promedios, label="Promedio")
        plt.plot(mejores, label="Mejor")
        plt.plot(peores, label="Peor")
        plt.legend()
        plt.show()

    def showStats(self):
        for corrida in self.corridas:
            print("Mejor:", corrida["mejor"])
            print("Peor:", corrida["peor"])
            print("Promedio:", corrida["promedio"])
            print("---------------------------------")
        print("Mejor:", self.mejor)
        print("Peor:", self.peor)

    def showStatsPoblacion(self, poblacion: DataFrame):
        stats_poblacion(poblacion)


if __name__ == "__main__":
    stats = Stats()

    # generate random stats
    stats.saveStats(DataFrame({"ID": [1, 2, 3], "titulo": [
                    "a", "b", "c"], "aptitud": [1, 2, 3]}))
    stats.saveStats(DataFrame({"ID": [122, 2222, 3222], "titulo": [
                    "aaa", "bbb", "ccc"], "aptitud": [100, 0, 32]}))
    stats.saveStats(DataFrame({"ID": [1, 2, 3], "titulo": [
                    "a", "b", "c"], "aptitud": [1, 2, 3]}))
    stats.saveStats(DataFrame({"ID": [122, 2222, 3222], "titulo": [
                    "aaa", "bbb", "ccc"], "aptitud": [100, 0, 32]}))
    stats.saveStats(DataFrame({"ID": [1, 2, 3], "titulo": [
                    "a", "b", "c"], "aptitud": [1, 2, 3]}))
    stats.saveStats(DataFrame({"ID": [122, 2222, 3222], "titulo": [
                    "aaa", "bbb", "ccc"], "aptitud": [100, 0, 32]}))

    stats.showPlot()
