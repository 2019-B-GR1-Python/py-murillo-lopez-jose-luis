# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:22:01 2019

@author: jose7
"""

import pandas as pd
import os

# 1) JSON CSV HTML XML ...
# 2) Binary files 
# 3) Relational databases

path = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data.csv'

df1 = pd.read_csv(
        path,
        nrows = 10)

columnas = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']


df2 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas)

df3 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas,
        index_col = 'id')

to_save_path = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data.pickle'

df3.to_pickle(to_save_path)


to_save_path_bin = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data_bin.pickle'

df4 = pd.read_csv(
        path)

df4.to_pickle(to_save_path_bin)

df5 = pd.read_pickle(to_save_path)



