import numpy as np

i = int(input('Ingrese inicio de lista '))
f = int(input('Ingrese fin de Lista '))
d = int(input('ingrese particion '))

lista1 = np.linspace(i, f, d,endpoint=False,dtype = int)
lista2 = np.linspace(i,f,d,endpoint=True,dtype = float)

lista1 = lista1.tolist()                    # Convertimos a lista el numpy.ndarray
lista2 = lista2.tolist()
lista3 = np.arange(i,f,d,int)
lista4 = np.arange(i,f,d,float)


print('la lista creada con linspace es :')
print(lista1)
print(lista2)
print('La lista creada con arrange es:')
print(lista3)
print(lista4)

obj = int(input('Ingrese numero a agregar al final '))
lista1.append(obj)
print(lista1)
