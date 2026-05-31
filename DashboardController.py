from tkinter import *
from Course import Course
from Exam import Exam
from Project import Project
from CourseRepository import CourseRepository
from CourseController import CourseController
from tkinter import messagebox

class DashboardController:
    def __init__(self, view):
        self.view = view
        self.course_repository = CourseRepository()
        self.course_controller = CourseController(self)

    # Zu Beginn müssen alle Kurse aktiven aus der Datenbank erhalten und dargestellt werden
    def initialize_courses(self):
        # Alle aktiven Kurse aus der Datenbank erhalten
        courses_data = self.course_repository.get_all_course_data()

        # Exammination wurde als String abgespeichert und basierend darauf wird wieder das Objekt erstellt
        if courses_data:
            for record in courses_data:
                if record[3] == "Klausur":
                    examination = Exam(None, 90)
                elif record[3] == "Projekt":
                    examination = Project(None, "31.12.2026")

                # Kurs wird mit den Attributen erstellt
                course = Course(record[0], record[1], examination)
                # Für jeden Kurs einen Button erstellen lassen
                self.view.create_course_button(course)

        # Zu Beginn muss auch Fortschritt und Durchschnittsnote aktualisiert werden
        self.update_progress()
        self.update_average_grade()

    # Methode für Erstellung eines neuen Kurses
    def add_new_course(self):
        if self.view.button_count > 7:
            # Warnung, wenn zu viele aktive Kurse vorhanden sind
            messagebox.showinfo("Übernimm dich nicht",
                                "Bitte schließe erst mal Kurse ab, bevor du weitere startest!")
            return

        # Einstellungen vom Fenster
        editor = Toplevel()
        editor.title('Kurs hinzufügen')
        editor.geometry('500x500')

        # Methode, die aufgerufen wird, wenn Nutzer die Eingaben bestätigt und den Kurs erstellt
        def submit():
            print(exam_type.get())
            examination = None
            if exam_type.get() == "Klausur":
                # Die Dauer wird der Einfachheit halber auf 90 Minuten festgelegt für alle Klausuren
                # Die Note existiert noch nicht
                examination = Exam(None, 90)
            elif exam_type.get() == "Projekt":
                # Die Deadline wird der Einfachheit halber auf 2026 festgelegt für alle Projekte
                # Die Note existiert noch nicht
                examination = Project(None, "31.12.2026")

            # Objekt der Klasse Kurs mit Nutzereingaben erstellen
            course = Course(c_name.get(), c_description.get(), examination)

            # Kurs in die Datenbank einpflegen
            self.course_repository.add_new_course(course.name, course.description, examination.name)

            # Methode zum Erstellen eines Buttons für den Kurs aufrufen
            self.view.create_course_button(course)

            # Fenster schließen
            editor.destroy()

        # Kursname Label
        c_name_label = Label(editor, text="Kursname")
        c_name_label.grid(row=0, column=0)
        # Eingabefeld für den Kursnamen
        c_name = Entry(editor, width=30)
        c_name.grid(row=0, column=1, padx=20)

        # Kursbeschreibung Label
        c_description_label = Label(editor, text="Kursbeschreibung")
        c_description_label.grid(row=1, column=0)
        # Eingabefeld für die Kursbeschreibung
        c_description = Entry(editor, width=30)
        c_description.grid(row=1, column=1, padx=20)

        # Festlegung von Klausur als Standard Prüfungsleistung
        exam_type = StringVar(value="Klausur")
        # Radiobutton ermöglichen Nutzer die Auswahl der Prüfungsleistung (zwischen Klausur und Projekt wählbar)
        Radiobutton(editor, text="Klausur", variable=exam_type, value="Klausur",
                    command=lambda: print(exam_type.get())).grid(row=3, column=0)
        Radiobutton(editor, text="Projekt", variable=exam_type, value="Projekt",
                    command=lambda: print(exam_type.get())).grid(row=3, column=1)

        # Button zum Speichern
        submit_button = Button(editor, text="Kurs speichern", command=submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        # Label für die Ausgabe der Kurse
        course_list = Label(editor, text="")
        course_list.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    # Wenn auf Kurs geklickt wird, wird an course_controller weitergeleitet
    def open_course(self, course):
        self.course_controller.open_course_page(course, self.view)

    # Wenn ein Kurs abgeschlossen wird, dann kann der Kurs-Button über diese Methode vom Dashboard entfernt werden
    def remove_course_button(self, course_name):
        self.view.remove_course_button(course_name)

    # Methode, die alle Noten in einem neuen Fenster darstellt
    def display_grades(self):
        # Einstellungen vom Fenster
        editor = Toplevel()
        editor.title('Noten')

        # Kurse Label
        course_frame = LabelFrame(editor, text="Kurse", padx=0, pady=0)
        course_frame.pack()
        # Textfeld für Liste der Noten
        finished_courses_label = Label(course_frame, text="")
        finished_courses_label.grid(row=1, column=1, pady=30, padx=30)

        # Alle abgeschlossenen Kurse aus der Datenbank abfragen
        finished_courses = self.course_repository.get_all_finished_courses()

        # String mit allen Einträgen erstellen
        print_records = ''
        if finished_courses:
            for record in finished_courses:
                # Namen, Note und Typ der Prüfungsleistung für jeden einzelnen Eintrag erhalten
                print_records += str(record[0] + ", Note: " + str(record[2]) + " (" + str(record[3])) + ")\n" + "\n"
        else:
            print_records = "Es wurden noch keine Kurse abgeschlossen"

        # Textfeld für Liste der Noten aktualisieren
        finished_courses_label.configure(text=print_records)

    # Methode für Aktualisierung des Sliders mit dem Fortschritt
    def update_progress(self):
        finished_courses_count = self.course_repository.get_finished_courses_count()

        # Wir gehen davon aus, dass es 6 Semester sind mit je 6 Kursen und somit insgesamt 36 Kurse
        progress_percentage = (finished_courses_count / 36) * 100

        # View mit dem berechneten Fortschritt aktualisieren
        self.view.set_progress(progress_percentage)

    # Methode für Aktualisierung des Labels mit der Durchschnittsnote
    def update_average_grade(self):
        finished_courses_count = self.course_repository.get_finished_courses_count()
        finished_courses_grades = self.course_repository.get_finished_courses_grades()

        grade_sum = 0
        average_grade = 0
        # Berechnung basierend auf Einträge der Noten in der Datenbank
        if finished_courses_grades:
            for record in finished_courses_grades:
                grade_sum += record[2]
            average_grade = grade_sum / finished_courses_count

        # View mit der berechneten Durchschnittsnote aktualisieren
        self.view.set_average(average_grade)