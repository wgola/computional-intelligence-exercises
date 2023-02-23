import pandas as pd
import matplotlib.pyplot as plt

miasta = pd.read_csv("~/Documents/inteligencja-obliczeniowa/lab01/miasta.csv")

print("Tabela z danymi: ")
print(miasta)

print("Wartości tabeli: ")
print(miasta.values)

miasta.loc[len(miasta)] = [2010, 460, 555, 405]

print("Tabela z dodanym wierszem: ")
print(miasta)

miasta.plot(x="Rok", y="Gdansk", marker="o", color="red", legend=False,
            title="Ludnosc w miastach Polski", xlabel="Lata", ylabel="Liczba ludnosci [W tys.]")


miasta.plot(x="Rok", y=["Gdansk", "Poznan", "Szczecin"], marker="o",
            title="Zmiany ludnosci w miastach", xlabel="Lata", ylabel="Liczba ludnosci [W tys.]")

plt.show()

df = miasta.drop('Rok', axis=1)

df_stand = (df - df.mean())/df.std()
mean_stand = df_stand.mean()
sd_stand = df_stand.std()
df_stand["Rok"] = miasta["Rok"]

print("Ustandaryzowane dane: ")
print(df_stand)
print("Średnia: ")
print(mean_stand)
print("Odchylenie standardowe: ")
print(sd_stand)

df_norm = (df - df.min())/(df.max()-df.min())
min_norm = df_norm.min()
max_norm = df_norm.max()
df_norm["Rok"] = miasta["Rok"]

print("Znormalizowane dane:")
print(df_norm)
print("Wartość minimalna: ")
print(min_norm)
print("Wartość maksymalna: ")
print(max_norm)
