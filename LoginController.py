from tkinter import messagebox
from Semester import Semester
from Student import Student
from Study import Study
from datetime import date
from datetime import datetime
from StudentRepository import StudentRepository

class LoginController:
    def __init__(self, view):
        self.view = view
        # Über student_repository erfolgen Zugriffe auf die Datenbank
        self.student_repository = StudentRepository()

        # Einträge aus der Datenbank abfragen
        records = self.student_repository.get_all_student_records()
        if records:
            # Wenn ein Eintrag vom Student existiert, so soll wieder das Objekt student erzeugt werden
            student = Student(records[0][0], records[0][1], records[0][2])
            study = Study(records[0][3])
            semester = Semester(records[0][4], date.fromisoformat(records[0][5]))
            # Beim Login wollen wir auch direkt das Semester überprüfen und entsprechend updaten
            semester.update_semester(records[0][2])

            # Debug der Angaben in der Konsole
            print(f"Name: {student.surname} {student.lastname}, Student ID: {student.id}, Studiengang: {study.name}")

            self.view.show_exisiting_user(student, study, semester)
        else:
            self.view.show_new_user_form()


    # Methode, die zur Erstellung vom Dashboard verwendet wird und mit den Eingaben des Nutzers arbeitet
    def init_dashboard(self, surname, lastname, study_name):
        # Warnung, wenn Eingabe fehlt
        if not surname or not lastname:
            messagebox.showinfo("Eingabe fehlt", "Bitte geben deinen/einen Namen an!")
            return

        # Student Objekt erzeugen lassen (dies ist vor allem wichtig, damit eine ID erstellt wird)
        student = Student(surname, lastname)
        # Studiengang basierend auf Auswahl in der Dropbox erstellen
        study = Study(study_name)
        # Es sollen einige Kurse als Beispiel hinzugefügt werden (abhängig vom Studiengang)
        study.add_starting_courses()
        # Das Semester wird erstellt mit dem heutigen Tag als Startdatum, sodass das Enddatum für das Semester erstellt werden kann
        semester = Semester(1, datetime.today().date())

        # Einträge in die Datenbank einpflegen
        self.student_repository.save_student(student, study, semester)

        # Dashboard mit den Eingaben initialisieren und aufrufen
        self.open_dashboard(student, study, semester)

    # Methode, die mit dem Zurücksetzen-Button aufgerufen werden kann, um alle Daten zu löschen (inklusive Name und Studiengang)
    def reset_all(self):
        # Einträge aus der Datenbank löschen
        self.student_repository.reset_database()
        self.view.restart_app()

    # Methode für das Aufrufen des Dashboards
    def open_dashboard(self, student: Student, study, semester):
        self.view.open_dashboard(student, study, semester)




