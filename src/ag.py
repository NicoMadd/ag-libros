# Este archivo contiene las principales funciones del Algoritmo Genetico
# Estas son las funciones de Seleccion, Cruzamiento, Mutacion y Evaluacion
# de los individuos, en este caso distintos libros

import numpy as np
import pandas as pd
from pandas import DataFrame
from Criterios.Seleccion.CriterioSeleccion import CriterioSeleccion, Ranking
from Criterios.Cruzamiento.CriterioCruzamiento import CriterioCruzamiento
from Criterios.Mutacion.CriterioMutacion import CriterioMutacion
from Criterios.Paro.CriterioDeParo import CriterioDeParo
from Criterios.PoblacionInicial.CriterioPoblacionInicial import AlAzar, CriterioPoblacionInicial

# TODO Definir una seleccion inicial. La actual me parece bien, hay que ver si se adapta a la
# teoria.


class AG:

    def __init__(self, criterio_seleccion: CriterioSeleccion = Ranking(), criterio_cruzamiento: CriterioCruzamiento = None, criterio_mutacion: CriterioMutacion = None, criterio_de_paro: CriterioDeParo = None, criterio_poblacion_inicial: CriterioPoblacionInicial = AlAzar()):
        self.criterio_seleccion = criterio_seleccion
        self.criterio_cruzamiento = criterio_cruzamiento
        self.criterio_mutacion = criterio_mutacion
        self.criterio_de_paro = criterio_de_paro
        self.criterio_poblacion_inicial = criterio_poblacion_inicial

    def getPoblacionInicial(self, dataset: DataFrame) -> DataFrame:
        return self.criterio_poblacion_inicial.samplear(dataset)

    def criterioDeParo(self, poblacion: DataFrame, criterioDeParo: CriterioDeParo = None) -> bool:
        return True

    def seleccion(self, poblacion: DataFrame):
        return self.criterio_seleccion.seleccionar(poblacion)

    def cruzamiento(self, poblacion: DataFrame, criterioCruzamiento: CriterioCruzamiento = None):
        return poblacion

    def mutacion(self, poblacion: DataFrame, criterioMutacion: CriterioMutacion = None):
        return poblacion

    def setCriterioSeleccion(self, criterio_seleccion: CriterioSeleccion):
        self.criterio_seleccion = criterio_seleccion

    def setCriterioPoblancionInicial(self, criterio_poblacion_inicial: CriterioPoblacionInicial):
        self.criterio_poblacion_inicial = criterio_poblacion_inicial
