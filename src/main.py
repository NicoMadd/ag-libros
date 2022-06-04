###### Algoritmo Genético ######
###### Seleccion de libros acorde a gustos #########

from Criterios.Cruzamiento.CriterioCruzamiento import CruzaModular, CruzaSimple
from Criterios.Mutacion.CriterioMutacion import MutaSimple
from Criterios.Paro.CriterioDeParo import AptitudMayorA, CantidadDeVueltas, TiempoTranscurrido
from Interfaz import Interfaz
from Stats import Stats
from utils import stats_poblacion
from FuncionAptitud import FuncionAptitud
from AG import AG
from dataset import getDataset
from Criterios.Seleccion.CriterioSeleccion import Ranking, Torneo
from Criterios.PoblacionInicial.CriterioPoblacionInicial import AlAzar
from pandas import DataFrame
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

tamanio_minimo_poblacion = 250
algoritmoGenetico: AG = AG(probabilidad_mutacion=0.5,
                           tamanio_subgrupo=25, tamanio_minimo_poblacion=tamanio_minimo_poblacion)
algoritmoGenetico.setCriterioPoblacionInicial(AlAzar(tamanio_minimo_poblacion))
# algoritmoGenetico.setCriterioSeleccion(
#     Ranking())
algoritmoGenetico.setCriterioSeleccion(Torneo())
algoritmoGenetico.setCriterioCruzamiento(CruzaModular())
algoritmoGenetico.setCriterioDeParo(CantidadDeVueltas(5))
algoritmoGenetico.setCriterioMutacion(MutaSimple())
# algoritmoGenetico.setCriterioDeParo(TiempoTranscurrido(2))
# algoritmoGenetico.setCriterioDeParo(AptitudMayorA(800))

stats = Stats()

# TODO
# 1. Completar precio, cantidad de paginas y fecha de publicacion en el dataset. ✔
# 2. Crear interfaz por consola para definir funcion aptitud. ✔
# 3. Implementar 2 criterios de seleccion (torneo y ranking). ✔
# 4. Implementar 2 criterios de cruzamiento. Mitad de tabla. ✔
# 5. Implementar 2 criterios de paro (cantidad de vueltas y tiempo transcurrido). ✔


if __name__ == "__main__":
    # Definir propiedades de la funcion aptitud
    funcionAptitud = Interfaz().getFuncionAptitud()
    algoritmoGenetico.setFuncionAptitud(funcionAptitud)
    stats.setFunctionAptitud(funcionAptitud)

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
    stats.log()
