# Vaterklasse Benutzer
class Benutzer:
    def __init__(self, name, alter, email):
        self.name = name
        self.alter = alter
        self.email = email

    def anzeigen(self):
        print(f"Name: {self.name}")
        print(f"Alter: {self.alter}")
        print(f"E-Mail: {self.email}")


# Kindklasse 1 Schüler
class Schüler(Benutzer):
    def __init__(self, name, alter, email, klasse):
        super().__init__(name, alter, email)  # Eigenschaften der Vaterklasse
        self.klasse = klasse  # Neue Eigenschaft

    def anzeigen(self):
        super().anzeigen()  # Aufruf der Methode der Vaterklasse
        print(f"Klasse: {self.klasse}")


# Kindklasse 2 Lehrer
class Lehrer(Benutzer):
    def __init__(self, name, alter, email, fachgebiet):
        super().__init__(name, alter, email)  # Eigenschaften der Vaterklasse
        self.fachgebiet = fachgebiet  # Neue Eigenschaft

    def anzeigen(self):
        super().anzeigen()  # Aufruf der Methode der Vaterklasse
        print(f"Fachgebiet: {self.fachgebiet}")


# Testen
if __name__ == "__main__":
    # Erstellen Schüler-Objekt
    schueler = Schüler("Max Mustermann", 16, "max@schule.com", "10A")
    print("Schüler:")
    schueler.anzeigen()
    print()

    # Erstellen Lehrer-Objekt
    lehrer = Lehrer("Frau Müller", 42, "mueller@schule.com", "Mathematik")
    print("Lehrer:")
    lehrer.anzeigen()
