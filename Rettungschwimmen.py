from typing import List, Dict 
import json

# Abzeichenklassen
class Abzeichen:
    def __init__(self):
        self.teile: List[str] = []
        self.mindestalter: int = 0 #Standardmäßig kein Mindestalter

class BronzeAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 8
        self.teile = [
            "15 Minuten Schwimmen",
            "Sprung kopfwärts",
            "2 m Tieftauchen",
            "Paketsprung"
        ]

class SilberAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 9
        self.teile = [
            "20 Minuten Schwimmen",
            "2x Tauchen",
            "Streckentauchen",
            "Sprung aus 3 m Höhe"
        ]

class GoldAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 10
        self.teile = [
            "30 Minuten Schwimmen",
            "Startsprung & Kraul",
            "50 m Brust",
            "50 m Rückenschwimmen",
            "10 m Streckentauchen",
            "3x Tauchen",
            "Sprung aus 3 m Höhe",
            "Transportschwimmen"
        ]
class JuniorretterAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 10
        self.teile = [
            "Theoretische Prüfung",
            "100m Schwimmen ohne Unterbrechung, davon 25 m Kraulschwimmen, 25 m Rückenkraulschwimmen, 25 m Brustschwimmen und 25 m Rückenschwimmen mit Grätschschwung",
            "25 m Schleppen eines Partners mit Achselschleppgriff",
            "Selbstrettungsübung: Kombinierte Übung in leichter Freizeitbekleidung, die ohne Pause in der angegebenen Reihenfolge zu erfüllen ist: fußwärts ins Wasser springen, danach Schwebelage einnehmen, 4 Minuten Schweben an der Wasseroberfläche in Rückenlage mit Paddelbewegungen, 6 Minuten langsames Schwimmen, jedoch mindestens viermal die Körperlage wechseln (Bauch-, Rücken-, Seitenlage), die Kleidungsstücke in tiefen Wasser ausziehen",
            "Fremdrettungsübung: Kombinierte Übung, die in der angegebenen Reihenfolge zu erfüllen ist: 15 m zu einem Partner in Bauchlage anschwimmen, nach halber Strecke auf ca. 2 m Tiefe abtauchen und zwei kleine Tauchringe heraufholen, diese anschließend fallen lassen und das Anschwimmen fortsetzen, Rückweg: 15 m Schleppen eines Partners mit Achselschleppgriff, Sichern des Geretteten"
        ]
        
class RettungsBronzeAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 12
        self.teile = [
            "Theoretische Prüfung",
            "200 m Schwimmen in höchstens 10 Minuten, davon 100 m in Bauchlage und 100 m in Rückenlage mit Grätschschwung ohne Armtätigkeit",
            "100 m Schwimmen in Kleidung in höchstens 4 Minuten, anschließend im Wasser entkleiden",
            "Drei verschiedene Sprünge aus etwa 1 m Höhe (z.B. Paketsprung, Schrittsprung, Startsprung, Fußsprung, Kopfsprung)",
            "15 m Streckentauchen",
            "50 m Transportschwimmen: Schieben oder Ziehen",
            "zweimal Tieftauchen von der Wasseroberfläche, einmal kopfwärts und einmal fußwärts, innerhalb von 3 Minuten mit zweimaligem Heraufholen eines 5-kg-Tauchrings oder eines gleichartigen Gegenstandes (Wassertiefe zwischen 2 und 3 m)",
            "Fertigkeiten zur Vermeidung von Umklammerungen sowie zur Befreiung aus Halsumklammerung von hinten und Halswürgegriff von hinten",
            "50 m Schleppen, je eine Hälfte mit Kopf- oder Achselschleppgriff und dem Standard-Fesselschleppgriff",
            "Kombinierte Übung, die ohne Pause in der angegebenen Reihenfolge zu erfüllen ist: 20 m Anschwimmen in Bauchlage, hierbei etwa auf halber Strecke Abtauchen auf 2 bis 3 m Wassertiefe und Heraufholen eines 5 kg Tauchrings oder eines gleichartigen Gegenstandes, diesen anschließend fallen lassen und das Anschwimmen fortsetzen; 20 m Schleppen eines Partners",
            "Demonstration des Anlandbringens",
            "3 Minuten Durchführung der Herz-Lungen-Wiederbelebung (HLW)"
        ] 
class RettungsSilberAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 14
        self.teile = [
            "Theoretische Prüfung",
            "400 m Schwimmen in 15 Min (50 m Kraul, 150 m Brust, 200 m Rücken ohne Arme)",
            "300 m Schwimmen in Kleidung in 12 Min, anschließend Entkleiden im Wasser",
            "Sprung aus 3 m Höhe",
            "25 m Streckentauchen",
            "3x Tieftauchen in 3 Min mit Heraufholen eines 5-kg-Gewichts (2x kopfwärts, 1x fußwärts)",
            "50 m Transportschwimmen in 1:30 Min (Schieben oder Ziehen)",
            "Befreiung aus Umklammerung (Halsumklammerung & Würgegriff von hinten)",
            "50 m Schleppen in 4 Min (je 25 m mit Kopf-/Achsel- & Fesselschleppgriff)",
            "Rettungsgerät anwenden (z. B. Gurtretter, Wurfleine, Rettungsring)",
            "Kombinierte Rettungsübung inkl. HLW"
        ]
class RettungsGoldAbzeichen(Abzeichen):
    def __init__(self):
        super().__init__()
        self.mindestalter = 16
        self.teile = [
            "300 m Flossenschwimmen in 6 Min (250 m Schwimmen + 50 m Schleppen mit Partner in Kleidung)",
            "300 m Schwimmen in Kleidung in 9 Min, anschließend Entkleiden im Wasser",
            "50 m Transportschwimmen in Kleidung in 1:30 Min (Schieben oder Ziehen)",
            "100 m Schwimmen in 1:40 Min",
            "30 m Streckentauchen, mindestens 8 von 10 Ringen/Tellern aufsammeln",
            "3x Tieftauchen in Kleidung in 3 Min (1x Kopfsprung, je 1x kopf- & fußwärts, jeweils 2x 5-kg-Gewichte)",
            "Befreiung aus Halsumklammerung & Halswürgegriff von hinten",
            "Kombinierte Rettungsübung mit HLW (Sprung, Schwimmen, Tauchen, Befreiung, Schleppen, Anlandbringen, 3 Min HLW)",
            "Retten mit Wurfgerät (z. B. Rettungsball mit Leine): 6 Würfe in 5 Min, 4 Treffer auf 12 m in 3-m-Zielsektor",
            "Retten mit anderem geeigneten Rettungsgerät",
            "Handhabung gebräuchlicher Wiederbelebungshilfsmittel"
        ]

ABZEICHEN_KLASSEN = [BronzeAbzeichen, SilberAbzeichen, GoldAbzeichen, JuniorretterAbzeichen, RettungsBronzeAbzeichen, RettungsSilberAbzeichen, RettungsGoldAbzeichen]


ABZEICHEN_KLASSEN_DICT = {
    "BronzeAbzeichen": BronzeAbzeichen,
    "SilberAbzeichen": SilberAbzeichen,
    "GoldAbzeichen": GoldAbzeichen,
    "JuniorretterAbzeichen": JuniorretterAbzeichen,
    "RettungsBronzeAbzeichen": RettungsBronzeAbzeichen,
    "RettungsSilberAbzeichen": RettungsSilberAbzeichen,
    "RettungsGoldAbzeichen": RettungsGoldAbzeichen
}
class Person:
    """
    Basisklasse für alle Personen (Teilnehmer, Prüfer).
    Enthält gemeinsame Kontaktdaten.
    """

    def __init__(self, vorname: str, nachname: str, alter: int, notfallnummer: str, email: str):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.notfallnummer = notfallnummer
        self.email = email
        self.pruefungen = {}

    def get_kontaktinfo(self) -> str:
        return f"{self.vorname} {self.nachname}, Alter: {self.alter}, Notfall: {self.notfallnummer}, Email: {self.email}"

    def to_dict(self) -> dict:
        return {
            "vorname": self.vorname,
            "nachname": self.nachname,
            "alter": self.alter,
            "notfallnummer": self.notfallnummer,
            "email": self.email,
            "pruefungen": self.pruefungen,
        }

class Teilnehmer(Person):
    def __init__(self, vorname: str, nachname: str, alter: int, notfallnummer: str, email: str, abzeichen_liste: list):
        super().__init__(vorname, nachname, alter, notfallnummer, email)
        self.pruefungen = {
            ab.__class__.__name__: {teil: False for teil in ab.teile} for ab in abzeichen_liste
        }
    
    @classmethod
    def from_dict(cls, teilnehmer_dict):
        instance = cls(
            vorname=teilnehmer_dict['vorname'], 
            nachname=teilnehmer_dict['nachname'], 
            alter=teilnehmer_dict['alter'], 
            notfallnummer=teilnehmer_dict['notfallnummer'], 
            email=teilnehmer_dict['email'], 
            pruefungen=teilnehmer_dict['pruefungen'], 
        )
        return instance 

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict['pruefungen'] = self.pruefungen
        return base_dict

    def pruefung_bestehen(self, abzeichen_klasse: type, teil: str):
        ab_name = abzeichen_klasse.__name__
        if ab_name in self.pruefungen and teil in self.pruefungen[ab_name]:
            self.pruefungen[ab_name][teil] = True

    def get_fortschritt(self):
        print(f"\n{self.vorname} {self.nachname} – Fortschritt:")
        for ab, teile in self.pruefungen.items():
            print(f"  {ab}:")
            for teil, status in teile.items():
                print(f"    {'✅' if status else '❌'} {teil}")
class Pruefer(Person):
    def __init__(self, vorname, nachname, alter, notfallnummer, email, abzeichen_klasse):
        super().__init__(vorname, nachname, alter, notfallnummer, email)
        self.abzeichen_klasse = abzeichen_klasse

    @classmethod
    def from_dict(cls, teilnehmer_dict):
        _abzeichen_klasse = ABZEICHEN_KLASSEN_DICT.get(teilnehmer_dict['abzeichen_klasse'])
        instance = cls(
            vorname=teilnehmer_dict['vorname'], 
            nachname=teilnehmer_dict['nachname'], 
            alter=teilnehmer_dict['alter'], 
            notfallnummer=teilnehmer_dict['notfallnummer'], 
            email=teilnehmer_dict['email'], 
            abzeichen_klasse=_abzeichen_klasse, 
        )
        return instance 


    def to_dict(self):
        base_dict = super().to_dict()
        base_dict['abzeichen_klasse'] = self.abzeichen_klasse.__name__
        return base_dict

    def pruefung_durchfuehren(self, teilnehmer, teil):
        print(f" Prüfer {self.vorname} prüft {teil} für {teilnehmer.vorname} beim Abzeichen {self.abzeichen_klasse.__name__}")
        teilnehmer.pruefung_bestehen(self.abzeichen_klasse, teil)

# Verwaltungsklasse
class Schwimmverwaltung:
    def __init__(self):
        self.teilnehmer_liste: List[Teilnehmer] = []
        self.pruefer_liste: List[Pruefer] = []

    def load_json(self, file_path='./schwimmerverwaltung.json'):
        try:
            # Filestream öffenen
            with open(file_path, 'r') as file_stream:
                # Datei Laden
                data = json.load(file_stream)
                # Attribute überschreiben 
                self.teilnehmer_liste = [Teilnehmer.from_dict(t) for t in data.get("Teilnehmer", [])] 
                self.pruefer_liste = [Pruefer.from_dict(p) for p in data.get("Pruefer", [])]
                print('Json Datei Erfolgreich geladen')
        except Exception as e :
            print(e)

    def save_to_json(self, file_path='./schwimmerverwaltung.json'):
        
        # DATEN IN EIN DICT VERWANDELN 
        data = {
            "Teilnehmer": [_teilnehmer.to_dict()  for _teilnehmer in self.teilnehmer_liste],
            "Pruefer": [_pruefer.to_dict()  for _pruefer in self.pruefer_liste], 
        }

        # JSON DATEI ÖFFNEN 
        with open(file_path, 'w') as file_stream:
            # DATEN IN JSON DATEI SCHREIBEN
            print('Write to json!')
            json.dump(data, file_stream, indent=4)


    def teilnehmer_hinzufuegen(self, teilnehmer: Teilnehmer):
        self.teilnehmer_liste.append(teilnehmer)

    def finde_teilnehmer(self, name: str) -> Teilnehmer:
        for t in self.teilnehmer_liste:
            vollname = f"{t.vorname} {t.nachname}".lower()
            if name.lower() == vollname:
                return t
        raise ValueError(" Teilnehmer nicht gefunden.")

    def teilnehmer_namen(self) -> List[str]:
        return [f"{t.vorname} {t.nachname}" for t in self.teilnehmer_liste]
    
    def teilnehmer_bearbeiten(self, teilnehmer: Teilnehmer):
        print("\n--- Teilnehmer bearbeiten ---")
        print(f"Aktueller Name: {teilnehmer.vorname} {teilnehmer.nachname}")
        neuer_vorname = input("Neuer Vorname (leer lassen zum Beibehalten): ")
        neuer_nachname = input("Neuer Nachname (leer lassen zum Beibehalten): ")
        neue_email = input("Neue E-Mail (leer lassen zum Beibehalten): ")
        neue_notfallnummer = input("Neue Notfallnummer (leer lassen zum Beibehalten): ")

        if neuer_vorname:
            teilnehmer.vorname = neuer_vorname
        if neuer_nachname:
            teilnehmer.nachname = neuer_nachname
        if neue_email:
            teilnehmer.email = neue_email
        if neue_notfallnummer:
            teilnehmer.notfallnummer = neue_notfallnummer

        print("✅ Teilnehmerdaten wurden aktualisiert.")

    def teilnehmer_loeschen(self, teilnehmer: Teilnehmer):
        self.teilnehmer_liste.remove(teilnehmer)
        print(f"🗑 Teilnehmer {teilnehmer.vorname} {teilnehmer.nachname} wurde gelöscht.")
    
    def notfall_uebersicht(self):
        print("\n🔒 NOTFALL-ÜBERSICHT ALLER TEILNEHMER 🔒")
        print("-" * 60)
        if not self.teilnehmer_liste:
            print("⚠️  Keine Teilnehmer vorhanden.")
            return
    
        for teilnehmer in self.teilnehmer_liste:
            print(f"🧒 Name: {teilnehmer.vorname} {teilnehmer.nachname}")
            print(f"🎂 Alter: {teilnehmer.alter}")
            print(f"📞 Notfallnummer: {teilnehmer.notfallnummer}")
            print(f"📧 E-Mail: {teilnehmer.email}")
            print("🎖️  Abzeichenstatus:")
            for abzeichen_name, teile_dict in teilnehmer.pruefungen.items():
                status = []
                for teil, bestanden in teile_dict.items():
                    symbol = "✔️" if bestanden else "❌"
                    status.append(f"{symbol} {teil}")
                print(f"   - {abzeichen_name}: {' | '.join(status)}")

            print("-" * 60)
            print ()
            
    def pruefer_bearbeiten(self):
        if not self.pruefer_liste:
            print("❗ Keine Prüfer vorhanden.")
            return

        print("\n--- Prüferliste ---")
        for idx, pruefer in enumerate(self.pruefer_liste, 1):
            print(f"{idx}: {pruefer.vorname} {pruefer.nachname} ({pruefer.abzeichen_klasse.__name__})")

        try:
            auswahl = int(input("Wähle einen Prüfer zum Bearbeiten (Nummer): "))
            pruefer = self.pruefer_liste[auswahl - 1]
        except (ValueError, IndexError):
            print("Ungültige Auswahl.")
            return

        print("\n--- Prüfer bearbeiten ---")
        print(f"Aktueller Name: {pruefer.vorname} {pruefer.nachname}")
        neuer_vorname = input("Neuer Vorname (leer lassen zum Beibehalten): ")
        neuer_nachname = input("Neuer Nachname (leer lassen zum Beibehalten): ")
        neue_email = input("Neue E-Mail (leer lassen zum Beibehalten): ")
        neue_notfallnummer = input("Neue Notfallnummer (leer lassen zum Beibehalten): ")

        if neuer_vorname:
            pruefer.vorname = neuer_vorname
        if neuer_nachname:
            pruefer.nachname = neuer_nachname
        if neue_email:
            pruefer.email = neue_email
        if neue_notfallnummer:
            pruefer.notfallnummer = neue_notfallnummer

        print("✅ Prüferdaten wurden aktualisiert.")
    def pruefer_loeschen(self):
        if not self.pruefer_liste:
            print("❗ Es sind keine Prüfer vorhanden.")
            return

        suchbegriff = input("🔍 Optional: Namensteil für Suche eingeben (oder Enter für alle): ").strip().lower()

        # Gefiltert + sortiert
        gefiltert = [
            pruefer for pruefer in self.pruefer_liste
            if suchbegriff in pruefer.vorname.lower() or suchbegriff in pruefer.nachname.lower()
        ]    

        if not gefiltert:
            print("⚠️ Kein Prüfer mit diesem Namen gefunden.")
            return

        sortierte_liste = sorted(gefiltert, key=lambda p: (p.nachname.lower(), p.vorname.lower()))

        print("\n--- 🔢 Gefundene Prüfer ---")
        for idx, pruefer in enumerate(sortierte_liste, 1):
            print(f"{idx}: {pruefer.vorname} {pruefer.nachname} ({pruefer.abzeichen_klasse.__name__})")

        try:
            auswahl = int(input("Wähle den Prüfer, der gelöscht werden soll (Nummer): "))
            ausgewaehlt = sortierte_liste[auswahl - 1]
        except (ValueError, IndexError):
            print("❌ Ungültige Auswahl.")
            return

        bestaetigung = input(f"Bist du sicher, dass du {ausgewaehlt.vorname} {ausgewaehlt.nachname} löschen willst? (j/n): ").lower()
        if bestaetigung == "j":
            self.pruefer_liste.remove(ausgewaehlt)
            print("✅ Prüfer wurde gelöscht.")
        else: 
            print("❎ Abbruch. Prüfer wurde nicht gelöscht.")
            
    def notfall_uebersicht_pruefer(self):
        print("\n🔒 NOTFALL-ÜBERSICHT ALLER PRÜFER 🔒")
        print("-" * 60)
        if not self.pruefer_liste:
            print("⚠️  Keine Prüfer vorhanden.")
            return
    
        for pruefer in self.pruefer_liste:
            print(f"🧒 Name: {pruefer.vorname} {pruefer.nachname}")
            print(f"🎂 Alter: {pruefer.alter}")
            print(f"📞 Notfallnummer: {pruefer.notfallnummer}")
            print(f"📧 E-Mail: {pruefer.email}")
            print(f"🎖️  Macht den Kurs mit dem Abzeichen:{pruefer.abzeichen_klasse.__name__}")
            

            print("-" * 60)
            print ()

# Menüfunktion
def menue():
    verwaltung = Schwimmverwaltung()

    while True:
        print("\n--- Hauptmenü ---")
        print("1: ➕ Teilnehmer hinzufügen")
        print("2: 📋 Teilnehmer aufrufen und Prüfung verwalten")
        print("3: ✏️ Teilnehmer bearbeiten")
        print("4: 🗑️ Teilnehmer löschen")
        print("5: ⚠️ Notfallübersicht aller Teilnehmer ⚠️")
        print()
        print("6: ➕ Prüfer hinzufügen")
        print("7: ✏️ Prüfer bearbeiten")
        print("8: 🗑️ Prüfer löschen")
        print("9: ⚠️ Notfallübersicht aller Prüfer ⚠️")
        print("10: 💾 Datei speichern")
        print("11: 📁 Datei laden")
        print()
        print("0: Beenden")

        auswahl = input("Deine Wahl: ")

        if auswahl == "1":
            print("\n--- Teilnehmer hinzufügen ---")
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            try:
                alter = int(input("Alter: "))
            except ValueError:
                print(" Ungültige Eingabe für Alter.")
                continue
            notfallnummer = input("Notfallnummer: ")
            email = input("E-Mail-Adresse: ")

            ausgewaehlte_abzeichen = []

            while not ausgewaehlte_abzeichen:
                print("\nWelche Abzeichen soll der Teilnehmer machen?")
                for idx, ab in enumerate(ABZEICHEN_KLASSEN, 1):
                    temp_ab = ab()
                    print(f"{idx}: {ab.__name__} (ab {temp_ab.mindestalter} Jahren)")

                auswahl_abz = input("Gib die Nummern ein (z. B. 1,3): ").split(",")

                for nr in auswahl_abz:
                    nr = nr.strip()
                    if nr.isdigit() and 1 <= int(nr) <= len(ABZEICHEN_KLASSEN):
                        ab_klasse = ABZEICHEN_KLASSEN[int(nr) - 1]
                        ab_obj = ab_klasse()
                        if alter >= ab_obj.mindestalter:
                            ausgewaehlte_abzeichen.append(ab_obj)
                        else:
                            print(f" ⚠️ {ab_obj.__class__.__name__} ist erst ab {ab_obj.mindestalter}.")
                    else:
                        print(f" Ungültige Auswahl: {nr}")

                if not ausgewaehlte_abzeichen:
                    print("❗ Kein gültiges Abzeichen gewählt. Bitte erneut versuchen.")

            teilnehmer = Teilnehmer(vorname, nachname, alter, notfallnummer, email, ausgewaehlte_abzeichen)
            verwaltung.teilnehmer_hinzufuegen(teilnehmer)
            print(f" Teilnehmer {vorname} {nachname} wurde hinzugefügt.")
            
        elif auswahl == "2":
            if not verwaltung.teilnehmer_liste:
                print(" Keine Teilnehmer vorhanden.")
                continue

            # Teilnehmer nach Abzeichen gruppieren
            abzeichen_map: Dict[str, List[Teilnehmer]] = {}
            for t in verwaltung.teilnehmer_liste:
                for ab in t.pruefungen.keys():
                    abzeichen_map.setdefault(ab, []).append(t)

            if not abzeichen_map:
                print(" Keine Abzeichen vorhanden.")
                continue

            print("\nVerfügbare Abzeichen:")
            abzeichen_namen = list(abzeichen_map.keys())
            for idx, ab in enumerate(abzeichen_namen, 1):
                # Prüfer für dieses Abzeichen finden
                prüfer_für_ab = [
                        p for p in verwaltung.pruefer_liste if p.abzeichen_klasse.__name__ == ab
    ]
                # Prüfer-Namen zusammenbauen
                prüfer_namen_str = ", ".join([f"Prüfer:{p.vorname} {p.nachname}" for p in prüfer_für_ab]) if prüfer_für_ab else "Keine Prüfer"
                print(f"{idx}. {ab} ({prüfer_namen_str})")
        
    
            abwahl = input("Wähle ein Abzeichen (Nummer): ")
            try:
                ab_index = int(abwahl) - 1
                ab_name = abzeichen_namen[ab_index]
            except (IndexError, ValueError):
                print(" Ungültige Auswahl.")
                continue

            teilnehmerliste = abzeichen_map[ab_name]
            print(f"\nTeilnehmer mit dem Abzeichen {ab_name}:")
            for idx, t in enumerate(teilnehmerliste, 1):
                teile_status = t.pruefungen[ab_name]
                alle_bestanden = all(teile_status.values())
                symbol = "✅🎉" if alle_bestanden else "❌"
                print(f"{idx}: {t.vorname} {t.nachname} {symbol}")


            teilwahl = input("Wähle einen Teilnehmer (Nummer): ")
            try:
                teil_index = int(teilwahl) - 1
                teilnehmer = teilnehmerliste[teil_index]
            except (IndexError, ValueError):
                print(" Ungültige Auswahl.")
                continue

            teile = list(teilnehmer.pruefungen[ab_name].keys())
            while True:
                teilnehmer.get_fortschritt()
                print("\nWas möchtest du tun?")
                print("1: Prüfungsteil abhaken")
                print("0: Zurück zum Hauptmenü")
                aktion = input("Auswahl: ")

                if aktion == "1":
                    offene_teile = [teil for teil in teile if not teilnehmer.pruefungen[ab_name][teil]]

                    if not offene_teile:
                        print("✅ Alle Prüfungsteile für dieses Abzeichen sind bereits abgehakt.")
                        continue

                    print("\nNoch offene Prüfungsteile:")
                    for idx, teil in enumerate(offene_teile, 1):
                        print(f"{idx}: {teil}")

                    teilwahl = input("Teil-Nummer: ")
                    try:
                        teil = offene_teile[int(teilwahl) - 1]
                        teilnehmer.pruefung_bestehen(eval(ab_name), teil)
                        print(f"✅ '{teil}' abgehakt.")
                    except (IndexError, ValueError, NameError):
                        print(" Ungültige Auswahl.")
                elif aktion == "0":
                    break
                else:
                    print(" Ungültige Eingabe.")

        elif auswahl == "3":
            if not verwaltung.teilnehmer_liste:
                print(" Keine Teilnehmer vorhanden.")
                continue

            print("\n--- Teilnehmer bearbeiten ---")
            for idx, t in enumerate(verwaltung.teilnehmer_liste, 1):
                print(f"{idx}: {t.vorname} {t.nachname}")

            wahl = input("Wähle einen Teilnehmer (Nummer): ")
            try:
                index = int(wahl) - 1
                teilnehmer = verwaltung.teilnehmer_liste[index]
                verwaltung.teilnehmer_bearbeiten(teilnehmer)
            except (IndexError, ValueError):
                print(" Ungültige Auswahl.")

            
        elif auswahl == "4":
            if not verwaltung.teilnehmer_liste:
                print(" Keine Teilnehmer vorhanden.")
                continue

            print("\n--- Teilnehmer löschen ---")
            for idx, t in enumerate(verwaltung.teilnehmer_liste, 1):
                print(f"{idx}: {t.vorname} {t.nachname}")

            eingabe = input("Welche Teilnehmer sollen gelöscht werden? Gib Nummern durch Komma getrennt ein (z. B. 1,3): ")
            nummern = eingabe.split(",")

            geloescht = []
            for nr in nummern:
                try:
                    index = int(nr.strip()) - 1
                    teilnehmer = verwaltung.teilnehmer_liste[index]
                    bestaetigung = input(f"Löschen von {teilnehmer.vorname} {teilnehmer.nachname} bestätigen? (j/n): ")
                    if bestaetigung.lower() == "j":
                        geloescht.append(teilnehmer)
                except (IndexError, ValueError):
                    print(f"❌ Ungültige Nummer: {nr.strip()}")

            for t in geloescht:
                verwaltung.teilnehmer_liste.remove(t)
                print(f"✅ {t.vorname} {t.nachname} gelöscht.")

            if not geloescht:
                print("❗ Keine Teilnehmer wurden gelöscht.")

        elif auswahl == "5":
            verwaltung.notfall_uebersicht()
            
        elif auswahl == "6":
            print("\n--- Prüfer hinzufügen ---")
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            try:
                alter = int(input("Alter: "))
            except ValueError:
                print("Ungültige Eingabe für Alter.")
                continue
            notfallnummer = input("Notfallnummer: ")
            email = input("E-Mail-Adresse: ")

            print("\nWelchem Abzeichen soll der Prüfer zugeordnet werden?")
            for idx, ab in enumerate(ABZEICHEN_KLASSEN, 1):
                print(f"{idx}: {ab.__name__}")
            abwahl = input("Nummer wählen: ")
            try:
                ab_index = int(abwahl) - 1
                abzeichen_klasse = ABZEICHEN_KLASSEN[ab_index]
            except (IndexError, ValueError):
                print("Ungültige Auswahl.")
                continue

            pruefer = Pruefer(vorname, nachname, alter, notfallnummer, email, abzeichen_klasse)
    
            verwaltung.pruefer_liste.append(pruefer)
            print(f"Prüfer {vorname} {nachname} wurde hinzugefügt.")

        elif auswahl == "7":
            verwaltung.pruefer_bearbeiten()
            
        elif auswahl == "8":
            verwaltung.pruefer_loeschen()
            
        elif auswahl == "9":
            verwaltung.notfall_uebersicht_pruefer()
        elif auswahl == "10":
            verwaltung.save_to_json()
        elif auswahl == "11":
            verwaltung.load_json()

        elif auswahl == "0":
                print(" Programm beendet.")
                break
        else:
            print(" Ungültige Eingabe.")

if __name__ == "__main__":
    menue()
