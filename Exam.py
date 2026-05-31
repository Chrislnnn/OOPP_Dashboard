from Examination import Examination

# Unterklasse von Examination (Prüfungsleistung) erstellen
class Exam(Examination):
    def __init__(self, grade, duration):
        # Die Variable grade (Note) wird von der Klasse Examination geerbt
        super().__init__(grade)
        # Die Klausur soll über die Note hinaus noch die Variable duration und name besitzen
        self.duration = duration
        # name wird festgelegt auf Klausur
        self.name = "Klausur"

        