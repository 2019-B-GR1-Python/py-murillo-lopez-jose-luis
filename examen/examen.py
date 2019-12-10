import numpy as np
import pandas as pd
from scipy import ndimage
from scipy import misc

# 2) Crear un vector de ceros de tamaño 10

ej_2 = np.zeros(10)

print('EJ2 = ', ej_2)

# 3) Crear un vector de ceros de tamaño 10 y el de la posición 5 sea igual a 1

ej_3 = np.zeros(10)

ej_3[5] = 1

print('EJ3 = ', ej_3)

# 4) Cambiar el orden de un vector de 50 elemento

ej_4 = np.arange(50)

ej_4 = ej_4[::-1]

print('EJ4 = ', ej_4)

# 5) Crear una matriz 3x3 con valores del 0 al 8

ej_5 = np.arange(9)

ej_5 = ej_5.reshape((3,3))

print('EJ5 = ', ej_5)

# 6) Encontrar los indices que no sean 0

arreglo = [1,2,0,0,4,0]

arreglo = np.array(arreglo)

ej_6 = np.where(arreglo != 0)[0]

print('EJ6 = ', ej_6)

# 7) Crear una matriz identidad 3x3

ej_7 = np.eye(3)

print('EJ7 = ', ej_7)

# 8) Crear una matriz 3 x 3 x 3 con valores randomicos

ej_8 = np.random.randint(27, size=27).reshape(3,3,3)

print('EJ8 = ', ej_8)

#9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

ej_9 = np.arange(100).reshape(10,10)

ej_9_min = ej_9.min()

ej_9_max = ej_9.max()

print('EJ9 = min: ', ej_9_min, ' max: ', ej_9_max)

#10) Sacar los colores RGB unicos de una imagen

mapache = misc.face()

ej_10 = len(np.unique(mapache, axis=0))

print('EJ10 = ', ej_10)

#11) ¿Cómo crear una serie de una lista, diccionario o arreglo?

mylist = list('abcdefghijklmnsopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista = pd.Series(mylist)
serie_arr = pd.Series(myarr)
serie_dict = pd.Series(mydict)

print('EJ11 = lista: ', serie_lista, ' (',type(serie_lista),')')
print('EJ11 = arreglo: ', serie_arr, ' (',type(serie_arr),')')
print('EJ11 = diccionario: ', serie_dict, ' (',type(serie_dict),')')

#12) ¿Cómo convertir el indice de una serie en una columna de una DataFrame?

df = pd.DataFrame(serie_dict).reset_index()

print('EJ12 = ', df)

#13) ¿Cómo combinar varias series para hacer un dataframe?

ej_13 = pd.concat([serie_arr, serie_lista], axis = 1)

ej_13 = pd.DataFrame(ej_13)

print('EJ13 = ', ej_13)

#14) ¿Como obtener los items que estan en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ej_14 = np.setdiff1d(ser1, ser2)

print('EJ14 = ', ej_14)

#15) ¿Como obtener los items que no son comunes en una serie A y serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ej_15 = set(ser1) ^ set(ser2)

ej_15 = list(ej_15)

ej_15 = pd.Series(ej_15)

print('EJ15\n', ej_15)

#16) ¿Cómo obtener el número de veces que se repite el valor de una serie?

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

ej_16, counts = np.unique(ser, return_counts=True)

ej_16 = dict(zip(ej_16, counts))

print('EJ16\n', ej_16)

#17) ¿Cómo mantener los 2 valores mas repetidos de una serie, y a los demas cambiarles por 0?

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

ej_17, counts = np.unique(ser, return_counts=True)

index = np.argsort(-counts)

ej_17 = ej_17[index]

ej_17[2:] = 0
print('EJ17\n Serie: ', ser, ' Top = ', ej_17)

#18) ¿Cómo transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?

ser = pd.Series(np.random.randint(1, 10, 35))

ej_18 = pd.DataFrame(ser.values.reshape(7,5))

print('EJ18\n', ej_18, ' ', type(ej_18))

#19) ¿Obtener los valores de una serie conociendo la posición por indice?

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

ej_19 = ser[pos]

print('EJ19\n', ej_19)

#20) ¿Cómo añadir series vertical y horizonalmente a un DataFrame?

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

#Verical

df1 = pd.concat([pd.DataFrame(),ser2], ignore_index = True)

#Horizontal

df2 = pd.DataFrame().append(ser2, ignore_index=True)

print('EJ20\n', df1, '\n',df2)

#21) Obtener la media de una serie agrupada por otra serie

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))

print(pesos.tolist())
print(frutas.tolist())

ej_21 = pd.concat([frutas, pesos], axis = 1)

ej_21 = ej_21.groupby(ej_21[0], as_index=False)[1].mean()

print('EJ21', ej_21)

#22) 

#df = pd.read('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', columns=['columna1,columna2,...'])



