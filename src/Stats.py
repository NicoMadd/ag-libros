from datetime import datetime
import json
import os
from pickle import NONE
from dotenv import load_dotenv
from pandas import DataFrame, Series
import pandas
from FuncionAptitud import FuncionAptitud

from utils import stats_poblacion
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

load_dotenv()


class Stats:
    def __init__(self, aptitud_minima: float = 0):
        self.corridas = []
        self.mejor = None
        self.peor = None
        self.funcionAptitud = None
        self.aptitud_minima = aptitud_minima
        self.aptos = None
        # date with time
        self.file_name = f"stats_{datetime.today().strftime('%Y-%m-%d.%H_%M_%S')}.json"
        self.file_dir = os.getenv("STATS_DIR")
        self.file_path = os.path.join(self.file_dir, self.file_name)

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

        promedio = {"aptitud": promedio}
        lowerQuartile = {"aptitud": lowerQuartile}
        upperQuartile = {"aptitud": upperQuartile}

        # Guardar al mejor y al peor
        self.mejor = self.mejor if self.mejor is not None and self.mejor[
            "aptitud"] >= mejor["aptitud"] else mejor
        self.peor = self.peor if self.peor is not None and self.peor[
            "aptitud"] <= peor["aptitud"] else peor

        # Guarda la corrida
        corrida = {"mejor": mejor, "peor": peor, "promedio": promedio,
                   "lowerQuartile": lowerQuartile, "upperQuartile": upperQuartile, "varianza": varianza}
        self.corridas.append(corrida)

        # Guarda los individuos aptos. Estos son los que tengan mas aptitud que la minima establecida y ademas no hayan ID repetidos
        aptos = poblacion[(poblacion.aptitud >= self.aptitud_minima) & (
            poblacion.ID.duplicated(keep=False))]
        aptos = aptos[["ID", "titulo", "aptitud", "genero", "subgenero",
                       "precio", "idioma", "numero_paginas", "fechaPublicacion"]]

        # Agrega los individuos aptos
        self.aptos = pandas.concat(
            [self.aptos, aptos]) if self.aptos is not None else aptos

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

    # save stats to json
    def log(self):
        # Genera un archivo json con los datos de las corridas, los datos de la funcion aptitud, y los aptos

        # join all in one json
        json_data = {"corridas": self.corridas,
                     "aptos": self.aptos.T.to_dict(),
                     "funcionAptitud": self.funcionAptitud.to_dict()}

        # create dir if it doesnt exists
        if not os.path.exists(self.file_dir):
            os.mkdir(self.file_dir)
        # save json to file in current directory
        with open(self.file_path, 'w') as outfile:
            json.dump(json_data, outfile)


if __name__ == "__main__":

    # recorre archivos de carpeta stats
    for file in os.listdir("../stats"):
        content = json.load(open("../stats/" + file))
        corridas = content["corridas"]

        dfMain = pandas.DataFrame()
        for index, corrida in enumerate(corridas):
            mejor = corrida["mejor"]
            peor = corrida["peor"]
            # add mejor and peor to df
            df = pandas.DataFrame([mejor, peor], columns=["ID", "titulo", "aptitud", "genero",
                                  "subgenero", "precio", "idioma", "numero_paginas", "fechaPublicacion"])
            df.set_index("ID", inplace=True)
            df["corrida"] = index
            dfMain = pandas.concat([dfMain, df])

        dfMain.to_csv("../stats/" + file.replace(".json", ".csv"))
