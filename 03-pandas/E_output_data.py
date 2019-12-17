# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:59:20 2019

@author: jose7
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado_bin = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data_bin.pickle'

df5 = pd.read_pickle(path_guardado_bin)

df = df5.iloc[49980:50519,:].copy()

#Excel

path_de_guardado = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//mi_df_completo.xlsx'

df.to_excel(path_de_guardado)

df.to_excel(path_de_guardado, index = False)


columnas = ['artist', 'title', 'year']

df.to_excel(path_de_guardado, columns = columnas, index = False)


path_multiple = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//mi_df_multiple.xlsx'

writer = pd.ExcelWriter(path_multiple,
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = "Primera")

df.to_excel(writer, sheet_name = "Segunda", index = False)

df.to_excel(writer, sheet_name = "Tercera", columns = columnas)

writer.save()

num_artistas = df['artist'].value_counts()


path_colores = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//colores.xlsx'

writer = pd.ExcelWriter(path_colores, engine = 'xlsxwriter')

num_artistas.to_excel(writer, sheet_name='Artistas')

hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value":"99",
        "max_type":"percentile"
        }

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

chart = writer.book.add_chart(
        {
                'type' : 'column'
                })

chart.add_series({
        'values' : '=Artistas!$B$2:$B$85',
        'gap' : 2})

chart.set_y_axis({'major_gridlines' : {'visible':False}})

chart.set_legend({'position':'none'})

hoja_artistas.insert_chart('D2', chart)

writer.save()

#SQL

with sqlite3.connect("D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//bdd_artist.db") as conexion:
    df5.to_sql('py_artistas', conexion)    

##MySQL
#with mysql.connect('mysql://user:password@ip:puerto/nombre?base') as conexion:
#    df5.to_sql('tabla_mysql', conexion)
    
#JSON
    
df5.to_json("D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artist.json", orient='table')


