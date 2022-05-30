###### Algoritmo Genético ######
###### Seleccion de libros acorde a gustos #########

from Criterios.Paro.CriterioDeParo import CantidadDeVueltas
from Stats import Stats
from utils import stats_poblacion
from FuncionAptitud import FuncionAptitud
from AG import AG
from dataset import getDataset
from Criterios.Seleccion.CriterioSeleccion import Ranking
from Criterios.PoblacionInicial.CriterioPoblacionInicial import AlAzar
from pandas import DataFrame
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


algoritmoGenetico: AG = AG(probabilidad_mutacion=0.02,
                           tamanio_subgrupo=50, tamanio_minimo_poblacion=200)
algoritmoGenetico.setCriterioPoblacionInicial(AlAzar(200))
algoritmoGenetico.setCriterioSeleccion(
    Ranking(fraccionamiento=0.5))
algoritmoGenetico.setCriterioDeParo(CantidadDeVueltas(2))

stats = Stats()
if __name__ == "__main__":
    poblacion: DataFrame = algoritmoGenetico.getPoblacionInicial(getDataset())
    vuelta = 0
    while True:
        vuelta += 1
        print("Vuelta: ", vuelta)
        poblacion = algoritmoGenetico.seleccion(poblacion)
        poblacion = algoritmoGenetico.cruzamiento(poblacion)
        poblacion = algoritmoGenetico.mutacion(poblacion)
        mejor = poblacion.head(
            1)[["ID", "titulo", "aptitud"]].iloc[0].to_dict()
        peor = poblacion.tail(1)[["ID", "titulo", "aptitud"]].iloc[0].to_dict()
        print("Mejor:", mejor)
        print("Peor:", peor)
        stats.saveStats(poblacion)
        # stats.showStatsPoblacion(poblacion)
        if(algoritmoGenetico.criterioDeParo(poblacion)):
            break

    # stats.showStats()
    # stats.showPlot()
    # poblacion.sort_values(
    #     by=['aptitud'], ascending=False, inplace=True)
    # print(poblacion[["ID", "titulo", "aptitud"]].head())
    # print(poblacion[["ID", "titulo", "aptitud"]].tail())
