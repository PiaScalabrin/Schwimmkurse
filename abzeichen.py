from typing import List

class Abzeichen:
    def __init__(self):
        self.teile: List[str] = []
        self.mindestalter: int = 0  # Standardmäßig kein Mindestalter

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
