#Modificado desde MSI  24-Jan-2022
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
lista3 = lista3.tolist()

print('la lista creada con linspace es Lista1 :')
print(lista1)
print(lista2)
print('La lista creada con arrange es lista 3:')
print(lista3)
print(lista4)

obj = int(input('Ingrese numero a agregar al final '))
print(f'La lista original es {lista1}')
lista1.append(obj)
print(f'La lista agregada es {lista1}')
print(f'El numero que se repite {obj} es {lista1.count(obj)}')
lista1.extend(lista3)
print(f'La union de lista 1 y lista 3 es {lista1}')
print(f'La posicion del elemento {obj} es {lista1.index(obj)}')
lista1.reverse()
print(f'el inverso de la lista es {lista1}')
rem = int(input('Ingrese elemento a remover '))
lista1.remove(rem)
print(f'La lista final quedaria eliminando el número {rem}  {lista1}')
lista1.pop(rem)
print(f'Esa misma lista se elimina el elemento en la posicion {rem} quedaria {lista1}')
lista1.insert(rem,obj)
print(f'Se agrego el elemnto {obj}, en la posicion {rem} y el resultado es {lista1}')
lista1.sort(reverse=True)
print(f'La lista ordenada seria {lista1}')
