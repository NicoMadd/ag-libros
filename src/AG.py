# Este archivo contiene las principales funciones del Algoritmo Genetico
# Estas son las funciones de Seleccion, Cruzamiento, Mutacion y Evaluacion
# de los individuos, en este caso distintos libros

import numpy as np
import pandas as pd
from pandas import DataFrame
from Criterios.Seleccion.CriterioSeleccion import CriterioSeleccion, Ranking
from Criterios.Cruzamiento.CriterioCruzamiento import CriterioCruzamiento, CruzaSimple
from Criterios.Mutacion.CriterioMutacion import CriterioMutacion, MutaSimple, MutaOrdenada
from Criterios.Paro.CriterioDeParo import CriterioDeParo
from Criterios.PoblacionInicial.CriterioPoblacionInicial import AlAzar, CriterioPoblacionInicial


class AG:

    def __init__(self, criterio_seleccion: CriterioSeleccion = Ranking(),
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

    def getPoblacionInicial(self, dataset: DataFrame) -> DataFrame:
        self.dataset = dataset
        return self.criterio_poblacion_inicial.samplear(dataset)

    def criterioDeParo(self, poblacion: DataFrame) -> bool:
        return self.criterio_de_paro.parar(poblacion)

    def seleccion(self, poblacion: DataFrame) -> DataFrame:
        # Separa la poblacion en subgrupos
        subgrupos = poblacion.groupby(
            np.arange(len(poblacion)) // self.tamanio_subgrupo)

        print("Subgrupos: ", len(subgrupos))
        print("Poblacion inicial: ", poblacion.shape[0])

        df = DataFrame()
        for _, subgrupo in subgrupos:
            subgrupo = self.criterio_seleccion.seleccionar(subgrupo)
            df = pd.concat([df, subgrupo])

        print("Poblacion Final: ", df.shape[0])

        return df

    def cruzamiento(self, poblacion: DataFrame) -> DataFrame:
        tamanio_poblacion_actual = poblacion.shape[0]
        print("Poblacion inicial Cruza: ", tamanio_poblacion_actual)

        # for iterando en la poblacion agarrando dos individuos y cruzandolos.
        # Si es impar el ultimo no se cruza.
        df = poblacion.copy()
        while tamanio_poblacion_actual < self.tamanio_minimo_poblacion:
            for i in range(poblacion.shape[0]):

                if i % 2 == 0:
                    if i == df.shape[0] - 1:
                        break
                    individuo1 = df.iloc[i]
                    individuo2 = df.iloc[i+1]
                    hijo = self.criterio_cruzamiento.cruzar(
                        individuo1, individuo2)
                    poblacion = pd.concat([poblacion, hijo])
                    tamanio_poblacion_actual += 1
        print("Poblacion Final Cruza: ", poblacion.loc[poblacion.ID.isnull()])
        #         tamanio_poblacion_actual = poblacion.shape[0]
        # Cruzar hasta llegar a la tamanio de poblacion minima
        # Criterio de padres Random
        # while tamanio_poblacion_actual < self.tamanio_minimo_poblacion:
        #     # Busca a dos individuos para cruzar
        #     individuo_1 = poblacion.sample(1)
        #     individuo_2 = poblacion.sample(1)
        #     # Cruzamiento. Se pasan los dos padres y se obtiene un hijo mezcla de ambos. De ser o no un libro existente se agrega igual, de no serlo, se descartara en la etapa de seleccion.
        #     hijo = self.criterio_cruzamiento.cruzar(
        #         individuo_1, individuo_2)
        #     poblacion = pd.concat([poblacion, hijo])
        #     tamanio_poblacion_actual += 1
        return poblacion

    def mutacion(self, poblacion: DataFrame) -> DataFrame:
        mutaciones = 0

        print("Poblacion inicial: ", poblacion.shape[0])
        print(poblacion.columns)
        # Obtiene indices los libros de la poblacion que van a mutar
        for i in range(poblacion.shape[0]):
            if np.random.random() < self.probabilidad_mutacion:
                individuo = poblacion.iloc[i]
                individuo = self.criterio_mutacion.mutar(
                    individuo, self.dataset)
                print(poblacion.columns)
                poblacion.iloc[i] = individuo
                mutaciones += 1
        print("Mutaciones: ", mutaciones)
        return poblacion

    def setCriterioSeleccion(self, criterio_seleccion: CriterioSeleccion):
        self.criterio_seleccion = criterio_seleccion

    def setCriterioPoblacionInicial(self, criterio_poblacion_inicial: CriterioPoblacionInicial):
        self.criterio_poblacion_inicial = criterio_poblacion_inicial

    def setCriterioDeParo(self, criterio_de_paro: CriterioDeParo):
        self.criterio_de_paro = criterio_de_paro
