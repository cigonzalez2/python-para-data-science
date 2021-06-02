#************
#  TAREA 2  *
#************


# Realice una funcion que haga una lista de compras.
# La lista debe reproducir algo similar a lo que sigue:



# Desea agregar un producto a la lista? (Responda Y/N) :
# Y
# Ingrese el nombre del producto:
# Cereales
# Desea agregar otro producto? (Responda Y/N) :
# Y
# Ingrese el nombre del producto:
# Azucar
# Desea agregar otro producto? (Responda Y/N) :
# Y
# Ingrese el nombre del producto:
# Café
# Desea agregar otro producto? (Responda Y/N) :
# N
# La lista ha sido guardada como Lista_de_Compras.txt en la carpeta raiz.


# Como tarea extra trate que el programe no se caiga al introducir incorrectamente algun input
# Por ejemplo si pregunta si desea agregar otro producto y el usuario responde no quiero, que python no tire un error 
# si no que imprima: 
# No reconozco la respuesta, desea agregar otro producto? (Responda Y/N) :


# Torpedo

# Para seguir preguntando si agrega productos se puede usar un while.
# Para probar si se sale o no del while se puede usar un if o un break.
# Los productos se pueden agregar a una lista.
# La lista se puede guardar como un pandas dataframe y guardarlo como se muestra en el siguiente ejemplo


datos_filas1 = [1,2,3,4]
datos_filas2 = ['Azucar', 'Cafe', 'Cereales', 'Pan']

datos = {
  'N' : datos_filas1,
  'Producto' : datos_filas2
}

lista_compras = pd.DataFrame(datos)
lista_compras.to_csv('Lista.txt',sep='\t', index=False, header=True)
