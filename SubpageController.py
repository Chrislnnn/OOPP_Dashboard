from CourseRepository import CourseRepository

class SubpageController:
    def __init__(self, view, dashboard):
        self.view = view
        # Über course_repository erfolgen Zugriffe auf die Datenbank
        self.course_repository = CourseRepository()
        self.dashboard = dashboard

    def display_courses(self):
        # Alle aktiven und abgeschlossenen Kurse aus der Datenbank abfragen
        active_courses = self.course_repository.get_all_active_courses()
        finished_courses = self.course_repository.get_all_finished_courses()

        # Alle Daten aus courses als String verknüpfen (für die Ausgabe)
        active_courses_records = ''
        for record in active_courses:
            active_courses_records += str(record[0]) + "\n"
        # Alle Daten aus finished courses als String verknüpfen (für die Ausgabe)
        finished_courses_records = ''
        for record in finished_courses:
            finished_courses_records += str(record[0] + ", Note: " + str(record[2])) + "\n"

        # Alle aktiven und abgeschlossenen Kurse ausgeben (ein Beispiel für die Unterseite)
        self.view.show_courses(active_courses_records, finished_courses_records)