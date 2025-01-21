### Uke 2 oppgave 4 a)
import pandas as pd

fil = "Uke2_Oppg5.csv"
data = pd.read_csv(fil, sep= ";")    #vanlighvis skilles cvs filene med en ",", men i denne filen er det et ";"

x_gjenn = data["Reklameutgifter"].mean()
y_gjenn = data["Salg"].mean()

print(f"Gjennomsnitt reklameutgift er (x̄): {x_gjenn}")
print(f"Gjennomsnitt salg er (ȳ): {y_gjenn}")

## nå krysspuntkene  summen(xi^2), summen(yi^2) og summen(xi*yi)

sum_x = (data["Reklameutgifter"]**2).sum()
sum_y = (data["Salg"]**2).sum()
sum_xy = (data["Reklameutgifter"]*data["Salg"]).sum()

print(f"Sum av x_i^2 (∑x²): {sum_x}")
print(f"Sum av y_i^2 (∑y²): {sum_y}")
print(f"Sum av x_i*y_i (∑xy): {sum_xy}")