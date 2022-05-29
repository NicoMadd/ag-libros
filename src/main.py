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


algoritmoGenetico: AG = AG(probabilidad_mutacion=0.01,
                           tamanio_subgrupo=50, tamanio_minimo_poblacion=500)
algoritmoGenetico.setCriterioPoblacionInicial(AlAzar(500))
algoritmoGenetico.setCriterioSeleccion(
    Ranking(fraccionamiento=0.5))
algoritmoGenetico.setCriterioDeParo(CantidadDeVueltas(20))

# TODO
'''
1. Cambiar funcion de aptitud dependiendo eleccion de usuario
2. Para la mutacion, pre-ordenar la tabla segun criterios elegidos para eficientizar la busqueda
3. Cruzamiento de eleccion por individuo distancia media de ambos individuos padres

'''

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
        stats.saveStats(poblacion)
        # stats.showStatsPoblacion(poblacion)
        if(algoritmoGenetico.criterioDeParo(poblacion)):
            break

    stats.showStats()
    stats.showPlot()
    # poblacion.sort_values(
    #     by=['aptitud'], ascending=False, inplace=True)
    # print(poblacion[["ID", "titulo", "aptitud"]].head())
    # print(poblacion[["ID", "titulo", "aptitud"]].tail())
