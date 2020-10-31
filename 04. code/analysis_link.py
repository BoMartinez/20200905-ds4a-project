#**********************************************************************************************
# @Nombre: Agrupamiento de demanda por dia, ruta, hora y link
# @Autor: Grupo 21
# @Fecha: 2020/10/28 20:40:47
# @Ayuda: 
#**********************************************************************************************

#Importar librerias ---------------------------------------------------------------------------
import datetime as dt                 # Manipulacion de fechas
import pandas as pd                   # Manipulacion de datos
import numpy as np                    # Manipulacion numerica
import keyring                        # Manejo de contraseñas
import os, glob                       # Manejo del sistema
from google.colab import data_table

# Proceso de transformacion -------------------------------------------------------------------
#1. Filtro por la columna FAR == 'False'
#2. Agrupamiento de los datos:
#    - Datekey.
#    - CodigoRuta.
#    - Hour.
#    - Link.
#3. Sumarizacion:
#    - Sumatoria PaxUp
#    - Sumatoria PaxDw

# Desarrollo ----------------------------------------------------------------------------------
path = "/content/drive/My Drive/ds4a-project/outputs/"
path_to = "/content/drive/My Drive/ds4a-project/stats/pax_by_link/"

# Listado de los archivos para procesar
lista_files = [f for f in os.listdir(path) if f.endswith('.csv')]

# Proceso de tratamiento de datos
for l in lista_files:
    print("Cargando: " + l)
    # Read file
    df = pd.read_csv((path + l), 
                     usecols = ['DATEKEY', 'CODIGORUTA', 'HOUR', 'LINK', 'PAXUP', 'PAXDW', 'FAR'],
                     keep_default_na=False)
    # Filter by FAR
    df = df[df['FAR'] == False]
    # Group by date, route, hour and link
    df = df.groupby(['DATEKEY', 'CODIGORUTA', 'HOUR', 'LINK'], as_index = False).agg(PAXUP = ('PAXUP', 'sum'), PAXDW = ("PAXDW", 'sum'))
    # save result
    df.to_csv(path_to + str(df.DATEKEY[0]) + '_pax_link.csv', index = False)
    print("Guardado: " + l)
