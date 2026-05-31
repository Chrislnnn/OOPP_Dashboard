from tkinter import *

class CourseView(Toplevel):
    def __init__(self, parent, controller, course):
        super().__init__(parent)
        self.controller = controller
        self.course = course
        self.title('Kurs Darstellung')
        self.geometry('500x500')

        # Kursname Label
        c_name_label = Label(self, text="Kursname: ")
        c_name_label.grid(row=0, column=0)
        # Der Kursname wird hier ausgegeben
        c_name = Label(self, text=course.name)
        c_name.grid(row=0, column=1, padx=20)

        # Kursbeschreibung Label
        c_description_label = Label(self, text="Kursbeschreibung: ")
        c_description_label.grid(row=1, column=0)
        # Die Kursbeschreibung wird hier ausgegeben
        c_description = Label(self, text=course.description)
        c_description.grid(row=1, column=1, padx=20)

        # Prüfungsleistung Label
        c_description_label = Label(self, text="Prüfungsleistung: ")
        c_description_label.grid(row=2, column=0)
        # Typ der Prüfungsleistung wird hier ausgegeben (Klausur oder Projekt)
        c_description = Label(self, text=course.examination.name)
        c_description.grid(row=2, column=1, padx=20)

        # Kursnote Label
        c_grade_label = Label(self, text="Kursnote")
        c_grade_label.grid(row=3, column=0)
        # Eingabefeld für die Kursnote
        c_grade = Entry(self, width=30)
        c_grade.grid(row=3, column=1, padx=20)

        # Button zum Abschließen des Kurses (ruft die finish_course Methode auf)
        submit_button = Button(self, text="Kurs abschließen", command=lambda: self.controller.finish_course(course, c_grade.get()) )
        submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    def close_window(self):
        # Fenster schließen
        self.destroy()
