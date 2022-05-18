# Funciones utils para el proyecto de la asignatura de Inteligencia Artificial
import pandas as pd
import numpy as np


def read_csv(file_name):
    df = pd.read_csv(file_name)
    return df


def stats_poblacion(poblacion: pd.DataFrame):
    print("size:", poblacion.shape[0])
    # print(poblacion.columns)
    print(poblacion[["ID", "titulo", "aptitud"]].head())
