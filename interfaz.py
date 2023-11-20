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
from gestion_metadatos import *

def main():
    xlsx_file_path = './dataset/covid_19_radiography/COVID-19_Radiography_Dataset/COVID.metadata.xlsx'
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            # Código para agregar nueva imagen
            print("Agregar nueva imagen y metadatos:")
            nuevos_metadatos = capturar_datos_imagen()
            # Aquí llamarías a la función para agregar los metadatos
            add_metadata(df, nuevos_metadatos)
            df = reload_dataframe(xlsx_file_path)
        elif opcion == '2':
            print("Actualizar metadatos de imagen:")
            file_name = input("Ingrese el nombre del archivo de la imagen a actualizar: ")
            nuevos_metadatos = capturar_datos_imagen()
            # Convertimos los nuevos metadatos a un formato adecuado para la función de actualización
            metadatos_formateados = {k: nuevos_metadatos[k] for k in ['FORMAT', 'SIZE', 'URL']}
            # Llamamos a la función de actualización
            update_metadata(df, file_name, metadatos_formateados)
            df.to_excel(xlsx_file_path, index=False)

        elif opcion == '3':
            # Código para eliminar imagen
            print("Eliminar imagen y metadatos:")
            file_name = input("Ingrese el nombre del archivo de la imagen a eliminar: ")
            delete_metadata(df, file_name)
            df.to_excel(xlsx_file_path, index=False)
        elif opcion == '4':
            # Mostrar metadatos de una imagen
            df = reload_dataframe(xlsx_file_path)
            file_name = input("Ingrese el nombre del archivo de la imagen a mostrar: ")
            print_metadata(df, file_name)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")
