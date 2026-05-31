from CourseRepository import CourseRepository

class Study:
    def __init__(self, name_input):
        self.name = name_input
        # Über course_repository erfolgen Zugriffe auf die Datenbank
        self.course_repository = CourseRepository()

    # Wenn der Nutzer zum ersten Mal sein Dashboard erstellt, werden beispielhaft Kurse ins Dashboard hinzugefügt (basierend auf dem Studiengang)
    # Momentan werden jedoch nur 2 verschiedene Studiengänge angeboten (Softwareentwicklung und Mathematik)
    def add_starting_courses(self):
        # Basierend auf dem Studiengang werden hier einige Kurse als Beispiel initalisiert
        if self.name == "Software Engineering":
            self.course_repository.add_new_course("Requirements Engineering", "Platzhalter für Kursbeschreibung","Klausur")
            self.course_repository.add_new_course("Python Projekt", "Platzhalter für Kursbeschreibung", "Projekt")
        elif self.name == "Mathematics":
            self.course_repository.add_new_course("Stochastik", "Platzhalter für Kursbeschreibung", "Klausur")
            self.course_repository.add_new_course("Lineare Algebra", "Platzhalter für Kursbeschreibung", "Klausur")
            self.course_repository.add_new_course("Analysis", "Platzhalter für Kursbeschreibung", "Klausur")