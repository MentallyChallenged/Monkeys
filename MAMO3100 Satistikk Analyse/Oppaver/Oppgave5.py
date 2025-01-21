## Oppgave 5
import pandas as pd

filen = "Housing.csv"
data = pd.read_csv(filen, sep=";")

x_gjennom = data["price"].mean()
y_gjennom = data["area"].mean()

print(f"Gjennomsnitt pris er (x̄): {x_gjennom}")
print(f"Gjennomsnitt areal er (ȳ): {y_gjennom}")

## nå krysspuntkene  summen(xi^2), summen(yi^2) og summen(xi*yi)

sum_x = (data["price"]**2).sum()
sum_y = (data["area"]**2).sum()
sum_xy = (data["price"]*data["area"]).sum()

print(f"Sum av x_i^2 (∑x²): {sum_x}")
print(f"Sum av y_i^2 (∑y²): {sum_y}")
print(f"Sum av x_i*y_i (∑xy): {sum_xy}")

## Beregner betta b, stigningstallet 

b = (sum_xy - len(data) * x_gjennom * y_gjennom) / (sum_x - len(data) * x_gjennom**2)

## nå regne ut alfa, konstanten

a = y_gjennom - b * x_gjennom

print(f"Stigningstall (b): {b}")
print(f"Konstant (a): {a}")
