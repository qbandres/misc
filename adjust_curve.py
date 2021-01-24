import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

df=pd.read_excel(r'C:\Users\qband\Documents\QBANDRES\MACHINE LEARNING\PYCHARM\PYTHON\Data analisis BB\data.xlsx',"bambas")

def func(x,a,b):
    #return a*np.exp(-b*x**2)
    return a+x*b


res, cov =  curve_fit(func,df['AVANA_B'],df['HHD_B'])

print(res)
