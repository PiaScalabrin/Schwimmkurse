import json
from typing import List, Dict
from person import Teilnehmer, Pruefer

class Schwimmverwaltung:
    def __init__(self):
        self.teilnehmer_liste: List[Teilnehmer] = []
        self.pruefer_liste: List[Pruefer] = []

    def load_json(self, file_path='./schwimmerverwaltung.json'):
        try:
            with open(file_path, 'r') as file_stream:
                data = json.load(file_stream)
                self.teilnehmer_liste = [Teilnehmer.from_dict(t) for t in data.get("Teilnehmer", [])]
                self.pruefer_liste = [Pruefer.from_dict(p) for p in data.get("Pruefer", [])]
                print('Json Datei Erfolgreich geladen')
        except Exception as e:
            print(e)

    def save_to_json(self, file_path='./schwimmerverwaltung.json'):
        data = {
            "Teilnehmer": [_teilnehmer.to_dict() for _teilnehmer in self.teilnehmer_liste],
            "Pruefer": [_pruefer.to_dict() for _pruefer in self.pruefer_liste],
        }

        with open(file_path, 'w') as file_stream:
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
            print("⚠️ Keine Teilnehmer vorhanden.")
            return

        for teilnehmer in self.teilnehmer_liste:
            print(f"🧒 Name: {teilnehmer.vorname} {teilnehmer.nachname}")
            print(f"🎂 Alter: {teilnehmer.alter}")
            print(f"📞 Notfallnummer: {teilnehmer.notfallnummer}")
            print(f"📧 E-Mail: {teilnehmer.email}")
            print("🎖️ Abzeichenstatus:")
            for abzeichen_name, teile_dict in teilnehmer.pruefungen.items():
                status = []
                for teil, bestanden in teile_dict.items():
                    symbol = "✔️" if bestanden else "❌"
                    status.append(f"{symbol} {teil}")
                print(f"   - {abzeichen_name}: {' | '.join(status)}")

            print("-" * 60)
            print()

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
            print("⚠️ Keine Prüfer vorhanden.")
            return

        for pruefer in self.pruefer_liste:
            print(f"🧒 Name: {pruefer.vorname} {pruefer.nachname}")
            print(f"🎂 Alter: {pruefer.alter}")
            print(f"📞 Notfallnummer: {pruefer.notfallnummer}")
            print(f"📧 E-Mail: {pruefer.email}")
            print(f"🎖️ Macht den Kurs mit dem Abzeichen: {pruefer.abzeichen_klasse.__name__}")

            print("-" * 60)
            print()
