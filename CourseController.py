from CourseRepository import CourseRepository
from CourseView import CourseView
from tkinter import messagebox

class CourseController:
    def __init__(self, dashboard):
        self.view = None
        self.course_repository = CourseRepository()
        self.dashboard = dashboard

    def open_course_page(self, course, dashboard):
        self.view = CourseView(dashboard, self, course)

    # Methode zum Abschließen eines Kurses
    def finish_course(self, course, grade):
        # Sicherstellen, dass die Eingabe auch wirklich eine sinnvolle Note ist
        if not (grade.isdigit() and 1 <= int(grade) <= 6):
            # Andernfalls Nutzer über inkorrekte Eingabe informieren
            messagebox.showinfo("Eingabe inkorrekt", "Bitte gültige Note eingeben")
            return

        # Kurs in die abgeschlossenen Kurse einpflegen
        self.course_repository.insert_finished_course(course, grade)

        # Entferne Button vom Kurs
        self.dashboard.remove_course_button(course.name)
        # Methode zur Aktualisierung des Fortschritts ausführen
        self.dashboard.update_progress()
        # Methode zur Aktualisierung des Durchschnitts ausführen
        self.dashboard.update_average_grade()
        # Kurs-Fenster schließen
        self.view.close_window()