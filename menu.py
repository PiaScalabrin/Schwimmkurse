from abzeichen import ABZEICHEN_KLASSEN
from person import Teilnehmer, Pruefer
from verwaltung import Schwimmverwaltung
from typing import Dict, List

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
                print("Ungültige Eingabe für Alter.")
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
                            print(f"⚠️ {ab_obj.__class__.__name__} ist erst ab {ab_obj.mindestalter}.")
                    else:
                        print(f"Ungültige Auswahl: {nr}")

                if not ausgewaehlte_abzeichen:
                    print("❗ Kein gültiges Abzeichen gewählt. Bitte erneut versuchen.")

            teilnehmer = Teilnehmer(vorname, nachname, alter, notfallnummer, email, ausgewaehlte_abzeichen)
            verwaltung.teilnehmer_hinzufuegen(teilnehmer)
            print(f"Teilnehmer {vorname} {nachname} wurde hinzugefügt.")

        elif auswahl == "2":
            if not verwaltung.teilnehmer_liste:
                print("Keine Teilnehmer vorhanden.")
                continue

            abzeichen_map: Dict[str, List[Teilnehmer]] = {}
            for t in verwaltung.teilnehmer_liste:
                for ab in t.pruefungen.keys():
                    abzeichen_map.setdefault(ab, []).append(t)

            if not abzeichen_map:
                print("Keine Abzeichen vorhanden.")
                continue

            print("\nVerfügbare Abzeichen:")
            abzeichen_namen = list(abzeichen_map.keys())
            for idx, ab in enumerate(abzeichen_namen, 1):
                prüfer_für_ab = [
                    p for p in verwaltung.pruefer_liste if p.abzeichen_klasse.__name__ == ab
                ]
                prüfer_namen_str = ", ".join([f"Prüfer:{p.vorname} {p.nachname}" for p in prüfer_für_ab]) if prüfer_für_ab else "Keine Prüfer"
                print(f"{idx}. {ab} ({prüfer_namen_str})")

            abwahl = input("Wähle ein Abzeichen (Nummer): ")
            try:
                ab_index = int(abwahl) - 1
                ab_name = abzeichen_namen[ab_index]
            except (IndexError, ValueError):
                print("Ungültige Auswahl.")
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
                print("Ungültige Auswahl.")
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
                        print("Ungültige Auswahl.")
                elif aktion == "0":
                    break
                else:
                    print("Ungültige Eingabe.")

        elif auswahl == "3":
            if not verwaltung.teilnehmer_liste:
                print("Keine Teilnehmer vorhanden.")
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
                print("Ungültige Auswahl.")

        elif auswahl == "4":
            if not verwaltung.teilnehmer_liste:
                print("Keine Teilnehmer vorhanden.")
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
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    menue()
