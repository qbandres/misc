#Nuevos
import pandas as pd
#url='https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
d_abalone=pd.read_csv(url,header=None)


print(d_abalone)
