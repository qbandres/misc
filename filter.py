import pandas as pd

names = ["Arum","Varum","Ram","Mohan","Andres","Yoavna","Claudia"]
age = [29,21,32,51,34,78,23]

df = pd.DataFrame(list(zip(names,age)),columns=["Name","age"])

#Vamos a filtrar impares
odd = [i for i in df.age if i % 2 != 0 ]
odd2 = list(filter(lambda x: x%2 !=0, df.age ))

squares = [i**2 for i in df.age]
squares2 = list(map(lambda x: x**2, df.age))

print(df)
print(odd)
print(odd2)

print(squares)
print(squares2)