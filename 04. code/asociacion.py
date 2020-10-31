#**********************************************************************************************
# @Nombre: Process for the association of the demand to the nearest segment
# @Autor: Grupo 21
# @Fecha: 2020/09/16 18:40:47
# @Ayuda: 
#**********************************************************************************************

#Importar librerias ---------------------------------------------------------------------------
import datetime as dt                 # Manipulacion de fechas
import pandas as pd                   # Manipulacion de datos
import numpy as np                    # Manipulacion numerica
import os, glob                       # Manejo del sistema
import time                           # Informacion de tiempo
import re                             # Regex
import pytz                           # TimeZone

#Desarrollo -----------------------------------------------------------------------------------

from google.colab import drive
drive.mount('/content/drive')

# Introduction --------------------------------------------------------------------------------
# Process for the association of the demand to the nearest segment
#
# According to the geographical location of the event and the configuration of the points of 
# the transport network, we make the following process:
# 
# 1. Build the association function to the nearest point using the haversine equation.
# 2. Identify the first node.
# 3. Filter the data of the nodes according to the identification of the first node and then 
#    apply again the function of the nearest point.

# function to the nearest point using the haversine equation ----------------------------------
def haversine(lon1, lat1, lon2, lat2):
  # lon1, lat1, lon2, lat2 are arrays  
  KM = 6378.1370   # mean equatorial radius
  lon1, lat1, lon2, lat2 = map(np.deg2rad, [lon1, lat1, lon2, lat2])
  dlat = lat2 - lat1 
  dlon = lon2 - lon1 
  a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
  c = 2 * np.arcsin(np.sqrt(a)) 
  # devuelve la distancia en kilometros entre (lon1, lat1) y (lon2, lat2)
  return KM * c

# function to identify very far points --------------------------------------------------------
def far_point(xcoord, ycoord, link_xcoord1, link_ycoord1, limit):
  # xcoord, ycoord, link_xcoord1, link_ycoord1 are arrays, the limit is the maximum distance allowed
  # devuelve True si la distancia de un evento al nodo mas cercano es superior a limit
  return [np.amin(haversine(x, y, link_xcoord1, link_ycoord1)) > limit for x,y in zip(xcoord, ycoord)]

# function to calculate the nearest link ------------------------------------------------------
def idx_nearest_link(xcoord, ycoord, link_xcoord1, link_ycoord1):
  # xcoord, ycoord, link_xcoord1, link_ycoord1 are arrays
  nearest = np.array([np.argmin(haversine(x, y, link_xcoord1, link_ycoord1)) for x,y in zip(xcoord, ycoord)])
  # en el codigo siguiente se utiliza el nombre del dataframe de 'links' y los nombres de sus columnas:
    # 'Inode' es el id del primer nodo del i-esimo link
    # 'LongitudJn' y 'LatitudJn' son las coordenadas geográficas del segundo nodo del i-esimo link
  link = nearest + np.array([np.argmin([haversine(xcoord[i], ycoord[i],
                                                  x, y) for x,y in links.loc[links['Inode'] == links.loc[node, 'Inode'],
                                                                             ['LongitudJn','LatitudJn']].values]) for i,node in list(enumerate(nearest))])
  # devuelve el id del dataset de links del link mas cercano
  return [links['Id'].values[index] for index in link]

# Loop to get all files from folder -----------------------------------------------------------

# Definir las fechas para el procesamiento de los datos
inicio = '20191101'
fin = '20200510'

actuales = pd.date_range(start = inicio, end = fin).strftime("%Y%m%d")
actuales = [int(x) for x in actuales]

# Veririca los archivos procesados y lo quita del listado
procesados = glob.glob('/content/drive/My Drive/ds4a-project/outputs/*.csv')
procesados = [int(re.findall(r'\d{8}', i)[0]) for i in procesados]

to_run = [x for x in actuales if x not in procesados]

# Load of data --------------------------------------------------------------------------------

# Definicion del path de los archivos
path_data = "/content/drive/My Drive/ds4a-project/inputs/transacciones/"
path_to = "/content/drive/My Drive/ds4a-project/outputs/"
path_stats = "/content/drive/My Drive/ds4a-project/stats/"

# Cargue de los links
links = pd.read_csv('/content/drive/My Drive/ds4a-project/inputs/maestros/links_clean.csv')

stats = []

for i in to_run:
  startTime = time.time()
  
  print("Inicia Proceso: " + str(i) + " " + str(dt.datetime.now(pytz.timezone('America/Bogota')).time()))
  
  data = pd.read_csv(path_data + str(i) + '.csv')

  # Se crean las columnas aplicando las funciones definidas
  data['FAR'] = far_point(data['LONGITUD'].values, data['LATITUD'].values, links['LongitudIn'].values, links['LatitudIn'].values, limit = 1)
  print((time.time() - startTime))
  data['LINK'] = idx_nearest_link(data['LONGITUD'].values, data['LATITUD'].values, links['LongitudIn'].values, links['LatitudIn'].values)

  executionTime = (time.time() - startTime)

  print(executionTime)

  # Se almacena los datos transformados
  data.to_csv(path_to + str(i) + ".csv")

  # Se guarda estadisticas del proceso
  try:
    linksfar = data['FAR'].value_counts().iloc[1]
  except:
    linksfar = 0
  else:
    linksfar
  
  stats.append(
        {
          'Archivo': i,
          'Tiempo': executionTime,
          'LinksAsigandos' : data['FAR'].value_counts().iloc[0],
          'LinksFar' : linksfar
        }
    )

stats = pd.DataFrame(stats)
stats.to_csv(path_stats + inicio + "_" + fin + "_stats.csv", index = False)
