# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:14 2019

@author: jose7
"""


import pandas as pd

path_guardado_bin = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data_bin.pickle'

df5 = pd.read_pickle(path_guardado_bin)

primero = df5.loc[1035]

segundo = df5.iloc[1035]

df_index = df5.set_index('id')

primero = df_index.loc[1035]

segundo = df_index.iloc[1035]

datos = {
        "nota_1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }

df_prueba = pd.DataFrame(datos)

prueba_1= df_prueba.loc["Pepito"]

prueba_2 = df_prueba.iloc[0]

df_prueba.loc[['Pepito', 'Juanita'], ['disciplina', 'nota_1']]


condicion_nota = df_prueba['nota_1'] > 7

df_prueba.loc[condicion_nota]

condicion_doble = df_prueba['disciplina'] > 7

df_prueba.loc[condicion_nota][condicion_doble]

df_prueba.loc['Maria','disciplina'] = 7

#Ej1: Poner un valor en algunos valores de la columna

condicion_disciplina = df_prueba['disciplina'] < 7

df_prueba.loc[condicion_disciplina, ['disciplina']] = 7

#Ej2: Poner un valor en toda la fila

df_prueba.loc['Pepito'] = 10

#Ej3: Poner un valor en toda la columna

df_prueba.loc[:, 'disciplina'] = 7

#Ej4: Promediar dos columnas

df_prueba['promedio'] = (df_prueba['nota_1'] + df_prueba['disciplina']) / (df_prueba.columns.size - 1) 


