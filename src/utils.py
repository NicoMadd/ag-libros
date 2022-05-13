# Funciones utils para el proyecto de la asignatura de Inteligencia Artificial
import pandas as pd
import numpy as np


def read_csv(file_name):
    df = pd.read_csv(file_name)
    return df
