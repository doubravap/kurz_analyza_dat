# Importy knihoven
import pandas as pd
import geopandas as gpd
from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from shapely.geometry import Point

# Vykresleni vsech sloupcu
pd.set_option("display.max_columns", None)

## Nacteni dat o celnich kontrolach
cesta_kontroly = Path("Data_kontroly.csv")
data_kontroly = pd.read_csv(cesta_kontroly, sep=";")
print(data_kontroly.head())

## Chybejici hodnoty
print(data_kontroly.isna().sum())

## Celkova velikost datasetu
print(data_kontroly.shape)

## Upraveni GPS souradnic
data_kontroly["axisx"] = data_kontroly["axisx"].apply(lambda x: float(x.replace(",", ".")))
data_kontroly["axisy"] = data_kontroly["axisy"].apply(lambda x: float(x.replace(",", ".")))

## Vytvoreni sloupce pro usporadanou dvojici souradnic
data_kontroly["zemepisna_poloha"] = list(zip(data_kontroly["axisx"],
                                             data_kontroly["axisy"]))
# Transofrmace souradnic do bodu pro pozdejsi zobrazeni
data_kontroly["zemepisna_poloha"] = data_kontroly["zemepisna_poloha"] \
                                        .apply(lambda x: Point(x))

## Vraceni radku s nevyplnenym ID vozidla
print("Chybejici ID vozidla")
print(data_kontroly[data_kontroly["ID_vozidla"].isna()])

## Nalezeni casoveho obdobi dat
print("\n----Casove obdobi----")
casove_obdobi_od = data_kontroly["LocDate"].min()
casove_obdobi_do = data_kontroly["LocDate"].max()
print(f"Kontroly probihaly v obdobi od {casove_obdobi_od} do {casove_obdobi_do}.")

## Statistika pokut
print("\n----Statistika pokut----")
statistika_pokuty = data_kontroly[["penalty", "NotCashPenalty", "CashPenalty",
                                   "CashLessPenalty"]].describe()
print(statistika_pokuty)

# Statistika pokut pro kontroly, kde pokuta byla udelena
statistika_udelene_pokuty = data_kontroly[data_kontroly["penalty"] > 0][["penalty"]] \
                                .describe()
print("")
print(statistika_udelene_pokuty)

print("\n----Celkova vyse udelenych pokut---")
print(f"{data_kontroly["penalty"].sum():,}")

## Kontrola, jestli neni v tabulce duplicita podle ID vozidla (melo by byt unikatni)
print("\n----Pocet kontrol na kazde ID vozidla----")
pocty_kontrol_na_vozidlo = (data_kontroly["ID_vozidla"].value_counts()
                                .sort_values(ascending=False))
print(pocty_kontrol_na_vozidlo)

## Kontroly podle kodu zeme
# Pocty kontrol podle kodu zemi
kody_kontroly = data_kontroly["kod"].value_counts().reset_index()
kody_kontroly.columns = ["kod", "pocet"]

# Diskriminujeme ceska auta a auta, ktera nejsou z deseti nejcastejsich zemi
kody_kontroly = kody_kontroly[kody_kontroly["kod"] != "CZ"]
kody_kontroly = kody_kontroly.sort_values("pocet", ascending=False).reset_index(drop=True)
kody_kontroly = kody_kontroly.head(10)
fig, ax = plt.subplots(figsize=(10, 10))
kody_kontroly.plot(ax=ax, x="kod", y="pocet", kind="bar")

# Soucty udelenych pokut podle kodu zeme
kody_kontroly_sumy = data_kontroly.groupby("kod")["penalty"].sum().reset_index()
kody_kontroly_sumy.columns = ["kod", "soucet"]
kody_kontroly_sumy = kody_kontroly_sumy.sort_values("soucet", ascending=False)
kody_kontroly_sumy.plot(x="kod", y="soucet", kind="bar")
plt.show()