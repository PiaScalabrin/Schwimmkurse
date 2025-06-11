from typing import Dict, List
from abzeichen import ABZEICHEN_KLASSEN_DICT

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
