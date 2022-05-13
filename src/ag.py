# Este archivo contiene las principales funciones del Algoritmo Genetico
# Estas son las funciones de Seleccion, Cruzamiento, Mutacion y Evaluacion
# de los individuos, en este caso distintos libros

import numpy as np
import pandas as pd
from pandas import DataFrame
from Criterios.Seleccion.CriterioSeleccion import CriterioSeleccion
from Criterios.Cruzamiento.CriterioCruzamiento import CriterioCruzamiento
from Criterios.Mutacion.CriterioMutacion import CriterioMutacion
from Criterios.Paro.CriterioDeParo import CriterioDeParo

# TODO Definir una seleccion inicial. La actual me parece bien, hay que ver si se adapta a la
# teoria.


def getPoblacionInicial(dataset: DataFrame, tamano_poblacion: int = 10) -> DataFrame:
    return dataset.sample(tamano_poblacion)


def criterioDeParo(poblacion: DataFrame, criterioDeParo: CriterioDeParo = None) -> bool:
    return True


def seleccion(poblacion: DataFrame, criterioSeleccion: CriterioSeleccion = None):
    return poblacion


def cruzamiento(poblacion: DataFrame, criterioCruzamiento: CriterioCruzamiento = None):
    return poblacion


def mutacion(poblacion: DataFrame, criterioMutacion: CriterioMutacion = None):
    return poblacion
