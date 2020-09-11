#**********************************************************************************************
# @Nombre: Limpieza y tratamiento de los datos
# @Autor: Grupo 21
# @Fecha: 2020/09/11 12:40:47
# @Ayuda: 
#**********************************************************************************************

#Importar librerias ---------------------------------------------------------------------------
import datetime as dt                 # Manipulacion de fechas
import pandas as pd                   # Manipulacion de datos
import numpy as np                    # Manipulacion numerica
import keyring                        # Manejo de contraseñas
import os, glob                       # Manejo del sistema

#Desarrollo -----------------------------------------------------------------------------------
path = "/Users/jorgesaavedra/Downloads/amva_concurso/"
path_to = "/Users/jorgesaavedra/Downloads/amva_concurso/data/"

# Listado de los archivos para procesar
lista_files = [f for f in os.listdir(path) if f.endswith('.csv')]

# Proceso de tratamiento de datos
for l in lista_files:
    print("Cargando: " + l)
    # Definicion de tipos de datos para idvehiculo y codigo de rutda
    transacciones = pd.read_csv((path + l), dtype = {'IDVEHICULO': object, 'CODIGORUTA': object})
    # Conversion de fecha
    transacciones['FECHAREGISTRO'] = pd.to_datetime(transacciones['FECHAREGISTRO'], format = '%d/%m/%Y %H:%M:%S')
    # Clave de fecha
    transacciones['DATEKEY'] = transacciones['FECHAREGISTRO'].dt.strftime('%Y%m%d')
    
    # Creacion de for para guardar los archivos por dia.
    for i in pd.unique(transacciones['DATEKEY']):
        print("Guardado: " + i)
        set_transac = transacciones[transacciones['DATEKEY'] == i]
        set_transac['HOUR'] = set_transac['FECHAREGISTRO'].dt.hour
        # Creacion de la sumatoria de columnas para pasajeros de entrada y salida
        set_transac['PAXUP'] = set_transac['SUBENDELANTERA'] + set_transac['SUBENTRASERA']
        set_transac['PAXDW'] = set_transac['BAJANDELANTERA'] + set_transac['BAJANTRASERA']
        set_transac.to_csv(path_to + i + '.csv', index = False)
