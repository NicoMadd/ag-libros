###### Algoritmo Genético ######
###### Seleccion de libros acorde a gustos #########

import numpy as np
import pandas as pd
from pandas import DataFrame
from dataset import getDataset
from ag import getPoblacionInicial, criterioDeParo, cruzamiento, mutacion, seleccion

if __name__ == "__main__":
    poblacion: DataFrame = getPoblacionInicial(getDataset())

    while True:
        poblacion = seleccion(poblacion)
        poblacion = cruzamiento(poblacion)
        poblacion = mutacion(poblacion)
        if(criterioDeParo(poblacion)):
            break
    print(poblacion)
