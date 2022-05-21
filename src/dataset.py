# Este archivo prepara el dataset para el algoritmo genetico


import json
import pandas as pd
from pandas import DataFrame
import numpy as np
import os
from dotenv import load_dotenv
from GoogleAPI import GoogleBooksAPI
from utils import read_csv

load_dotenv()

DATASET_URL = os.getenv('DATASET_URL')
DATA_DIR = os.getenv("DATA_DIR")
DATA_FILENAME = os.getenv("DATA_FILENAME")
DATA_FILE_PATH = f'{DATA_DIR}/{DATA_FILENAME}'


def getDatasetFromUrl() -> DataFrame:
    df = pd.read_csv(DATASET_URL)
    df = formatDataset(df)
    return df

# TODO Normalizar el dataset, obteniendo la informacion que mas nos sirva y clasificandolo
# segun el documento del genotipo


# if genero is NULL then return Nan else return genero
def formatGeneros(generos: str):
    return np.NaN if "NULL" in generos else generos


def formatDataset(df: DataFrame) -> DataFrame:

    df.drop(columns=['bookId'], inplace=True, axis=1)
    df.rename(inplace=True, columns={
              'title': 'titulo', 'author': 'autor', 'rating': 'calificacion', 'genres': 'generos', 'publisher': 'publicador', 'likedPercentage': 'porcentaje de aprobacion'})

    # ID as rowNumber
    df["ID"] = df.index
    df["generos"] = np.vectorize(formatGeneros)(df["generos"])
    df["aptitud"] = 0

    return df


def getDataset() -> DataFrame:
    if os.path.exists(DATA_FILE_PATH):
        df = read_csv(DATA_FILE_PATH)
    else:
        df = getDatasetFromUrl()
        df.to_csv(DATA_FILE_PATH, index=False)
    return df


if __name__ == "__main__":
    # df = getDatasetFromUrl()
    df = getDataset()
    # df.to_csv(DATA_FILE_PATH, index=False)
    print(df.head())
    print("size:", df.shape[0])

    one = df.iloc[0]
    api = GoogleBooksAPI()
    api.addTitulo(one['titulo']).addAutor(
        one['autor'])
    book = api.getBook()
    print(json.dumps(book, indent=4))
