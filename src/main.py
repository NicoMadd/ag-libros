###### Algoritmo Genético ######
###### Seleccion de libros acorde a gustos #########

from Criterios.Paro.CriterioDeParo import CantidadDeVueltas
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


algoritmoGenetico: AG = AG(probabilidad_mutacion=0.1,
                           tamanio_subgrupo=2, tamanio_minimo_poblacion=100)
algoritmoGenetico.setCriterioPoblacionInicial(AlAzar())
algoritmoGenetico.setCriterioSeleccion(
    Ranking(fraccionamiento=0.5))
algoritmoGenetico.setCriterioDeParo(CantidadDeVueltas(50))


if __name__ == "__main__":
    poblacion: DataFrame = algoritmoGenetico.getPoblacionInicial(getDataset())
    while True:
        poblacion = algoritmoGenetico.seleccion(poblacion)
        poblacion = algoritmoGenetico.cruzamiento(poblacion)
        poblacion = algoritmoGenetico.mutacion(poblacion)
        if(algoritmoGenetico.criterioDeParo(poblacion)):
            break

    poblacion.sort_values(
        by=['aptitud'], ascending=False, inplace=True)
    print(poblacion[["ID", "titulo", "aptitud"]].head())
    # print(poblacion[["ID", "titulo", "aptitud"]].tail())
