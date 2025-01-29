import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Erklärungstext
print("Bravais-Pearson-Korrelationskoeffizient (r)")
print("-------------------------------------------")
print("r misst die lineare Beziehung zwischen zwei Variablen.")
print("Kombination von theoretischen und realen Beispielen:\n")

# Berechnungsformel
formel = """
Berechnungsformel:
          ∑(x_i - x̄)(y_i - ȳ)
r = -------------------------------
    √[∑(x_i - x̄)²] * √[∑(y_i - ȳ)²]
"""
print(formel)

# Daten erzeugen
np.random.seed(42)

# Theoretische Beispiele
x_pos = np.linspace(0, 10, 100)
y_pos = x_pos + np.random.normal(0, 1, 100)

x_neg = np.linspace(0, 10, 100)
y_neg = -x_neg + np.random.normal(0, 1, 100)

x_null = np.random.normal(5, 2, 100)
y_null = np.random.normal(5, 2, 100)

x_nonlin = np.linspace(-5, 5, 100)
y_nonlin = x_nonlin**2 + np.random.normal(0, 1, 100)

x_perf = np.linspace(0, 10, 100)
y_perf = x_perf

x_out = np.append(np.random.normal(5, 2, 100), 30)
y_out = np.append(np.random.normal(5, 2, 100), 30)

# Realistische Beispiele
studienzeit = np.random.normal(15, 5, 100)
pruefungsergebnis = 40 + 3*studienzeit + np.random.normal(0, 8, 100)

temperatur = np.random.uniform(10, 35, 100)
heizungskosten = 1000 - 15*temperatur + np.random.normal(0, 100, 100)

einkommen = np.random.normal(3000, 1000, 100)
sparbetrag = 0.2*einkommen + np.random.normal(0, 200, 100)

# Plot-Setup
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Theoretische Plots
axs[0,0].scatter(x_pos, y_pos, c='#1f77b4')
axs[0,0].set_title(f"Theoretisch: Starke positive Korrelation\n(r = {pearsonr(x_pos, y_pos)[0]:.2f})")
axs[0,0].set_xlabel("Variable X")
axs[0,0].set_ylabel("Variable Y")

axs[0,1].scatter(x_neg, y_neg, c='#ff7f0e')
axs[0,1].set_title(f"Theoretisch: Starke negative Korrelation\n(r = {pearsonr(x_neg, y_neg)[0]:.2f})")
axs[0,1].set_xlabel("Variable X")
axs[0,1].set_ylabel("Variable Y")

# Realistische Plots
axs[1,0].scatter(studienzeit, pruefungsergebnis, c='#2ca02c')
axs[1,0].set_title(f"Bildung: Lernstunden vs. Prüfungsergebnis\n(r = {pearsonr(studienzeit, pruefungsergebnis)[0]:.2f})")
axs[1,0].set_xlabel("Wöchentliche Lernzeit (h)")
axs[1,0].set_ylabel("Prüfungspunktzahl")

axs[1,1].scatter(temperatur, heizungskosten, c='#d62728')
axs[1,1].set_title(f"Energie: Temperatur vs. Heizkosten\n(r = {pearsonr(temperatur, heizungskosten)[0]:.2f})")
axs[1,1].set_xlabel("Durchschnittstemperatur (°C)")
axs[1,1].set_ylabel("Monatliche Heizkosten (€)")

# Kombinierte Plots
axs[2,0].scatter(x_out, y_out, c='#9467bd')
axs[2,0].annotate('Ausreißer', xy=(30,30), xytext=(25,25),
                 arrowprops=dict(facecolor='black', shrink=0.05))
axs[2,0].set_title(f"Problemfall: Einfluss von Ausreißern\n(r = {pearsonr(x_out, y_out)[0]:.2f})")
axs[2,0].set_xlabel("Variable X")
axs[2,0].set_ylabel("Variable Y")

axs[2,1].scatter(einkommen, sparbetrag, c='#8c564b')
axs[2,1].set_title(f"Finanzen: Einkommen vs. Sparbetrag\n(r = {pearsonr(einkommen, sparbetrag)[0]:.2f})")
axs[2,1].set_xlabel("Monatliches Nettoeinkommen (€)")
axs[2,1].set_ylabel("Monatliche Sparsumme (€)")

plt.tight_layout()

# Zusatzinformationen
print("Kombinierte Interpretation:")
print("- Theoretische Beispiele zeigen Grundmuster")
print("- Praxisbeispiele demonstrieren reale Anwendungen")
print("- Beachte: Reale Daten enthalten immer Störfaktoren")
print("- Korrelation ≠ Kausalität bleibt zentraler Punkt\n")

# Beispielvergleich
print("Vergleich Bildungsdaten:")
print(f"Pearson r: {pearsonr(studienzeit, pruefungsergebnis)[0]:.3f}")
print(f"p-Wert:    {pearsonr(studienzeit, pruefungsergebnis)[1]:.4f}")

plt.show()