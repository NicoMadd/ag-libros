# Este archivo prepara el dataset para el algoritmo genetico


import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from utils import read_csv

load_dotenv()

DATASET_URL = os.getenv('DATASET_URL')
DATA_DIR = os.getenv("DATA_DIR")
DATA_FILENAME = os.getenv("DATA_FILENAME")
DATA_FILE_PATH = f'{DATA_DIR}/{DATA_FILENAME}'


def getDatasetFromUrl() -> pd.DataFrame:
    df = pd.read_csv(DATASET_URL)
    df = formatDataset(df)
    return df


def formatDataset(df: pd.DataFrame) -> pd.DataFrame:
    return df


def getDataset() -> pd.DataFrame:
    if os.path.exists(DATA_FILE_PATH):
        df = read_csv(DATA_FILE_PATH)
        df = formatDataset(df)
    else:
        df = getDatasetFromUrl()
        df.to_csv(DATA_FILE_PATH, index=False)
    return df
