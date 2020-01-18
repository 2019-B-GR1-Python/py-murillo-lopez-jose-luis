# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:05 2020

@author: jose7
"""

import pandas as pd
import math

path_guardado_bin = 'D://Documents//GitHub//py-murillo-lopez-jose-luis//03-pandas//data//artwork_data_bin.pickle'

df5 = pd.read_pickle(path_guardado_bin)

seccion_df = df5.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)

for columna_agrupada, df_completo in df_agrupado:
    print(columna_agrupada)
    print(df_completo)

a = seccion_df['units'].value_counts()

a.empty

def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(math.isnan(valor_serie)):
                    pass
                else:
                    valor = int(valor_serie)
                    suma = suma + valor
                    numero_valores += 1
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        elif(tipo == 'frequency'):
            max = lista_valores.reset_index().head(1)['index'][0]
            series_valores_llenos = series.fillna(max)
            return series_valores_llenos
        
        
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    
    for artista, df in df_artist:
        serie_w = df['width']
        serie_h = df['height']
        df.loc[:,'width'] = llenar_valores_vacios(serie_w, 'frequency')
        df.loc[:,'height'] = llenar_valores_vacios(serie_h, 'frequency')
        lista_df.append(df)
    
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores


df_completo = transformar_df(seccion_df)

a = seccion_df['width']
