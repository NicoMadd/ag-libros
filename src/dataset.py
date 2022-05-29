# Este archivo prepara el dataset para el algoritmo genetico


import pandas as pd
from pandas import DataFrame
import numpy as np
import os
from dotenv import load_dotenv
from utils import read_csv
import random

load_dotenv()

DATASET_URL = os.getenv('DATASET_URL')
DATA_DIR = os.getenv("DATA_DIR")
DATA_FILENAME = os.getenv("DATA_FILENAME")
DATA_FILE_PATH = f'{DATA_DIR}/{DATA_FILENAME}'


def getDatasetFromUrl() -> DataFrame:
    df = pd.read_csv(DATASET_URL)
    df = formatDataset(df)
    df.sort_values(by=['titulo', 'autor', 'calificacion', 'language', 'generos', 'publicador',
       'likedPercent', 'genero', 'subgenero', 'aptitud', 'ID'], inplace=True, ignore_index=True)
    return df

# TODO Normalizar el dataset, obteniendo la informacion que mas nos sirva y clasificandolo
# segun el documento del genotipo

# if genero is NULL then return Nan else return genero
def formatGeneros(generos: list, posicion: int):
    return generos[posicion]


def formatDataset(df: DataFrame) -> DataFrame:

    df.drop(columns=['bookId'], inplace=True, axis=1)
    df.rename(inplace=True, columns={
              'title': 'titulo', 'author': 'autor', 'rating': 'calificacion', 'genres': 'generos', 'publisher': 'publicador', 'likedPercentage': 'porcentaje de aprobacion'})

    # ID as rowNumber
    df["ID"] = df.index
    df['generos_normalizados'] = df.generos.apply(normalizeGenre)
    df['genero'] = np.vectorize(formatGeneros)(df["generos_normalizados"], 0)
    df['subgenero'] = np.vectorize(formatGeneros)(df["generos_normalizados"], 1)
    df.drop(columns=['generos_normalizados'], inplace= True)
    df["aptitud"] = 0

    return df

def normalizeGenre(generosDF):
    generos_normalizados = [['Biopic', ['iography'], ['###@###']], ['Comedia', ['Humor', 'Comedy'], ['###@###']],
               ['Ciencia Ficcion', ['Science Fiction'], ['###@###']], ['Accion', ['Action'], ['###@###']],
               ['Western', ['West'], ['Western Africa']], ['Aventura', ['Adventure'], ['###@###']],
               ['Terror/Horror', ['Horror'], ['###@###']], ['Suspenso', ['Thriller', 'Suspense'], ['###@###']],
               ['Policial', ['Crime', 'Police'], ['###@###']], ['Misterio', ['Mystery'], ['###@###']],
               ['Fantasia', ['Fantas'], ['###@###']], ['Epic', ['Epic'], ['###@###']],
               ['Guerra', ['War'], ['Warming', 'Warcraft']], ['Romance', ['Romance', 'Love'], ['###@###']],
               ['Drama', ['Drama'], ['###@###']]]
    generos_encontrados = list()
    for normalizado in generos_normalizados:
        if any((any((buscar in genero) for buscar in normalizado[1]) & \
                (not any((evitar in genero) for evitar in normalizado[2]))) for genero in generosDF.split(',')):
            generos_encontrados.append(normalizado[0])
    if len(generos_encontrados) >= 2:
        return random.sample(generos_encontrados, 2)
    elif len(generos_encontrados) == 1:
        generos_encontrados.append('Ninguno')
        return generos_encontrados
    else:
        return ['Ninguno', 'Ninguno']


def getDataset() -> DataFrame:
    if os.path.exists(DATA_FILE_PATH):
        df = read_csv(DATA_FILE_PATH)
    else:
        df = getDatasetFromUrl()
        df.to_csv(DATA_FILE_PATH, index=False)
    return df


if __name__ == "__main__":
    poblacion: DataFrame = getDataset()
    # print(poblacion.head())
    filtered = poblacion
    print(filtered.head())
    print("size:", filtered.size)
