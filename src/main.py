###### Algoritmo Genético ######
###### Seleccion de libros acorde a gustos #########

from Criterios.Cruzamiento.CriterioCruzamiento import CruzaSimple
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


algoritmoGenetico: AG = AG(probabilidad_mutacion=0.06,
                           tamanio_subgrupo=25, tamanio_minimo_poblacion=150)
algoritmoGenetico.setCriterioPoblacionInicial(AlAzar(150))
algoritmoGenetico.setCriterioSeleccion(
    Ranking(fraccionamiento=0.5))
algoritmoGenetico.setCriterioDeParo(CantidadDeVueltas(100))

stats = Stats()

# TODO
# 1. Completar precio, cantidad de paginas en el dataset.
# 2. Crear interfaz por consola para definir funcion aptitud.
# 3. Implementar 2 criterios de seleccion
# 4. Implementar 2 criterios de cruzamiento. Mitad de tabla
# 5. Implementar 2 criterios de paro


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

    # stats.showStats()
    stats.showPlot()
