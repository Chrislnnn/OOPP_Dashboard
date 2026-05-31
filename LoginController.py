import sqlite3
import tkinter
from tkinter import ttk, messagebox
from Dashboard import Dashboard
from Semester import Semester
from Student import Student
from Study import Study
from Subpage import Subpage
from datetime import date
from datetime import datetime

class Login(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard Projekt")
        self.dashboard = Dashboard(self, self)
        self.subpage = Subpage(self, self)

        # Definierte Auswahl an möglichen Studiengängen (der einfachheit halber nur 2)
        # Diese werden die voreingestellten Kurse im Dashboard beeinflussen
        courses_of_study = ["Software Engineering", "Mathematics"]

        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Daten aus finished courses auswählen
        cursor.execute("SELECT *, oid FROM students")
        records = cursor.fetchall()

        # Darstellung der Login-Seite muss davon abhängig sein, ob bereits Einträge vom Studenten in der Datenbank existieren.
        # In diesem Prototyp wird es nicht erlaubt, mehr als einen Studenten zu erstellen
        if records:
            # Wenn ein Eintrag vom Student existiert, so soll wieder das Objekt student erzeugt werden
            student = Student(records[0][0],records[0][1],records[0][2])
            study = Study(records[0][3])
            semester = Semester(records[0][4], date.fromisoformat(records[0][5]))
            # Beim Login wollen wir auch direkt das Semester überprüfen und entsprechend updaten
            semester.update_semester(records[0][2])

            #Debug der Angaben in der Konsole
            print(f"Name: {student.surname} {student.lastname}, Student ID: {student.id}, Studiengang: {study.name}")

            # Login-Seite
            self.login_page = tkinter.Frame(self)
            self.login_page.pack(fill="both",expand=True)
            tkinter.Label(self.login_page, text="Willkommen zurück!").grid(row=0, column=0, columnspan=2, pady=20, padx=20)

            # Eingabefeld für den Vornamen
            surname_label = tkinter.Label(self.login_page, text="Vorname: " + records[0][0])
            surname_label.grid(row=1, columnspan=2, pady=10, padx=20)

            # Eingabefeld für den Nachnamen
            lastname_label = tkinter.Label(self.login_page, text="Nachname: " + records[0][1])
            lastname_label.grid(row=2, columnspan=2, pady=10, padx=20)

            # Auswahl vom Studiengang mit drop box
            studies_label = tkinter.Label(self.login_page, text="Studiengang: " + records[0][3])
            studies_label.grid(row=3, columnspan=2, pady=10, padx=20)

            # Button zum Bearbeiten von persönlichen Informationen
            create_dashboard_button = tkinter.Button(self.login_page, text="Persönliche Informationen anpassen",command=lambda: student.update_info())
            create_dashboard_button.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

            # Button zum Erstellen des Dashboards
            create_dashboard_button = tkinter.Button(self.login_page, text="Zum Dashboard",command=lambda: self.show_dashboard(student, study, semester))
            create_dashboard_button.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="ew")
        else:
            # Login-Seite
            self.login_page = tkinter.Frame(self)
            self.login_page.pack(fill="both",expand=True)
            tkinter.Label(self.login_page, text="Willkommen! Du kannst hier dein neues Dashboard erstellen.").grid(row=0, column=0, columnspan=2, pady=20, padx=20)

            # Button zum Erstellen des Dashboards
            create_dashboard_button = tkinter.Button(self.login_page, text="Dashboard erstellen",command=self.init_dashboard)
            create_dashboard_button.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

            # Eingabefeld für den Vornamen
            surname_label = tkinter.Label(self.login_page, text="Vorname: ")
            surname_label.grid(row=1, column=0, pady=10, padx=20)
            self.surname_input = tkinter.Entry(self.login_page, width=30)
            self.surname_input.grid(row=1, column=1, pady=10, padx=20)

            # Eingabefeld für den Nachnamen
            lastname_label = tkinter.Label(self.login_page, text="Nachname: ")
            lastname_label.grid(row=2, column=0, pady=10, padx=20)
            self.lastname_input = tkinter.Entry(self.login_page, width=30)
            self.lastname_input.grid(row=2, column=1, pady=10, padx=20)

            # Auswahl vom Studiengang mit drop box
            studies_label = tkinter.Label(self.login_page, text="Studiengang: ")
            studies_label.grid(row=3, column=0, pady=10, padx=20)
            self.studies_drop_box = ttk.Combobox(self.login_page, values=courses_of_study)
            self.studies_drop_box.current(0)
            self.studies_drop_box.grid(row=3, column=1, pady=10, padx=20)



        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()


        # Button zum Zurücksetzen des Dashboards (Achtung dies wird auch den Namen und Studiengang löschen)
        reset_dashboard_button = tkinter.Button(self.login_page, text="Alles zurücksetzen", command=self.reset_all)
        reset_dashboard_button.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="ew")



        self.login_page.pack(fill="both", expand=True)

    # Methode zum Initialisieren der Datenbank und den darin vorhanden Tabellen (wurde beim ersten Starten aufgerufen, damit die study_database.db erstellt wurde)
    def initialize_database(self):
        # Eine Datenbank muss erstellt werden
        conn = sqlite3.connect('study_database.db')
        # Ein Cursor wird benötigt
        cursor = conn.cursor()
        # Table für Studenten erstellen
        cursor.execute("""CREATE TABLE students (
                                               student_surname text,
                                               student_lastname text,
                                               student_id integer,
                                               study text,
                                               semester integer,
                                               semester_start_date DATE,
                                               semester_end_date DATE)""")
        # Table für aktuelle Kurse erstellen
        cursor.execute("""CREATE TABLE courses (
                                   course_name text,
                                   course_description text,
                                   course_grade integer,
                                   course_examination text)""")
        # Table für abgeschlossene Kurse erstellen
        cursor.execute("""CREATE TABLE finished_courses (
                                   course_name text,
                                   course_description text,
                                   course_grade integer,
                                   course_examination text)""")
        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

    # Methode, die zur Erstellung vom Dashboard verwendet wird und mit den Eingaben des Nutzers arbeitet
    def init_dashboard(self):
        # Namen vom Studenten erhalten
        surname = self.surname_input.get()
        lastname = self.lastname_input.get()

        # Warnung, wenn Eingabe fehlt
        if not surname or not lastname:
            messagebox.showinfo("Eingabe fehlt", "Bitte geben deinen/einen Namen an!")
            return

        # Student Objekt erzeugen lassen (dies ist vor allem wichtig, damit eine ID erstellt wird)
        student = Student(surname, lastname)
        # Studiengang basierend auf Auswahl in der Dropbox erstellen
        study = Study(self.studies_drop_box.get())
        # Es sollen einige Kurse als Beispiel hinzugefügt werden (abhängig vom Studiengang)
        study.add_starting_courses()
        # Das Semester wird erstellt mit dem heutigen Tag als Startdatum, sodass das Enddatum für das Semester erstellt werden kann
        semester = Semester(1, datetime.today().date())

        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Daten vom Studenten und den Studiengang einpflegen
        cursor.execute("INSERT INTO students VALUES (:student_surname, :student_lastname, :student_id, :study, :semester, :semester_start_date, :semester_end_date)",
                       {
                           'student_surname': student.surname,
                           'student_lastname': student.lastname,
                           'student_id': student.id,
                           'study': study.name,
                           'semester': semester.semester,
                           'semester_start_date': semester.start.isoformat(),
                           'semester_end_date': semester.end.isoformat()
                       })

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        # Dashboard mit den Eingaben initialisieren und aufrufen
        self.show_dashboard(student, study, semester)

    # Methode, die mit dem Zurücksetzen-Button aufgerufen werden kann, um alle Daten zu löschen (inklusive Name und Studiengang)
    def reset_all(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Einträge aus den Tabellen entfernen
        cursor.execute("DELETE FROM students")
        cursor.execute("DELETE FROM courses")
        cursor.execute("DELETE FROM finished_courses")

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        # Aktuelles Fenster schließen und erneut starten
        self.destroy()
        self.__init__()

    # Methode für das Aufrufen des Dashboards
    def show_dashboard(self, student: Student, study, semester):
        self.dashboard = Dashboard(self, self)
        # Die initialize-Methode in der Klasse Dashboard wird aufgerufen
        self.dashboard.initialize(student, study, semester)
        # Alle anderen Seiten schließen
        self.login_page.pack_forget()

        # Dashboard verpacken
        self.dashboard.pack(fill="both", expand=True)



# Es soll immer zuerst die Login-Seite gestartet werden bei der Ausführung
if __name__ == "__main__":
    app = Login()
    app.mainloop()
