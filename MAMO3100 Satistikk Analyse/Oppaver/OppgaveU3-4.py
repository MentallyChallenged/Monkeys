## Oppgave 4 -- Uke 3

import pandas as pd
import statsmodels.api as sm 

file = "Høyde.csv"
data = pd.read_csv(file, sep = ";")

x_gjenn = data["Fars høyde"].mean()
y_gjenn = data["Sønns høyde"].mean()

print(f"Gjennomsnitt fars høyde er (x̄): {x_gjenn}")
print(f"Gjennomsnitt sønns høyde er (ȳ): {y_gjenn}")

sum_x = (data["Fars høyde"]**2).sum()
sum_y = (data["Sønns høyde"]**2).sum()
sum_xy = (data["Fars høyde"]*data["Sønns høyde"]).sum()

print(f"Sum av x_i^2 (∑x²): {sum_x}")
print(f"Sum av y_i^2 (∑y²): {sum_y}")
print(f"Sum av x_i*y_i (∑xy): {sum_xy}")

dataframe = pd.DataFrame(data)
x = dataframe[["Fars høyde"]]
y = dataframe[["Sønns høyde"]]
x = sm.add_constant(x)

moddellen = sm.OLS(y,x).fit()
print(moddellen.summary())

## lage regrosjonsligningen
# danner koefisentene 
koeffisienter = moddellen.params
print(koeffisienter)

uttrykk = [f"{koeff:.4f} * x{i}" for i, koeff in enumerate(koeffisienter[1:], start = 1)]
ligningn = f"y = {koeffisienter[0]:.4f} + " + " + ".join(uttrykk)
print("Regresjons lingingen er: ")
print(ligningn)