###### Algoritmo Genético ######
###### Seleccion de libros acorde a gustos #########

import numpy as np
import pandas as pd
from pandas import DataFrame
from Criterios.Seleccion.CriterioSeleccion import Ranking
from dataset import getDataset
from AG import AG
from FuncionAptitud import FuncionAptitud

algoritmoGenetico: AG = AG()
algoritmoGenetico.setCriterioSeleccion(
    Ranking(subgrupo_minimo=2, fraccionamiento=0.5))

if __name__ == "__main__":
    poblacion: DataFrame = algoritmoGenetico.getPoblacionInicial(getDataset())
    while True:
        poblacion = algoritmoGenetico.seleccion(poblacion)
        poblacion = algoritmoGenetico.cruzamiento(poblacion)
        poblacion = algoritmoGenetico.mutacion(poblacion)
        if(algoritmoGenetico.criterioDeParo(poblacion)):
            break
    print(poblacion)
