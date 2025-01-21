##Oppgave 3 uke 3 

import pandas as pd
import statsmodels.api as sm
import numpy as np

fil = "avling.csv"
data = pd.read_csv(fil, sep = ";")
dataframe = pd.DataFrame(data)

x =dataframe[["Gjødselmengde", "Giftmengde", "Kunstig vanning"]]
x = sm.add_constant(x)
# If you don't do sm.add_constant, the algorithms assume that b = 0 in y = mx + b. Therefore, 
# they will fit the model using b = 0 instead of calculating what b is supposed to be based on your data.
y = dataframe["Avling"]

moddellen = sm.OLS(y,x).fit()   # Merk: y først, deretter X
print(moddellen.summary())