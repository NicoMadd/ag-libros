# Este archivo contiene las principales funciones del Algoritmo Genetico
# Estas son las funciones de Seleccion, Cruzamiento, Mutacion y Evaluacion
# de los individuos, en este caso distintos libros

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from Criterios.Seleccion.CriterioSeleccion import CriterioSeleccion, Ranking
from Criterios.Cruzamiento.CriterioCruzamiento import CriterioCruzamiento, CruzaSimple
from Criterios.Mutacion.CriterioMutacion import CriterioMutacion, MutaSimple, MutaOrdenada
from Criterios.Paro.CriterioDeParo import CriterioDeParo
from Criterios.PoblacionInicial.CriterioPoblacionInicial import AlAzar, CriterioPoblacionInicial
from FuncionAptitud import FuncionAptitud


class AG:

    def __init__(self,
                 criterio_seleccion: CriterioSeleccion = Ranking(),
                 criterio_cruzamiento: CriterioCruzamiento = CruzaSimple(),
                 criterio_mutacion: CriterioMutacion = MutaOrdenada(),
                 criterio_de_paro: CriterioDeParo = None,
                 criterio_poblacion_inicial: CriterioPoblacionInicial = AlAzar(),
                 tamanio_subgrupo: int = 2,
                 tamanio_minimo_poblacion: int = 10,
                 probabilidad_mutacion: float = 0.1):
        self.criterio_seleccion = criterio_seleccion
        self.criterio_cruzamiento = criterio_cruzamiento
        self.criterio_mutacion = criterio_mutacion
        self.criterio_de_paro = criterio_de_paro
        self.criterio_poblacion_inicial = criterio_poblacion_inicial
        self.tamanio_subgrupo = tamanio_subgrupo
        self.tamanio_minimo_poblacion = tamanio_minimo_poblacion
        self.probabilidad_mutacion = probabilidad_mutacion
        self.dataset = None

    def setFuncionAptitud(self, funcion_aptitud: FuncionAptitud):
        self.funcion_aptitud = funcion_aptitud

    def getPoblacionInicial(self, dataset: DataFrame) -> DataFrame:
        self.dataset = dataset
        self.criterio_de_paro.iniciar()
        return self.criterio_poblacion_inicial.samplear(dataset)

    def criterioDeParo(self, poblacion: DataFrame) -> bool:
        return self.criterio_de_paro.parar(poblacion)

    def seleccion(self, poblacion: DataFrame) -> DataFrame:
        # Separa la poblacion en subgrupos
        subgrupos = poblacion.groupby(
            np.arange(len(poblacion)) // self.tamanio_subgrupo)

        print("Subgrupos: ", len(subgrupos))
        print("Poblacion Inicial Seleccion: ", poblacion.shape[0])

        df = DataFrame()
        for _, subgrupo in subgrupos:
            subgrupo["aptitud"] = self.funcion_aptitud.evaluar(subgrupo)
            subgrupo = self.criterio_seleccion.seleccionar(subgrupo)
            df = pd.concat([df, subgrupo])

        print("Poblacion Final Seleccion: ", df.shape[0])

        return df

    def cruzamiento(self, poblacion: DataFrame) -> DataFrame:
        # Separa la poblacion en subgrupos de dos.
        # Aplicar la cruza por cada grupo, obteniendo un hijo.
        # Concatenar los hijos en una nueva poblacion y devolverla.

        tamanio_poblacion = poblacion.shape[0]
        print("Poblacion Inicial Cruzamiento: ", tamanio_poblacion)
        df = DataFrame(poblacion, columns=poblacion.columns)
        while tamanio_poblacion < self.tamanio_minimo_poblacion:
            subgrupos = poblacion.sample(frac=1).groupby(
                np.arange(len(poblacion)) // 2)
            for _, subgrupo in subgrupos:
                if subgrupo.shape[0] == 1:
                    break
                hijo = self.criterio_cruzamiento.cruzar(
                    subgrupo.iloc[0], subgrupo.iloc[1], self.dataset)
                hijo = hijo.to_frame().T
                hijo['aptitud'] = self.funcion_aptitud.evaluar(hijo)
                df = pd.concat([df, hijo])
                tamanio_poblacion += 1

        print("Poblacion Final Cruzamiento: ", tamanio_poblacion)
        return df

    def mutacion(self, poblacion: DataFrame) -> DataFrame:
        mutaciones = 0

        print("Poblacion Inicial Mutacion: ", poblacion.shape[0])

        # Obtiene indices los libros de la poblacion que van a mutar
        for i in range(poblacion.shape[0]):
            if np.random.random() < self.probabilidad_mutacion:
                individuo = poblacion.iloc[i]
                individuoMutado: Series = self.criterio_mutacion.mutar(
                    individuo, self.dataset)
                poblacion.iloc[i] = individuoMutado
                mutaciones += 1
        print("Mutaciones: ", mutaciones)
        print("Poblacion Final Mutacion: ", poblacion.shape[0])
        return poblacion

    def setCriterioSeleccion(self, criterio_seleccion: CriterioSeleccion):
        self.criterio_seleccion = criterio_seleccion

    def setCriterioPoblacionInicial(self, criterio_poblacion_inicial: CriterioPoblacionInicial):
        self.criterio_poblacion_inicial = criterio_poblacion_inicial

    def setCriterioDeParo(self, criterio_de_paro: CriterioDeParo):
        self.criterio_de_paro = criterio_de_paro

    def setCriterioCruzamiento(self, criterio_cruzamiento: CriterioCruzamiento):
        self.criterio_cruzamiento = criterio_cruzamiento

    def setCriterioMutacion(self, criterio_mutacion: CriterioMutacion):
        self.criterio_mutacion = criterio_mutacion
