import numpy as np
import math
# Newton.py: Skript som beregner nullpunkt ved Newtons metode.
# Definer funksjonen som vi skal bestemme nullpunktet til:
def f(x):
    return (x+1)**(1/2) + x** (1/3) - 2
# Og den deriverte:
def fd(x):
    return (1/2)*(x+1)**(-1/2) +(1/3)* x ** (-2/3)
# Sett startpunktet x0 :
x0=4
# Definerer hjelpevariabel "avvik":
avvik=0.001
antall = 0
while avvik>0.0001:
# Regn ut neste punkt i iterasjonen:
    xneste=x0-f(x0)/fd(x0)
# Regn ut avviket mellom to påfølgende punkter:
    avvik=np.abs(x0-xneste)
    x0=xneste
    antall+=1
# Skriv til skjerm
    print(xneste)
print(antall)