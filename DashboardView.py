import tkinter
from tkinter import *
from SubpageView import SubpageView
from DashboardController import DashboardController

class DashboardView(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # button_count zählt die Anzahl an aktiven Kursen
        self.button_count = 1
        self.course_buttons = {}
        self.controller = DashboardController(self)

        # Angaben des Studenten
        student_frame = LabelFrame(self, text="Informationen", padx=0, pady=10)
        student_frame.pack(fill='x', expand=False)
        student_frame.pack(padx=10, pady=10)
        self.student_information = Label(student_frame, text="Herzlich willkommen")
        self.student_information.pack()

        # Erstelle ein Frame für die Darstellung der Navigationselemente
        navigation_frame = LabelFrame(self, text="Navigationsleiste", padx=0, pady=20)
        navigation_frame.pack(fill='x', expand=False)
        navigation_frame.pack(padx=10, pady=10)

        # Erstelle Buttons für das Öffnen der Unterseiten
        subpage_button1 = Button(navigation_frame, text="Dashboard", fg="black", bg="grey", padx=50, pady=20, height=1,
                                 width=15)
        subpage_button2 = Button(navigation_frame, text="Unterseite 1", command=lambda: self.subpage_click(), fg="black",
                                 bg="grey", padx=50, pady=20, height=1, width=15)
        subpage_button3 = Button(navigation_frame, text="Unterseite 2", command=lambda: self.subpage_click(), fg="black",
                                 bg="grey", padx=50, pady=20, height=1, width=15)
        subpage_button4 = Button(navigation_frame, text="Unterseite 3", command=lambda: self.subpage_click(), fg="black",
                                 bg="grey", padx=50, pady=20, height=1, width=15)
        subpage_button5 = Button(navigation_frame, text="Unterseite 4", command=lambda: self.subpage_click(), fg="black",
                                 bg="grey", padx=50, pady=20, height=1, width=15)

        # Positionierung der Buttons für die Unterseite
        subpage_button1.grid(row=0, column=0, padx=50)
        subpage_button2.grid(row=0, column=1, padx=50)
        subpage_button3.grid(row=0, column=2, padx=50)
        subpage_button4.grid(row=0, column=3, padx=50)
        subpage_button5.grid(row=0, column=4, padx=50)

        # Erstelle ein Frame für die Darstellung der Kurse
        self.course_frame = LabelFrame(self, text="Kurse", padx=0, pady=20)
        self.course_frame.pack(fill='x', expand=False)
        self.course_frame.pack(padx=10, pady=10)

        # Button für das Hinzufügen von Kursen
        add_course_button = Button(self.course_frame, text="Kurs hinzufügen", command=lambda: self.controller.add_new_course(),
                                   fg="black", bg="grey", height=15, width=40)
        # Positionierung des Buttons
        add_course_button.grid(row=0, column=0, padx=50, pady=50)

        # Erstelle ein Frame für die Darstellung der Ziele (Studiumsdauer und Notendurchschnitt)
        goals_frame = LabelFrame(self, text="Ziele", padx=0, pady=20)
        goals_frame.pack(fill='x', expand=False)
        goals_frame.pack(padx=10, pady=10)

        # Label für den Fortschritt
        progress_text = Label(goals_frame, text="Prozentualer Fortschritt: ", padx=40, pady=10)
        # Slider, der prozentualen Fortschritt darstellen soll
        self.horizontal_slider = Scale(goals_frame, from_=0, to=100, orient=HORIZONTAL)

        # Label für den Notendurchschnitt
        average_text = Label(goals_frame, text="Notendurchschnitt: ", padx=40, pady=10)
        # Note wird in dieses Label eingetragen
        self.average_display_text = Label(goals_frame, text="", padx=40, pady=20)

        # Positionierungen der Labels im Grid
        progress_text.grid(row=0, column=0, padx=212)
        self.horizontal_slider.grid(row=1, column=0, padx=212)
        average_text.grid(row=0, column=1, padx=212)
        self.average_display_text.grid(row=1, column=1, padx=212)

        # Ein Button für die Anzeige der abeschlossenen Kurse und deren Noten
        add_course_button = Button(goals_frame, text="Bisherige Noten anzeigen", command=lambda: self.controller.display_grades(),
                                   fg="black", bg="grey", padx=40, pady=20)
        add_course_button.grid(row=0, column=2, rowspan=2, padx=50, pady=50)

        # Alle aktiven Kurse müssen dargestellt werden
        # Zu Beginn müssen Fortschritt und Durchschnittsnote aktualisiert werden
        self.controller.initialize_courses()
        self.controller.update_progress()
        self.controller.update_average_grade()


    # Methode die von der Login-Klasse aufgerufen wird, um Dashboard mit Information über den Studenten zu initialisieren
    def initialize(self, student, study, semester):
        # Hier wird der Text mit dem Namen vom Studenten und dem Studiengang ausgegeben
        self.student_information.config(
            text=f"Herzlich willkommen, {student.surname} {student.lastname}! \n Studiengang: {study.name} \n {semester.semester}. Semester")

    # Methode für das Öffnen der Unterseiten
    def subpage_click(self):
        subpage_view = SubpageView(self)
        self.pack_forget()
        subpage_view.pack(fill="both", expand=True)

    # Methode die einen neuen Button erstellt (für den zu erstellenden Kurs)
    def create_course_button(self, course):
        self.button_count += 1
        # Erstelle einen neuen Button für den hinzugefügten Kurs
        new_button = Button(self.course_frame, text=course.name,
                            command=lambda: self.controller.open_course(course), fg="black",
                            bg="grey", height=15, width=40)
        # Positionierung (Reihe und Spalte) des Buttons im grid mithilfe des button_count berechnen
        row = (self.button_count - 1) // 4
        column = (self.button_count - 1) % 4
        self.course_buttons[course.name] = new_button
        new_button.grid(row=row, column=column, padx=50, pady=50)

    # Methode zum Entfernen eines Kurs-Buttons (wird aufgerufen, wenn ein Kurs abgeschlossen wird und somit nicht mehr aktiv ist)
    def remove_course_button(self, course_name):
        # Entfernt den Button eines bestimmten Kurses
        if course_name in self.course_buttons:
            button = self.course_buttons.pop(course_name)
            # Entferne den Button aus der Anzeige
            button.grid_forget()
            # Verringere den Zähler der aktiven Kurse (Anzahl der aktiven Kurse entspricht der Anzahl der Kurs-Buttons)
            self.button_count -= 1

    # Methode für Aktualisierung des Sliders mit dem Fortschritt
    def set_progress(self, progress_percentage):
        self.horizontal_slider.set(progress_percentage)

    # Methode für Aktualisierung des Labels mit der Durchschnittsnote
    def set_average(self, average_grade):
        self.average_display_text.configure(text=str(average_grade))