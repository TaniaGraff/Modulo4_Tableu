
#Importo librerías
import pandas as pd
import numpy as np


import os
import sys
sys.path.append("../")

import warnings
warnings.filterwarnings("ignore")

"""Creamos función para abrir los excel y convertir en DF.
"""
def leer_csv(ruta_csv):
    df= pd.read_excel(ruta_csv)
    pd.set_option('display.max_columns', None)
    return df

"""Creamos función para ver la info de los excel.
"""
def info_df(df):
    return df.info()

"""Creamos función para buscar el porcentaje de nulos numéricos.
"""
def nulos_numericos(df):
    columnas_con_nulos = df.columns[df.isnull().any()].tolist()
    print("Porcentaje de nulos numéricos por columna:")
    print(df[columnas_con_nulos].isnull().sum() / df.shape[0] * 100)    
    return columnas_con_nulos

"""Creamos función para ver cómo se distribuyen los valores únicos en esas columnas.
"""
def distribucion_valores (df, columnas):
    for columna in columnas:
        print(f"La distribución de las categorías para la columna {columna.upper()}")
        print(df[columna].value_counts() / df.shape[0])


"""Creamos función para calcular la media y la mediana de las columnas con nulos numéricos.
"""
def media_mediana(df, *columnas):
    resultados = {}
    
    for columna in columnas:
            media = df[columna].mean()
            mediana = df[columna].median()
            resultados[columna] = {'media': media, 'mediana': mediana}
            print(f'La MEDIA de la columna {columna.upper()} es: {media}')
            print(f'La MEDIANA de la columna {columna.upper()} es: {mediana}')
    
    return resultados

"""Creamos función para imputar la mediana a las columnas.
"""
def imputar_mediana(df, columnas):
    for columna in columnas:
            mediana = df[columna].median()
            df[columna].fillna(mediana, inplace=True)
            print(f"Imputando mediana en la columna '{columna}': {mediana}")

    return df

"""Creo función para igualar nombres columnas con un guión bajo.
"""
def igualar_columnas(df):
    df.columns = df.columns.str.replace(' ', '_').str.replace(':', '').str.title()
    return df


"""Creamos función para guardar el DF resultante en la carpeta output_data.
"""
def guardar_df(df, nombre_archivo):
    ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'output_data', nombre_archivo + '.csv')
    df.to_csv(ruta_archivo, index=False)
    print(f"El DataFrame se ha guardado en {ruta_archivo}")
