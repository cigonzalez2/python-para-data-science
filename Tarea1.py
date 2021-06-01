#*********************
#      TAREA 1       *
#*********************


#     1. Hacer una funcion que entregue un promedio de notas.
#     a) Tiene que pedir cuantas notas se van a promediar.
#     b) Tiene que pedir cada nota y el ramo.
#     c) Imprimir el promedio de las notas.
#     d) Imprimir un dataframe con las notas y los ramos.

#********************
#      TORPEDO      *
#********************

# Input Variables  

var1 = float(input('texto'))


# Funciones:

def nombre_funcion(argumentos):
  aux = 'algo'
  return aux


# Tablas:

import pandas as pd

datos_filas1 = [1,2,3,4]
datos_filas2 = ['a', 'b', 'c', 'd']

datos = {
  'col1' : datos_filas1,
  'col2' : datos_filas2
}

tabla = pd.DataFrame(datos)
