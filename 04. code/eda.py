#**********************************************************************************************
# @Nombre: Analisis Exploratorio de datos
# @Autor: Grupo 21
# @Fecha: 2020/09/11 12:38:15
# @Ayuda: 
#**********************************************************************************************

#Importar librerias ---------------------------------------------------------------------------
import datetime as dt                 # Manipulacion de fechas
import pandas as pd                   # Manipulacion de datos
import numpy as np                    # Manipulacion numerica
import keyring                        # Manejo de contraseñas
import sweetviz as sv

#Desarrollo -----------------------------------------------------------------------------------
datos = pd.read_csv('/Users/jorgesaavedra/Downloads/amva_concurso/data/20191101.csv')

report = sv.analyze(datos)
report.show_html()


