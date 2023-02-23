import pandas as pd
import matplotlib.pyplot as plt

miasta = pd.read_csv("~/Documents/inteligencja-obliczeniowa/lab01/miasta.csv")

print(miasta)

print(miasta.values)

miasta.loc[len(miasta)] = [2010, 460, 555, 405]

print(miasta)

miasta.plot(x="Rok", y="Gdansk", marker="o", color="red", legend=False,
            title="Ludnosc w miastach Polski", xlabel="Lata", ylabel="Liczba ludnosci [W tys.]")


miasta.plot(x="Rok", y=["Gdansk", "Poznan", "Szczecin"], marker="o",
            title="Zmiany ludnosci w miastach", xlabel="Lata", ylabel="Liczba ludnosci [W tys.]")

plt.show()

df = miasta.drop('Rok', axis=1)

df_stand = (df - df.mean())/df.std()
df_stand = pd.concat((df_stand, miasta["Rok"]), 1)

df_norm = (df - df.min())/(df.max()-df.min())
df_norm = pd.concat((df_norm, miasta["Rok"]), 1)

print(df_norm)
print(df_stand)
