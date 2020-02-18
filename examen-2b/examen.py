import numpy as np
import pandas as pd
import random
import string

#Ejercicio 1

df_1 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

df_1_primeros = df_1.head(5)

df_1_ultimos = df_1.tail(5)


#Ejercicio 2

arreglo_numpy = np.random.uniform(0,1000,size=(6, 4))

columnas = pd.date_range('2020-02-18', '2020-02-24', 6)

df_2 = pd.DataFrame(arreglo_numpy, columns=list('ABCD'), index=columnas)


#Ejercicio 4

df_4 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

columnas_4 = df_4.columns

valores_4 = df_4.values


#Ejercicio 5

df_5 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

estadisticas = df_5.describe()


#Ejercicio 6

df_6 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

transpuesta = df_6.transpose()

#Eercicio 7

df_7 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

df_7_per_A_asc = df_7.sort_values('A')
df_7_per_A_desc = df_7.sort_values('A', ascending=False)

df_7_per_B_asc = df_7.sort_values('B')
df_7_per_B_desc = df_7.sort_values('B', ascending=False)

df_7_per_C_asc = df_7.sort_values('C')
df_7_per_C_desc = df_7.sort_values('C', ascending=False)

df_7_per_D_asc = df_7.sort_values('D')
df_7_per_D_desc = df_7.sort_values('D', ascending=False)

df_7_per_E_asc = df_7.sort_values('E')
df_7_per_E_desc = df_7.sort_values('E', ascending=False)

df_7_per_F_asc = df_7.sort_values('F')
df_7_per_F_desc = df_7.sort_values('F', ascending=False)


#Ejercicio 8

df_8 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_8_filtered = df_8.where(df_8 > 7)


#Ejercicio 9

df_9 = pd.DataFrame(np.random.randint(1,100,size=(10, 6)), columns=list('ABCDEF'))

df_9 = df_9.where(df_9 < 90)

df_9 = df_9.fillna(0)


#Ejercicio 10

df_10 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

#mean = average
df_10_mean = df_10.mean().mean()

df_10_mmedian = df_10.median().median()


#Ejercicio 11

df_11 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_11_2 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_11 = df_11.append(df_11_2)


#Ejercicio 12

lista_string = []

for i in range(60):
    lista_string.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))

df_12 = pd.DataFrame(np.array(lista_string).reshape(10,6), columns=list('ABCDEF'))

df_12_sol = pd.DataFrame()

df_12_sol['A'] = df_12['A'] + df_12['B'] 

df_12_sol['B'] = df_12['C'] + df_12['D']

df_12_sol['C'] = df_12['E'] + df_12['F']


#Ejercicio 13

df_13 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_3_freq_A = df_13['A'].value_counts()
df_3_freq_B = df_13['B'].value_counts()
df_3_freq_C = df_13['C'].value_counts()
df_3_freq_D = df_13['D'].value_counts()
df_3_freq_E = df_13['E'].value_counts()
df_3_freq_F = df_13['F'].value_counts()


#Ejercicio 14

df_14 = pd.DataFrame(np.random.randint(1,10,size=(10, 3)), columns=list('ABC'))

df_14['D'] = df_14['A'] * df_14['B'] / df_14['C']

