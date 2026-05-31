import tkinter
from tkinter import *
from SubpageController import SubpageController

class SubpageView(tkinter.Frame):
    def __init__(self, dashboard):
        super().__init__()
        # Controller für das View
        self.controller = SubpageController(self, dashboard)

        # Frame für die Darstellung der Navigationselemente erstellen
        navigation_frame = LabelFrame(self, text="Navigationsleiste", padx=0, pady=50)
        navigation_frame.pack(padx=10, pady=10)

        # Buttons für das Öffnen der Unterseiten erstellen
        subpage_button_1 = Button(navigation_frame, text="Dashboard", command=lambda: self.main_page_click(dashboard), fg="black",
                                  bg="grey", padx=40, pady=20)
        subpage_button_2 = Button(navigation_frame, text="Unterseite 1", command=lambda: self.subpage_click(),
                                  fg="black", bg="grey", padx=40, pady=20)
        subpage_button_3 = Button(navigation_frame, text="Unterseite 2", command=lambda: self.subpage_click(),
                                  fg="black", bg="grey", padx=40, pady=20)
        subpage_button_4 = Button(navigation_frame, text="Unterseite 3", command=lambda: self.subpage_click(),
                                  fg="black", bg="grey", padx=40, pady=20)
        subpage_button_5 = Button(navigation_frame, text="Unterseite 4", command=lambda: self.subpage_click(),
                                  fg="black", bg="grey", padx=40, pady=20)

        # Positionierung der Buttons für die Unterseite
        subpage_button_1.grid(row=0, column=0, padx=50)
        subpage_button_2.grid(row=0, column=1, padx=50)
        subpage_button_3.grid(row=0, column=2, padx=50)
        subpage_button_4.grid(row=0, column=3, padx=50)
        subpage_button_5.grid(row=0, column=4, padx=50)

        # Erstelle ein Frame für die Darstellung der aktuellen Kurse und der abgeschlossenen Kurse
        course_frame = LabelFrame(self, text="Kurse", padx=0, pady=50)
        course_frame.pack(padx=10, pady=10)

        # Label für die aktiven Kurse (Überschrift)
        current_courses_label = Label(course_frame, text="Aktuelle Kurse")
        current_courses_label.grid(row=0, column=0, pady=10, padx=10)
        # Label für die aktiven Kurse (Für die Ausgabe der Liste an Kursen)
        self.current_courses = Label(course_frame, text="")
        self.current_courses.grid(row=1, column=0, pady=10, padx=10)

        # Label für die abgeschlossenen Kurse (Überschrift)
        finished_courses_label = Label(course_frame, text="Abgeschlossene Kurse")
        finished_courses_label.grid(row=0, column=1, pady=10, padx=10)
        # Label für die abgeschlossenen Kurse (Für die Ausgabe der Liste an Kursen)
        self.finished_courses = Label(course_frame, text="")
        self.finished_courses.grid(row=1, column=1, pady=10, padx=10)

        # Hinweis
        info_text = Label(course_frame, text="Die Liste wird erst nach einem Neustart aktualisiert!")
        info_text.grid(row=2, columnspan=2, pady=10, padx=10)

        self.controller.display_courses()

    # Methode für die Ausgabe aller Kurse
    def show_courses(self, active_courses_records, finished_courses_records):
        self.current_courses.configure(text=active_courses_records)
        self.finished_courses.configure(text=finished_courses_records)

    # Methoden, die aufgerufen wird, wenn Nutzer auf eine andere Unterseite klickt
    # Es wird keine neue Unterseite geöffnet, sondern nur eine Info ausgegeben
    def subpage_click(self):
        navigate_to_subpage_label = Label(self, text="Dieser Button könnte an eine andere Unterseite weiterleiten!")
        navigate_to_subpage_label.pack()

    # Methode, die aufgerufen wird, wenn der Nutzer auf den Dashboard-Button klickt
    def main_page_click(self, dashboard):
        self.pack_forget()
        dashboard.pack(fill="both", expand=True)