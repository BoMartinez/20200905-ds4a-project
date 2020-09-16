#**********************************************************************************************
# @Nombre: Creacion de tabla Calendario
# @Autor: Grupo 21
# @Fecha: 2020/09/16 18:40:47
# @Ayuda: 
#**********************************************************************************************

#Importar librerias ---------------------------------------------------------------------------
import datetime as dt                 # Manipulacion de fechas
import pandas as pd                   # Manipulacion de datos
import numpy as np                    # Manipulacion numerica
import keyring                        # Manejo de contraseñas
import os, glob                       # Manejo del sistema

#Desarrollo -----------------------------------------------------------------------------------

# Parameters
start = '2019-10-01'
end = '2020-06-30'

# Creacion del dataframe
df = pd.DataFrame({'Date': pd.date_range(start, end)})
df['Date'] = pd.to_datetime(df['Date'])
df['DateKey'] = df['Date'].dt.strftime('%Y%m%d')
df['YYYYMM'] = df['Date'].dt.strftime('%Y%m')
df['DayName'] = df['Date'].dt.day_name()
df['Week'] = df['Date'].dt.weekofyear
df['Quarter'] = df['Date'].dt.quarter
df['Day'] = df['Date'].dt.day
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['IsWeekDay'] = np.where(df['DayOfWeek'] < 5, True, False)
