import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats

# Korelační test
# Načtení dat
data_korelace = pd.read_csv("korelace_praxe_pripady.csv")
# Zobrazení prvních 5 řádků
print(data_korelace.head())
# Vizualizace závislosti mezi sloupci
sns.relplot(data_korelace, x="Délka praxe (roky)", y="Počet odhalených případů")
# plt.show()
# Korelační test (Pearsonův koeficient)
pearsonova_korelace, pearsonova_p_hodnota = stats.pearsonr(data_korelace["Délka praxe (roky)"],
                                                           data_korelace["Počet odhalených případů"])
print(f"Pearsonova korelace: {pearsonova_korelace}, p-hodnota {pearsonova_p_hodnota}.")

# Korelační test (Spearmanův koeficient)
spearmanova_korelace, spearmanova_p_hodnota = stats.spearmanr(data_korelace.iloc[:, 0],
                                                              data_korelace.iloc[:, 1])
print(f"Spearmanova korelace: {spearmanova_korelace}, p-hodnota {spearmanova_p_hodnota}.")

# ANOVA (analýza rozptylů)
data_anova = pd.read_csv("zachyty_celni_prechody.csv", index_col="Týden")
pd.set_option('display.max_columns', None)
print(data_anova.head())
print("")
data_anova_vizualizace = data_anova.stack().reset_index() \
                        .rename(columns={"level_1": "Místo", 0: "Počet"})
sns.relplot(data_anova_vizualizace.iloc[-40:, :], x="Týden", y="Počet", hue="Místo", kind="line")
plt.show()

# Jednofaktorová ANOVA
statistika, p_hodnota = stats.f_oneway(data_anova.iloc[:, 0],
                                       data_anova.iloc[:, 1],
                                       data_anova.iloc[:, 2],
                                       data_anova.iloc[:, 3])

print(f"f-statistika: {statistika}, p-hodnota: {p_hodnota}.")
