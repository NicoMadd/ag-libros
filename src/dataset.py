# Este archivo prepara el dataset para el algoritmo genetico


from datetime import date
import timeit
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
import os
from dotenv import load_dotenv
from GoogleAPI import GoogleBooksAPI
from utils import read_csv
import random

load_dotenv()

DATASET_URL = os.getenv('DATASET_URL')
DATA_DIR = os.getenv("DATA_DIR")
DATA_FILENAME = os.getenv("DATA_FILENAME")
DATA_FILE_PATH = f'{DATA_DIR}/{DATA_FILENAME}'


# Completar si falta alguno
generos = ['Biopic', 'Comedia', 'Ciencia Ficcion', 'Accion',
           'Western', 'Policial', 'Misterio', 'Drama', 'Romance', 'Terror']
precios = ['0-1000', '1000-2000', '2000-3000', 'mas de 3000']
fechas = ['Antes del 2000',
          f'Antes del {date.today().year-10} ', 'Ultima Decada', 'Ultimo Año']
rangos_de_paginas = ['0-100', '100-300', '300-500', 'mas de 500']


def getDatasetFromUrl() -> DataFrame:
    df = pd.read_csv(DATASET_URL)
    df = formatDataset(df)
    df.sort_values(by=['language', 'titulo', 'genero', 'subgenero', 'autor', 'calificacion', 'publicador',
                       'likedPercent', 'ID'], inplace=True, ignore_index=True)
    return df

# TODO Normalizar el dataset, obteniendo la informacion que mas nos sirva y clasificandolo
# segun el documento del genotipo

# if genero is NULL then return Nan else return genero


def formatGeneros(generos: list, posicion: int):
    return generos[posicion]


def formatDataset(df: DataFrame) -> DataFrame:

    today = date.today()

    df.drop(columns=['bookId'], inplace=True, axis=1)
    df.rename(inplace=True, columns={
              'title': 'titulo', 'author': 'autor', 'rating': 'calificacion', 'genres': 'generos', 'publisher': 'publicador', 'likedPercentage': 'porcentaje de aprobacion'})

    # ID as rowNumber
    df["ID"] = df.index
    df['generos_normalizados'] = df.generos.apply(normalizeGenre)
    df['genero'] = np.vectorize(formatGeneros)(df["generos_normalizados"], 0)
    df['subgenero'] = np.vectorize(formatGeneros)(
        df["generos_normalizados"], 1)
    df.drop(columns=['generos_normalizados'], inplace=True)

    # Setear random a partir de las sigueintes opciones [0-1000, 1000 - 2000, 2000 - 3000, 3000 - mas de 3000]

    df["precio"] = np.random.normal(0, 9000, len(df))
    df["precio"] = np.select([df["precio"] < 1000, df["precio"] < 2000,
                             df["precio"] < 3000, df["precio"] >= 3000], ["0-1000", "1000-2000", "2000-3000", "mas de 3000"])

    df["fechaPublicacion"] = pd.Series(
        np.random.randint(-2000, 2022, size=len(df)))
    df["fechaPublicacion"] = np.select([df["fechaPublicacion"] < 0, df["fechaPublicacion"] < today.year-10,
                                        df["fechaPublicacion"] < today.year-1, df["fechaPublicacion"] < today.year],
                                       ["Antes del 2000", f"Antes del {today.year-10} ", "Ultima Decada", "Ultimo Año"])
    df["numero_paginas"] = pd.Series(np.random.randint(0, 1000, size=len(df)))
    df["numero_paginas"] = np.select([df["numero_paginas"] < 100, df["numero_paginas"]
                                     < 300, df["numero_paginas"] < 500], ["0-100", "100-300", "300-500"], default="mas de 500")

    df["aptitud"] = 0

    return df


def normalizeGenre(generosDF):
    generos_normalizados = [['Biopic', ['iography'], ['###@###']], ['Comedia', ['Humor', 'Comedy'], ['###@###']],
                            ['Ciencia Ficcion', ['Science Fiction'], [
                                '###@###']], ['Accion', ['Action'], ['###@###']],
                            ['Western', ['West'], ['Western Africa']], [
        'Aventura', ['Adventure'], ['###@###']],
        ['Terror/Horror', ['Horror'], ['###@###']], ['Suspenso',
                                                     ['Thriller', 'Suspense'], ['###@###']],
        ['Policial', ['Crime', 'Police'], ['###@###']
         ], ['Misterio', ['Mystery'], ['###@###']],
        ['Fantasia', ['Fantas'], ['###@###']
         ], ['Epic', ['Epic'], ['###@###']],
        ['Guerra', ['War'], ['Warming', 'Warcraft']], [
        'Romance', ['Romance', 'Love'], ['###@###']],
        ['Drama', ['Drama'], ['###@###']]]
    generos_encontrados = list()
    for normalizado in generos_normalizados:
        if any((any((buscar in genero) for buscar in normalizado[1]) &
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
    # df = getDatasetFromUrl()
    dataset = getDataset()
    # df.to_csv(DATA_FILE_PATH, index=False)
    # print(dataset.head())
    # print("size:", dataset.shape[0])

    print(dataset.head())
