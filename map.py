from functools import reduce

my_list = [1,3,5,4,5,6,3,5,12,3,4,5]

#Lista de impares
odd1 = [i for i in my_list if i%2!=0]
odd2 = list(filter(lambda x: x%2 !=0,my_list))
print(f'La lista es {my_list}')
print(odd1)
print(odd2)

# Al cuadrado
squares1 = [i**2 for i in my_list]
squares2 = list(map(lambda x : x**2,my_list))
print(f'la lista al cuadrado es {squares1}')
print(squares2)
all_mult1 = 1
for i in my_list:
    all_mult1 = all_mult1*i

all_mult2 =  reduce(lambda a, b:a*b,my_list)

print(f'la multiplicacion de elements es {all_mult1}')
print(all_mult2)
