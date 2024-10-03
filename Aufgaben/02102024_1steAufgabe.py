import random

# Funktion für Lottoziehung
def ziehe_lottozahlen():
    # Ziehe 6 verschiedene Zufallszahlen aus der Menge von 1 bis 45
    zahlen = random.sample(range(1, 46), 6)
    return zahlen

# Funktion für die Statistik der Lottoziehungen
def lotto_statistik(anzahl_ziehungen):
    # Dictionary für die Statistik (Zähler für jede Zahl)
    statistik = {i: 0 for i in range(1, 46)}

    # 1000 Ziehungen
    for _ in range(anzahl_ziehungen):
        gezogene_zahlen = ziehe_lottozahlen()

        # Nach jeder Ziehung die Statistik aktualisieren
        for zahl in gezogene_zahlen:
            statistik[zahl] += 1

    return statistik

# 6 Zufallszahlen ausgeben (einmalige Ziehung)
print("Lottozahlen:", ziehe_lottozahlen())

# Statistik nach 1000 Ziehungen berechnen
anzahl_ziehungen = 1000
statistik = lotto_statistik(anzahl_ziehungen)

# Statistik ausgeben
print("\nStatistik nach 1000 Ziehungen:")
for zahl, count in sorted(statistik.items()):
    print(f"Zahl {zahl}: {count} mal gezogen")
