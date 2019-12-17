# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:22 2019

@author: jose7
"""

import numpy as np
import pandas as pd


arr_panda = np.random.randint(0, 10, 6).reshape(2,3)

df1 = pd.DataFrame(arr_panda)

s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

df1[3] = pd.Series([1, 2])

df1[4] = s1 * s2


datos_fisicos_uno = pd.DataFrame(
        arr_panda,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (años)'])

datos_fisicos_dos = pd.DataFrame(
        arr_panda,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (años)'],
        index = ['José', 'Luis'])

df1.index = ['José', 'Luis']






