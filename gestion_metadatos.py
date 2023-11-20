# Importar dependencias
# La librería JSON permite abrir y guardar archivos en formato JSON
import json
# Sklearn cuenta con una herramienta para dividir un dataset
# en un subconjunto de entrenamiento y un subconjunto de evaluación
# Ambos, son importantes para el trabajo con aprendizaje automatico
from sklearn.model_selection import train_test_split
# os es una librería propia de Python que permite precesar archivos
import os
import subprocess
import zipfile
# La librería TQDM permite integrar barras de progreso en estructuras repetitivas for
from tqdm.auto import tqdm
# La librería shutil tiene implementaciones optimizadas para trabajar con archivos
import shutil
# La librería random permite crear números aleatorios
import random
# La librería OpenCV contiene funciones y algoritmos para procesar imágenes y video
import cv2
import pandas as pd
from matplotlib import pyplot as plt
import kaggle

xlsx_file_path = './dataset/covid_19_radiography/COVID-19_Radiography_Dataset/COVID.metadata.xlsx'

# funciones add_metadata, update_metadata, y delete_metadata.
def update_metadata(df, image_id, new_metadata):

    # Comprobar si el  id de la imagen existe en el DataFrame
    if image_id in df['FILE NAME'].values:
        index = df[df['FILE NAME'] == image_id].index
        for key, value in new_metadata.items():
            df.loc[index, key] = value
        print("Metadatos actualizados.")
    else:
        print("No se encontró la imagen.")
    return df

def delete_metadata(df, image_id):

  # Comprobar si la imagen existe en el DataFrame
    if image_id in df['FILE NAME'].values:
        df.drop(df[df['FILE NAME'] == image_id].index, inplace=True)
        print("Metadatos eliminados para la imagen:", image_id)
    else:
        print("Imagen no encontrada en los metadatos.")
  # Adicionar nuevo registro
def add_metadata(df, new_metadata):
    #Agrega nuevos metadatos de imagen al DataFrame.
    if new_metadata['FILE NAME'] not in df['FILE NAME'].values:
        # Convertimos el diccionario a DataFrame para poder usar pd.concat
        new_metadata_df = pd.DataFrame([new_metadata])
        # Usamos pd.concat para añadir la nueva fila
        df = pd.concat([df, new_metadata_df], ignore_index=True)
        print("Nuevos metadatos agregados para la imagen:", new_metadata['FILE NAME'])
        # Guardamos el DataFrame actualizado en el archivo CSV
        df.to_excel('./dataset/covid_19_radiography/COVID-19_Radiography_Dataset/COVID.metadata.xlsx', index=False)
        print("Archivo CSV actualizado.")
    else:
        print("Una imagen con ese nombre de archivo ya existe.")
    return df
# Función para recargar el DataFrame desde el archivo .csv
def reload_dataframe(xlsx_file_path):
    return pd.read_excel(xlsx_file_path)
def capturar_datos_imagen():
    file_name = input("Ingrese el nombre del archivo de la imagen: ")
    format = input("Ingrese el formato de la imagen: ")
    size = input("Ingrese el tamaño de la imagen: ")
    url = input("Ingrese la URL de la imagen: ")
    return {'FILE NAME': file_name, 'FORMAT': format, 'SIZE': size, 'URL': url}

def mostrar_menu():
    print("\nMenú Principal")
    print("1. Agregar Nueva Imagen y Metadatos")
    print("2. Actualizar Metadatos de Imagen")
    print("3. Eliminar Imagen y Metadatos")
    print("4. Mostrar Metadatos de Imagen")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Definición de la función para imprimir metadatos.
def print_metadata(df, image_id):
    if image_id in df['FILE NAME'].values:
        metadata = df.loc[df['FILE NAME'] == image_id]
        print(metadata)
    else:
        print("Imagen no encontrada en los metadatos.")