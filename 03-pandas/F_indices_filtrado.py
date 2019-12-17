# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:50:46 2019

@author: jose7
"""

import pandas as pd

path_guardado_bin = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data_bin.pickle'

df5 = pd.read_pickle(path_guardado_bin)

#Obtener los nombres de los artistas

serie_artistas_repetidos = df5["artist"]

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)

blake = df5["artist"] == "Blake, William"

blake.value_counts()

df5["artist"].value_counts()

df_blake = df5[blake]


